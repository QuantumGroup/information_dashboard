"""
This class takes in a list of RSS feeds, downloads their data, parses that data, and saves that
data to the database.
"""


class RSS_Collector():

    def __init__(self, rss_url, error_log, debug):
        self.rss_url = rss_url
        self.error_log = error_log
        self.debug = debug

    def rss_ingestor(self, rss_url, error_log, debug):
        import feedparser

        return feedparser.parse(rss_url)

    def rss_parser(self, rss_url, error_log, debug):
        import os
        import json
        import calendar
        import time
        import random
        import sys
        import sqlite3
        import re
        from urllib.parse import urlparse

        # this instantiates the feedparser instance and returns the relevant data as an 'items' entry in a JSON object
        feed = self.rss_ingestor(rss_url, error_log, debug)

        # for each 'items' in the feedparser object (aka, for every RSS entry), we save the JSON object locally
        for item in feed['items']:
            rss_json_raw = json.dumps(item)
            rss_json = json.loads(rss_json_raw)

            # we create the variables for each JSON value we wish to record: the following blocks go through each step,
            # with slight variations depending on the RSS source.
            # NB: the fact that each RSS entry is different based on the source means that adding a source to the RSS
            # reader cannot be done at the user level, but must be programmed in every time.

            # this block parses the URL in order to determine the organization responsible for the feed. This is how
            # sourcing is determined, and the results of this block are used by the rest of the variable creation code.
            try:
                str_url = rss_json['link']
                parsed_url = urlparse(str_url)
                hostname_url = parsed_url.hostname
                organization = str(hostname_url[4:-4])
            except:
                organization = 'None'
                e = sys.exc_info()[0]
                print('organization error\n' + str(str_url) + '\n' + str(e))
            print(str_url)
            print('organization is ' + organization)

            # This block extracts the date published from the RSS JSON object, from the website URL, or if neither is
            # possible, uses the time during which this script is run (since the script is meant to be run on a regular
            # basis, there should not be many duplicates): which method is used depends on the organization, since the
            # organization chooses their method of publishing this data (if at all).
            # The following regular expression strips dates from URLs, and the line after that converts that regex
            # object to a Python date object
            # url_date_regex = re.search(r'([\./\-_]{0,1}(19|20)\d{2})[\./\-_]{0,1}(([0-3]{0,1}[0-9][\./\-_])|'
            #                            r'(\w{3,5}[\./\-_]))([0-3]{0,1}[0-9][\./\-]{0,1})?', str_url)
            # url_date = time.strptime(str(url_date_regex.group(0)), '/%Y/%m/%d/')
            try:
                if organization == 'nytimes':
                    #  NY Times has a published value in the RSS JSON object
                    published_raw = str(rss_json['published'])
                    published_struct = time.strptime(published_raw, '%a, %d %b %Y %H:%M:%S %Z')
                    published = str(time.strftime('%c', published_struct))
                elif organization == 'washingtonpost':
                    # todo: attempt to combine date from RSS JSON object with time when the script is run
                    # WaPo contains the date but not the time the article is published in the URL; therefore, we will
                    # use the time this script is run on a WaPo RSS object
                    published_int = int(time.time())
                    published_struct = time.gmtime(published_int)
                    published = str(time.strftime('%c', published_struct))
            except:
                published = 'None'
                e = sys.exc_info()
                print('published error\n' + str(e))
            print('published is ' + published)

            # This block extracts the article title from the RSS JSON object
            try:
                if organization == 'nytimes':
                    title = str(rss_json['title'])
                elif organization == 'washingtonpost':
                    title = str(rss_json['title'])
            except:
                title = 'None'
                e = sys.exc_info()
                print('title error\n' + str(e))
            print('title is ' + title)

            # this block uses the 'published' time, converted into seconds since epoch, plus five (5) random integers
            # at the end, as unique identifiers for each entry
            try:
                if organization == 'nytimes':
                    try:
                        time_id = str(calendar.timegm(time.strptime(published, '%a %b %d %H:%M:%S %Y')))
                    except ValueError:
                        time_id = str(calendar.timegm(time.strptime(published, '%a, %b %d %H:%M:%S %Y')))
                    time_addition = random.sample(range(99999), 1)
                    uid = time_id + str(time_addition[0])
                elif organization == 'washingtonpost':
                    try:
                        time_id = str(calendar.timegm(time.strptime(published, '%a %b %d %H:%M:%S %Y')))
                    except ValueError:
                        time_id = str(calendar.timegm(time.strptime(published, '%a, %b %d %H:%M:%S %Y')))
                    time_addition = random.sample(range(99999), 1)
                    uid = time_id + str(time_addition[0])
            except:
                time_id_list = random.sample(range(9999999999), 1)
                uid = str(time_id_list[0])
                e = sys.exc_info()
                print('uid error\n' + str(e))
            print('uid is ' + uid)

            # this block looks for a story summary embedded within the RSS JSON object
            try:
                if organization == 'nytimes':
                    summary_dict = rss_json['content'][0]
                    summary = str(summary_dict['value'])
                elif organization == 'washingtonpost':
                    summary = str(rss_json['summary'])
            except:
                summary = 'None'
                e = sys.exc_info()
                print('summary error\n' + str(e))
            print('summary is ' + summary)

            # this block returns the website content from the URL specified in the RSS JSON object
            # todo: properly call web scraper method with appropriate arguments
            target_url = ''
            content = self.rss_scraper(target_url)
            print('content is ' + content)

            # # prints out the resulting variables for debugging purposes
            # if debug is True:
            #     print(uid + '\n' + organization + '\n' + published + '\n' + 'title: ' + title + '\n' + 'summary: ' +
            #           summary + '\n' + content + '\n---\n')

            # sets up the connection to the SQLite database
            sqlite_database = os.path.join('collector.sqlite3')
            conn = sqlite3.connect(sqlite_database)
            c = conn.cursor()
            # saves each variable to the database using DB-API's parameter substitution, where '?' is a stand-in for a
            # tuple element containing the actual values
            c.execute('INSERT INTO rss VALUES (?,?,?,?,?,?)',
                      (uid, organization, published, title, summary, content))
            # commits the changes to the database
            try:
                conn.commit()
            except sqlite3.Error as e:
                print('database commit error\n' + str(e))

    def rss_scraper(self, url):
        # todo: build website scraper that takes in  URL and returns main body text, tailored for each required RSS feed
        return 'TEST WEBSITE CONTENT'