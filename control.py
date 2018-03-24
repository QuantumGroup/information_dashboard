"""
This is the main control script.
"""


# Python library imports
import time
import datetime
# local file imports
import setup.setup as setup
import collection.real_time_collectors.twitter_sample_collector as twitter_collector
import collection.batch_collectors.headline_collector as headline_collector
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
            'feed://www.latimes.com/world/rss2.0.xml',
            'https://reliefweb.int/disasters/rss.xml']

"""
this runs the Twitter collector
"""
twitter = twitter_collector.TwitterSample()
twitter.twitter_sample_ingestor()

"""
runs the headline collector
"""
# saves HTML ETags and last-modified headers in a persistent variable to be referenced when pulling data from websites
e_tags = {}
last_modifieds = {}

# instantiates the batch collector classes
headlines = headline_collector.RSS_Collector()

# prints upon starting the script, whether in debug mode or not
current_time_int = int(time.time())
current_time_struct = time.gmtime(current_time_int)
current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
print('\n'
      '=======================================================\n'
      'starting the Information Edge Tool (working title)\n'
      'release-0.0.1. 2018-03-12 running at %s\n'
      '=======================================================\n'
      % current_time)

# this runs all of the collectors in perpetuity
while True:
    for url in rss_urls:
        headlines.rss_parser(url)
    print('run completed at %d' % int(time.time()))
    time.sleep(60)
