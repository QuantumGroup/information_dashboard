"""
This is the main control script.
"""


# Python library imports
import os
import time
import datetime
import sys
import traceback
# local file imports
import setup.setup as setup
import collection.real_time_collectors.twitter_sample_collector as twitter_collector
import collection.batch_collectors.headline_collector as rss_collector
import collection.batch_collectors.stock_collector as stock_collector
import collection.batch_collectors.currency_collector as currency_collector
import collection.batch_collectors.market_sector_collector as market_sector_collector
import error as error_class


"""
sets up whether whether debug mode is on
"""
debug = True

"""
sets up files necessary files
"""
setup = setup.InformationCollectorSetup()
setup.initiate()

"""
instantiates the error class
"""
error = error_class.Error()

"""
sets up variables for Twitter location collection: this is to be a list of the four corners of a bounded box. Per the 
Twitter docs: A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets 
by... Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the 
bounding box coming first. 
           [  SW,    NW,    NE,    SE, | SW,    NW,    NE,   SE ]
"""
location = [-122.7, 36.8, -121.7, 37.8, -74.0, 40.0, -73.0, 41.0]
"""
sets up the variables for Twitter track collection: this is a list of keywords to be tracked. Per Twitter docs: A comma-
separated list of phrases which will be used to determine what Tweets will be delivered on the stream. A phrase may be 
one or more terms separated by spaces, and a phrase will match if all of the terms in the phrase are present in the 
Tweet, regardless of order and ignoring case. By this model, you can think of commas as logical ORs, while spaces are 
equivalent to logical ANDs (e.g. ‘the twitter’ is the AND twitter, and ‘the,twitter’ is the OR twitter).
"""
keywords = ['international relations', 'political science', 'international affairs', 'global affairs']
"""
sets up the variables for Twitter follow collection: this is a list of Twitter user IDs. Per the Twitter docs: A comma-
separated list of user IDs, indicating the users whose Tweets should be delivered on the stream.

"""
accounts = ['34713362', '428333', '18767649', '23484039', '346569891', '804556370', '81075524', '51241574',
            '2566535282', '380648579', '189305014', '87416722', '94119095', '26574283', '18424289', '16666806',
            '5402612', '80797182', '2754484003', '1877831', '1952855342', '4048091663', '789303014192402432']
"""
sets up the URLs that contain active RSS feeds 
"""
rss_urls = ['http://www.nytimes.com/services/xml/rss/nyt/World.xml',
            'feed://feeds.washingtonpost.com/rss/world',
            'http://www.smh.com.au/rssheadlines/world/article/rss.xml',
            'http://www.thedailystar.net/world/rss.xml',
            'http://www.thehindu.com/news/international/?service=rss',
            'http://timesofindia.indiatimes.com/rssfeeds/296589292.cms',
            'http://www.haaretz.com/cmlink/1.628765',
            'feed://www.haaretz.com/cmlink/1.798067',
            'feed://www.nation.co.ke/news/world/1068-1068-view-asFeed-hmfstbz/index.xml',
            'feed://www.nation.co.ke/news/africa/1066-1066-view-asFeed-15sj5pt/index.xml',
            'feed://english.yonhapnews.co.kr/RSS/headline.xml',
            'feed://english.yonhapnews.co.kr/RSS/northkorea.xml',
            'feed://www.straitstimes.com/news/asia/rss.xml',
            'feed://www.taipeitimes.com/xml/world.rss',
            'http://feeds.bbci.co.uk/news/world/europe/rss.xml',
            'http://feeds.bbci.co.uk/news/world/rss.xml',
            'http://rss.csmonitor.com/feeds/world',
            'feed://www.wsj.com/xml/rss/3_7085.xml'
            'feed://hosted2.ap.org/atom/APDEFAULT/cae69a7523db45408eeb2b3a98c0c9c5',
            'http://feeds.reuters.com/Reuters/worldNews',
            'feed://www.latimes.com/world/rss2.0.xml']

stock_markets = ['DJI',
                 'RUT',
                 'SPX',
                 'BURCAP',
                 'UKX',
                 'SX5E',
                 'SENSEX'
                 ]

twitter = twitter_collector.TwitterSample()
twitter.twitter_sample_ingestor()

"""
runs the batch collectors
"""
# saves HTML ETags and last-modified headers in a persistent variable to be referenced when pulling data from websites
e_tags = {}
last_modifieds = {}

# instantiates the batch collector classes
rss = rss_collector.RSS_Collector()
stocks = stock_collector.StockCollector()
currencies = currency_collector.CurrencyCollector()
market_sectors = market_sector_collector.MarketSectorCollector()

# prints upon starting the script, whether in debug mode or not
current_time_int = int(time.time())
current_time_struct = time.gmtime(current_time_int)
current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
print('\n'
      '=======================================================\n'
      'starting the Global Real-time Information Dashboard\n'
      'release-0.0.1 2018-02-19 running at %s\n'
      '=======================================================\n'
      % current_time)

# this runs all of the collectors in perpetuity
try:
    while True:
        # this runs the batch collectors
        if debug is True:
            print('===================================================================================\n'
                  'headline collection starting\n'
                  '===================================================================================\n')
        for url in rss_urls:
            rss.rss_parser(url)
        if debug is True:
            print('========================================================================================\n'
                  'all headline entries pre-processed: continuing to next collector...\n'
                  '========================================================================================\n')

        # this runs the Market Sector Collector
        if debug is True:
            print('================================================================================\n'
                  'market sector collection starting\n'
                  '================================================================================\n')
        market_sectors.market_sector_ingestor()
        if debug is True:
            print('==============================================================================================\n'
                  'all market sector entries pre-processed: continuing to next collector...\n'
                  '==============================================================================================\n')

        # this runs the Stock Collector
        if debug is True:
            print('===================================================================================\n'
                  'stock market collection starting\n'
                  '===================================================================================\n')
        for stock_market in stock_markets:
            stocks.stock_ingestor(stock_market)
        if debug is True:
            print('===============================================================================================\n'
                  'all stock index entries pre-processed: continuing to next collector...\n'
                  '===============================================================================================\n')

        # this runs the Currency Collector
        if debug is True:
            print('================================================================================\n'
                  'currency collection starting\n'
                  '================================================================================\n')
        currencies.currency_ingestor()
        if debug is True:
            print('==============================================================================================\n'
                  'all currency index entries pre-processed: continuing to next run...\n'
                  '==============================================================================================\n')
except (KeyboardInterrupt, SystemExit):
    os._exit(1)
except:
    e = sys.exc_info()
    full_e = traceback.format_exc()
    error.if_error(str(e), full_e, 'control', 'FLASH FAILURE')
    try:
        os.execv(sys.executable, ['python3'] + sys.argv)
    except:
        e = sys.exc_info()
        full_e = traceback.format_exc()
        error.if_error(str(e), full_e, 'control', 'CRITIC FAILURE', sms=True)
