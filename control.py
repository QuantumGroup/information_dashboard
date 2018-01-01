"""
This is the main control script: in a production run, this should be either replaced or updated by the web UI
"""
import os
import time
import argparse

import setup
import twitter_location_collector
import twitter_track_collector
import twitter_follow_collector
import rss_collector

"""
sets up whether the setup script is needed 
"""
setup_required = False

"""
sets up whether whether debug mode is on
"""
debug = True


"""
sets up the error log
"""
error_log = os.path.join('error_log.txt')


"""
sets up files, if necessary
"""
setup = setup.InformationCollectorSetup()
if setup_required is True:
    setup.initiate()


"""
sets up variables for Twitter location collection: this is to be a list of the four corners of a bounded box. Per the 
Twitter docs: A comma-separated list of longitude,latitude pairs specifying a set of bounding boxes to filter Tweets 
by... Each bounding box should be specified as a pair of longitude and latitude pairs, with the southwest corner of the 
bounding box coming first. 
            [  SW,    NW,     NE,    SE,   SW, NW,  NE, SE ]
"""
location = [-122.75, 36.8, -121.75, 37.8, -74, 40, -73, 41]
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

        Twitter IDs can be found at sites such as http://mytwitterid.com
        1.  @business           '34713362'          Bloomberg
        2.  @cnnbrk             '428333'            CNN Breaking News
        3.  @cbstopnews         '18767649'          CBS Top News
        4.  @wsjbreakingnews    '23484039'          WSJ Breaking News
        5.  @ftcommodities      '346569891'         FT Commodities
        6.  @bncommodities      '804556370'         BN Commodities
        7.  @reuterescommods    '81075524'          Reuters Commodities
        8.  @AP                 '51241574'          AP
        9.  @conflicts          '2566535282'        Conflict News
        10. @afp                '380648579'         AFP News Agency
        11. @bnonews            '189305014'         BNO News
        12. @SkyNewsBreak       '87416722'          Sky News Newsdesk
        13. @USGSBigQuakes      '94119095'          USGS Big Quakes         USGS earthquake alerts
        14. @CNBCnow            '26574283'          CNBC Now
        15. @AJENews            '18424289'          Al Jazeera News
        16. @UPI                '16666806'          UPI.com
        17. @BBCBreaking        '5402612'           BBC Breaking News
        18. @FEWSNET            '80797182'          FEWS NET                Famine Early Warning Systems Network
        19. @ECDC_Outbreaks     '2754484003'        ECDC Outbreaks          EU Centre for Disease Prevention & Control
        20. @nytimesworld       '1877831'           New York Times World
        21. @TheWarMonitor      '1952855342'        WarMonitor
        23. @StratSentinal      '789303014192402432'Strategic Sentinel      
        22. @Strat2Intel        '4048091663'        Strat 2 Intel           Intelligence arm of Strategic Sentinel LLC

        
        deleted sources                         reason
            @markets                            messages are retweeted by @business
            @reuters                            messages are repeated multiple times daily
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

# """
# runs the Twitter Location Collector
# """
# twitter_location = twitter_location_collector.TwitterLocationCollector(location, error_log, debug)
# twitter_location.twitter_location_ingestor(location, error_log, debug)
# """
# runs the Twitter Track Collector
# """
# twitter_track = twitter_track_collector.TwitterTrackCollector(keywords, error_log, debug)
# twitter_track.twitter_track_ingestor(keywords, error_log, debug)
# """
# runs the Twitter Follow Collector
# """
# twitter_follow = twitter_follow_collector.TwitterFollowCollector(accounts, error_log, debug)
# twitter_follow.twitter_follow_ingestor(accounts, error_log, debug)
"""
runs the RSS Collector
"""
e_tags = {}
last_modifieds = {}

rss = rss_collector.RSS_Collector(rss_urls, error_log, debug, e_tags, last_modifieds)
while True:
    for url in rss_urls:
        rss.rss_parser(url, error_log, debug, e_tags, last_modifieds)
    print(e_tags)
    print(last_modifieds)
    time.sleep(300)

