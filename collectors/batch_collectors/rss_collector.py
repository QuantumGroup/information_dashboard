"""
This class takes in a list of RSS feeds, downloads their data, parses that data, and saves that
data to the database.
"""


class RSS_Collector():

    def __init__(self, rss_url, error_log, debug, e_tags, last_modifieds):
        self.rss_url = rss_url
        self.error_log = error_log
        self.debug = debug
        self.e_tag = e_tags
        self.last_modifieds = last_modifieds

    def rss_ingestor(self, rss_url, error_log, debug, e_tags, last_modifieds):
        import feedparser
        import sys
        import control

        try:
            if rss_url in control.e_tags:
                print('etag found for ' + rss_url)
                e_tag = control.e_tags[rss_url]
                print(e_tag)
                parser = feedparser.parse(rss_url, etag=e_tag)
                control.e_tags[rss_url] = parser.etag

            elif rss_url in control.last_modifieds:
                print('last-modified found for ' + rss_url)
                last_modified = control.last_modifieds[rss_url]
                print(last_modified)
                parser = feedparser.parse(rss_url, modified=last_modified)
                control.last_modifieds[rss_url] = parser.modified

            else:
                parser = feedparser.parse(rss_url)
                try:
                    control.e_tags[rss_url] = parser.etag
                except:
                    e = sys.exc_info()
                    print('no etag found for ' + rss_url)
                    print(str(e))
                try:
                    control.last_modifieds[rss_url] = parser.modified
                except:
                    e = sys.exc_info()
                    print('no last-modified found for ' + rss_url)
                    print(str(e))

        except:
            e = sys.exc_info()
            print(str(e))
            print('failure')

        return parser

    def rss_parser(self, rss_url, error_log, debug, e_tags, last_modifieds):
        # local file imports
        import control
        # Python library imports
        import os
        import json
        import sys
        import sqlite3
        import re
        import datetime
        import time
        from urllib.parse import urlparse

        if control.debug is True:
            print('starting RSS Collector\n'
                  '======================\n\n')

        # sets up the connection to the SQLite database
        sqlite_database_path = os.path.join('collector.sqlite3')
        sqlite_database = os.path.abspath(sqlite_database_path)
        conn = sqlite3.connect(sqlite_database)
        c = conn.cursor()

        # this instantiates the feedparser instance and returns the relevant data as an 'items' entry in a JSON object
        feed = self.rss_ingestor(rss_url, error_log, debug, e_tags, last_modifieds)

        if control.debug is True:
            current_time_int = int(time.time())
            current_time_struct = time.gmtime(current_time_int)
            current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
            print('--------------------------------------------------------------------------------------------\n'
                  'batch ingested from the RSS feed on %s: comparing entries to database\n'
                  '--------------------------------------------------------------------------------------------\n'
                  % current_time)

        # for each 'items' in the feedparser object (aka, for every RSS entry), we save the JSON object locally
        for item in feed['items']:

            rss_json_raw = json.dumps(item)
            rss_json = json.loads(rss_json_raw)

            # we create the variables for each JSON value we wish to record: the following blocks go through each step,
            # with slight variations depending on the RSS source.
            # NB: the fact that each RSS entry is different based on the source means that adding a source to the RSS
            # reader cannot be done at the user level, but must be programmed in every time.

            # this block parses the URL in order to determine the name of the organization responsible for the feed.
            # This is how sourcing is determined, and the results of this block are used by the rest of the variable
            # creation code.
            try:
                str_url = rss_json['link']
                # this saves the whole link, to be used as an identifier so as to not save the same story twice in our
                # database, and for use to download the content from the site itself
                url = str(str_url)
                parsed_url = urlparse(str_url)
                hostname_url = parsed_url.hostname
                if debug is True:
                    print('hostname: ' + str(hostname_url))
                if hostname_url == 'www.nytimes.com':
                    name = 'The New York Times (USA)'
                elif hostname_url == 'www.washingtonpost.com':
                    name = 'The Washington Post (USA)'
                elif hostname_url == 'smh.com.au':
                    name = 'The Sydney Morning Herald (AUS)'
                elif hostname_url == 'www.thedailystar.net':
                    name = 'The Daily Star (IND)'
                elif hostname_url == 'timesofindia.indiatimes.com':
                    name = 'The Times of India (IND)'
                elif hostname_url == 'www.thehindu.com':
                    name = 'The Hindu (IND)'
                elif hostname_url == 'www.haaretz.com':
                    name = 'Haaretz (ISR)'
                elif hostname_url == 'www.nation.co.ke':
                    name = 'The Nation (KEN)'
                elif hostname_url == 'app.yonhapnews.co.kr':
                    name = 'Yonhap (KOR)'
                elif hostname_url == 'www.straitstimes.com':
                    name = 'The Straits Times (SGP)'
                elif hostname_url == 'www.taipeitimes.com':
                    name = 'Taipei Times (TWN)'
                elif hostname_url == 'www.bbc.co.uk':
                    name = 'BBC (GBR)'
                elif hostname_url == 'www.csmonitor.com':
                    name = 'The Christian Science Monitor (USA)'
                elif hostname_url == 'www.wsj.com':
                    name = 'The Wall Street Journal (USA)'
                elif hostname_url == 'hosted2.ap.org':
                    name = 'AP (USA)'
                elif hostname_url == 'feeds.reuters.com':
                    name = 'Reuters (GBR)'
                elif hostname_url == 'www.latimes.com':
                    name = 'The Los Angeles Times (USA)'
                else:
                    name = str(hostname_url[4:-4])
            except:
                url = 'None'
                name = 'None'
                e = sys.exc_info()[0]
                print('name error\n' + str(str_url) + '\n' + str(e))

            # this block checks the database to see if the URL in the new article matches any URLs already captured: if
            # not a match, the script continues the pre-processing and downloading process; if yes a match, pass
            c.execute('SELECT url FROM rss')
            urls = c.fetchall()
            if url not in str(urls):
                if debug is True:
                    print('name: ' + name)

                # This block extracts the time published from the RSS JSON object, or the date from the website URL.
                try:
                    if name == 'The New York Times (USA)' or name == 'The Times of India (IND)' or name == 'BBC (GBR)':
                        # These have a published value in the JSON object: "Wed, 27 Dec 2017 13:08:10 GMT"
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%a, %d %b %Y %H:%M:%S %Z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Sydney Morning Herald (AUS)':
                        # These have a published value in the JSON object: "Wed Dec 27 15:11:22 UTC 2017"
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%a %b %d %H:%M:%S %Z %Y')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Daily Star (IND)' or name == 'The Hindu (IND)' or name == 'Haaretz (ISR)' or \
                            name == 'The Straits Times (SGP)' or name == 'Reuters (GBR)':
                        # These have a published value in the JSON object: "Wed, 27 Dec 2017 00:00:00 +0600"
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%a, %d %b %Y %H:%M:%S %z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Nation (KEN)':
                        # These have a published value in the JSON object: 2017-12-27T14:38:54Z
                        published_raw = str(rss_json['updated'])
                        published_stripped = published_raw[:-1]
                        published_struct = time.strptime(published_stripped, '%Y-%m-%dT%H:%M:%S')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'Yonhap (KOR)':
                        # These have a published value in the JSON object: 20171227145701
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%Y%m%d%H%M%S')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'Taipei Times (TWN)' or name == 'AP (USA)':
                        # these have a published value in the JSON object: 2017-12-28T08:00:00+08:00
                        if name == 'Taipei Times (TWN)':
                            published_raw = str(rss_json['updated'])
                        elif name == 'AP (USA)':
                            published_raw = str(rss_json['published'])
                        # since Python time objects don't support colons in the middle of UTC offsets, this will strip
                        # out the last three chars in the string and replace them with two (2) zeros (0s), so as to
                        # complete the full offset as understood by the datetime library's %z directive
                        published_stripped = published_raw[:-3]
                        published_assembled = published_stripped + '00'
                        published_struct = time.strptime(published_assembled, '%Y-%m-%dT%H:%M:%S%z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Wall Street Journal (USA)' or name == 'The Los Angeles Times (USA)':
                        # these have a published value in the JSON object: Wed, 27 Dec 2017 03:00:00 PST
                        published_raw = str(rss_json['published'])
                        if name == 'The Wall Street Journal (USA)':
                            published_stripped = published_raw[:-3]
                            published_assembled = published_stripped + '-0500'
                        elif name == 'The Los Angeles Times (USA)':
                            published_stripped = published_raw[:-3]
                            published_assembled = published_stripped + '-0800'
                        published_struct = time.strptime(published_assembled, '%a, %d %b %Y %H:%M:%S %z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Washington Post (USA)' or name == 'The Christian Science Monitor (USA)':
                        # These contain the date but not the time the article is published in the URL; therefore,
                        # we will use only the date
                        # ---------------------------
                        # The following regular expression strips dates from URLs, and the line after that converts that
                        # regex object to a Python date object
                        # todo: issue with regex where if year in headline, regex fails to parse date (<class 'ValueError'>, ValueError("time data '-2017-has-' does not match format '/%Y/%m/%d/'",)
                        url_date_regex = re.search(
                            r'([./\-_]{0,1}(19|20)\d{2})[./\-_]{0,1}(([0-3]{0,1}[0-9][./\-_])|'
                            r'(\w{3,5}[./\-_]))([0-3]{0,1}[0-9][./\-]{0,1})?', str_url)
                        if name == 'The Washington Post (USA)':
                            url_date = time.strptime(str(url_date_regex.group(0)), '/%Y/%m/%d/')
                        elif name == 'The Christian Science Monitor (USA)':
                            url_date = time.strptime(str(url_date_regex.group(0)), '/%Y/%m%d/')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(url_date)))
                except:
                    published = 'None'
                    e = sys.exc_info()
                    print('published error\n' + str(e))
                if debug is True:
                    print('published: ' + published)

                # this block returns the date and time when the RSS entry was imported
                try:
                    imported_int = int(time.time())
                    imported_struct = time.gmtime(imported_int)
                    imported = str(datetime.datetime.fromtimestamp(time.mktime(imported_struct)))
                except:
                    imported = 'None'
                    e = sys.exc_info()
                    print('imported error\n' + str(e))
                if debug is True:
                    print('imported: ' + imported)

                # This block extracts the article title from the RSS JSON object
                try:
                    title = str(rss_json['title'])
                except:
                    title = 'None'
                    e = sys.exc_info()
                    print('title error\n' + str(e))
                if debug is True:
                    print('title: ' + title)

                # this block looks for a story summary embedded within the RSS JSON object
                try:
                    if name == 'The New York Times (USA)':
                        summary_dict = rss_json['content'][0]
                        summary = str(summary_dict['value'])
                    else:
                        summary = str(rss_json['summary'])
                except:
                    summary = 'None'
                    e = sys.exc_info()
                    print('summary error\n' + str(e))
                if debug is True:
                    print('summary: ' + summary)
                    print('\n')

                # saves each variable to the database using DB-API's parameter substitution, where '?' is a stand-in
                # for a tuple element containing the actual values
                c.execute('INSERT INTO rss VALUES (?,?,?,?,?,?)',
                          (name, published, imported, title, summary, url))
                # commits the changes to the database
                try:
                    conn.commit()
                except sqlite3.Error as e:
                    print('database commit error\n' + str(e))

            else:
                if debug is True:
                    print('------------------------------------------\n'
                          'ingested item present in database: passing\n'
                          '------------------------------------------\n')

        if debug is True:
            print('=================================================\n'
                  'all entries pre-processed on %s: continuing to next run\n'
                  % current_time)
