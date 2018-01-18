"""
This class takes in a list of RSS feeds, downloads their data, parses that data, and saves that
data to the database.
"""


class RSS_Collector:

    def __init__(self, rss_url, error_log, debug, e_tags, last_modifieds):
        self.rss_url = rss_url
        self.error_log = error_log
        self.debug = debug
        self.e_tag = e_tags
        self.last_modifieds = last_modifieds

    def rss_ingestor(self, rss_url, error_log, debug, e_tags, last_modifieds):
        # Python library imports
        import feedparser
        import sys
        import control
        import traceback
        # local file imports
        import error as error_class

        # instantiates the error class
        error = error_class.error()

        try:
            if rss_url in control.e_tags:
                e_tag = control.e_tags[rss_url]
                parser = feedparser.parse(rss_url, etag=e_tag)
                control.e_tags[rss_url] = parser.etag

            elif rss_url in control.last_modifieds:
                last_modified = control.last_modifieds[rss_url]
                parser = feedparser.parse(rss_url, modified=last_modified)
                control.last_modifieds[rss_url] = parser.modified

            else:
                parser = feedparser.parse(rss_url)
                try:
                    control.e_tags[rss_url] = parser.etag
                except:
                    pass
                try:
                    control.last_modifieds[rss_url] = parser.modified
                except:
                    pass

        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'rss_ingestor()', 'feedparser failure')

        return parser

    def rss_parser(self, rss_url, error_log, debug, e_tags, last_modifieds):
        # Python library imports
        import os
        import json
        import sys
        import sqlite3
        import re
        import datetime
        import time
        import traceback
        from urllib.parse import urlparse
        # local file imports
        import control
        import error as error_class

        # instantiates error class
        error = error_class.error()

        if control.debug is True:
            print('----------------------\n'
                  'starting RSS Collector\n'
                  '----------------------\n\n')

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
            print('--------------------------------------------------------------------------------------\n'
                  'batch ingested from the RSS feed on %s: comparing entries to database\n'
                  '--------------------------------------------------------------------------------------\n'
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
                    name = 'The New York Times'
                elif hostname_url == 'www.washingtonpost.com':
                    name = 'The Washington Post'
                elif hostname_url == 'smh.com.au':
                    name = 'The Sydney Morning Herald'
                elif hostname_url == 'www.thedailystar.net':
                    name = 'The Daily Star'
                elif hostname_url == 'timesofindia.indiatimes.com':
                    name = 'The Times of India'
                elif hostname_url == 'www.thehindu.com':
                    name = 'The Hindu'
                elif hostname_url == 'www.haaretz.com':
                    name = 'Haaretz'
                elif hostname_url == 'www.nation.co.ke':
                    name = 'The Nation'
                elif hostname_url == 'app.yonhapnews.co.kr':
                    name = 'Yonhap'
                elif hostname_url == 'www.straitstimes.com':
                    name = 'The Straits Times'
                elif hostname_url == 'www.taipeitimes.com':
                    name = 'The Taipei Times'
                elif hostname_url == 'www.bbc.co.uk':
                    name = 'The BBC'
                elif hostname_url == 'www.csmonitor.com':
                    name = 'The Christian Science Monitor'
                elif hostname_url == 'www.wsj.com':
                    name = 'The Wall Street Journal'
                elif hostname_url == 'hosted2.ap.org':
                    name = 'AP'
                elif hostname_url == 'feeds.reuters.com':
                    name = 'Reuters'
                elif hostname_url == 'www.latimes.com':
                    name = 'The Los Angeles Times'
                else:
                    name = str(hostname_url[4:-4])
            except:
                e = sys.exc_info()
                full_e = traceback.format_exc()
                error.if_error(str(e), full_e, 'rss_parser()', 'URL or name error')
                return

            # this code block adds the nationality of origin for each of these news services
            if hostname_url == 'www.nytimes.com':
                country = 'USA'
            elif hostname_url == 'www.washingtonpost.com':
                country = 'USA'
            elif hostname_url == 'smh.com.au':
                country = 'AUS'
            elif hostname_url == 'www.thedailystar.net':
                country = 'IND'
            elif hostname_url == 'timesofindia.indiatimes.com':
                country = 'IND'
            elif hostname_url == 'www.thehindu.com':
                country = 'IND'
            elif hostname_url == 'www.haaretz.com':
                country = 'ISR'
            elif hostname_url == 'www.nation.co.ke':
                country = 'KEN'
            elif hostname_url == 'app.yonhapnews.co.kr':
                country = 'KOR'
            elif hostname_url == 'www.straitstimes.com':
                country = 'SGP'
            elif hostname_url == 'www.taipeitimes.com':
                country = 'TWN'
            elif hostname_url == 'www.bbc.co.uk':
                country = 'GBR'
            elif hostname_url == 'www.csmonitor.com':
                country = 'USA'
            elif hostname_url == 'www.wsj.com':
                country = 'USA'
            elif hostname_url == 'hosted2.ap.org':
                country = 'USA'
            elif hostname_url == 'feeds.reuters.com':
                country = 'GBR'
            elif hostname_url == 'www.latimes.com':
                country = 'USA'

            # this block checks the database to see if the URL in the new article matches any URLs already captured: if
            # not a match, the script continues the pre-processing and downloading process; if yes a match, pass
            c.execute('SELECT url FROM rss')
            urls = c.fetchall()
            if url not in str(urls):
                if debug is True:
                    print('name: ' + name)

                # This block extracts the time published from the RSS JSON object, or the date from the website URL.
                try:
                    if name == 'The New York Times' or name == 'The Times of India' or name == 'The BBC':
                        # These have a published value in the JSON object: "Wed, 27 Dec 2017 13:08:10 GMT"
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%a, %d %b %Y %H:%M:%S %Z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Sydney Morning Herald':
                        # These have a published value in the JSON object: "Wed Dec 27 15:11:22 UTC 2017"
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%a %b %d %H:%M:%S %Z %Y')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Daily Star' or name == 'The Hindu' or name == 'Haaretz' or \
                            name == 'The Straits Times' or name == 'Reuters':
                        # These have a published value in the JSON object: "Wed, 27 Dec 2017 00:00:00 +0600"
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%a, %d %b %Y %H:%M:%S %z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Nation':
                        # These have a published value in the JSON object: 2017-12-27T14:38:54Z
                        published_raw = str(rss_json['updated'])
                        published_stripped = published_raw[:-1]
                        published_struct = time.strptime(published_stripped, '%Y-%m-%dT%H:%M:%S')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'Yonhap':
                        # These have a published value in the JSON object: 20171227145701
                        published_raw = str(rss_json['published'])
                        published_struct = time.strptime(published_raw, '%Y%m%d%H%M%S')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Taipei Times' or name == 'AP':
                        # these have a published value in the JSON object: 2017-12-28T08:00:00+08:00
                        if name == 'The Taipei Times':
                            published_raw = str(rss_json['updated'])
                        elif name == 'AP':
                            published_raw = str(rss_json['published'])
                        # since Python time objects don't support colons in the middle of UTC offsets, this will strip
                        # out the last three chars in the string and replace them with two (2) zeros (0s), so as to
                        # complete the full offset as understood by the datetime library's %z directive
                        published_stripped = published_raw[:-3]
                        published_assembled = published_stripped + '00'
                        published_struct = time.strptime(published_assembled, '%Y-%m-%dT%H:%M:%S%z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Wall Street Journal' or name == 'The Los Angeles Times':
                        # these have a published value in the JSON object: Wed, 27 Dec 2017 03:00:00 PST
                        published_raw = str(rss_json['published'])
                        if name == 'The Wall Street Journal':
                            published_stripped = published_raw[:-3]
                            published_assembled = published_stripped + '-0500'
                        elif name == 'The Los Angeles Times':
                            published_stripped = published_raw[:-3]
                            published_assembled = published_stripped + '-0800'
                        published_struct = time.strptime(published_assembled, '%a, %d %b %Y %H:%M:%S %z')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
                    elif name == 'The Washington Post' or name == 'The Christian Science Monitor':
                        # These contain the date but not the time the article is published in the URL; therefore,
                        # we will use only the date
                        # ---------------------------
                        # The following regular expression strips dates from URLs, and the line after that converts that
                        # regex object to a Python date object
                        # todo: issue with regex where if year in headline, regex fails to parse date (<class 'ValueError'>, ValueError("time data '-2017-has-' does not match format '/%Y/%m/%d/'",)
                        url_date_regex = re.search(
                            r'([./\-_]{0,1}(19|20)\d{2})[./\-_]{0,1}(([0-3]{0,1}[0-9][./\-_])|'
                            r'(\w{3,5}[./\-_]))([0-3]{0,1}[0-9][./\-]{0,1})?', str_url)
                        if name == 'The Washington Post':
                            url_date = time.strptime(str(url_date_regex.group(0)), '/%Y/%m/%d/')
                        elif name == 'The Christian Science Monitor':
                            url_date = time.strptime(str(url_date_regex.group(0)), '/%Y/%m%d/')
                        published = str(datetime.datetime.fromtimestamp(time.mktime(url_date)))
                except:
                    published = 'None'
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'rss_parser()', 'published error')
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
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'rss_parser()', 'imported error')
                if debug is True:
                    print('imported: ' + imported)

                # This block extracts the article title from the RSS JSON object
                try:
                    title = str(rss_json['title'])
                except:
                    title = 'None'
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'rss_parser()', 'title error')
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
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'rss_parser()', 'summary error')
                if debug is True:
                    print('summary: ' + summary)
                    print('\n')

                # saves each variable to the database using DB-API's parameter substitution, where '?' is a stand-in
                # for a tuple element containing the actual values
                c.execute('INSERT INTO rss VALUES (?,?,?,?,?,?,?)',
                          (name, country, published, imported, title, summary, url))
                # commits the changes to the database
                try:
                    conn.commit()
                except sqlite3.Error as e:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'rss_parser()', 'database commit error')
            else:
                if debug is True:
                    print('------------------------------------------\n'
                          'ingested item present in database: passing\n'
                          '------------------------------------------\n')

        if debug is True:
            # raw_url = urlparse(rss_url)
            # base_url = raw_url.hostname
            print('----------------------------------------------\n'
                  'all entries for %s pre-processed on %s\n'
                  '----------------------------------------------\n'
                  % (urlparse(rss_url).hostname, current_time))
