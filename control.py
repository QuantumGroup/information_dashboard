"""
This is the main control script: in a production run, this should be replace by the web UI
"""
import os
import time

import setup
import twitter_location_collector
import twitter_track_collector
import twitter_follow_collector
import rss_collector


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
# setup = setup.InformationCollectorSetup()
# setup.database_setup()


"""
sets up variables for Twitter location collection: this is to be a list of the four corners of a bounded box
"""
location = [-98.7006, 29.2641, -98.3542, 29.6081]
"""
sets up the variables for Twitter track collection: this is a list of keywords to be tracked
"""
keywords = ['international relations', 'political science', 'international affairs', 'global affairs']
"""
sets up the variables for Twitter follow collection: this is a list of Twitter user IDs
"""
accounts = ['34713362', '428333', '18767649', '23484039', '346569891', '804556370', '81075524', '51241574',
            '2566535282', '380648579', '189305014', '87416722', '94119095', '26574283', '18424289', '16666806',
            '5402612', '80797182', '2754484003', '1877831', '1952855342', '4048091663', '789303014192402432']
"""
sets up the URLs that contain active RSS feeds 
"""
rss_urls = ['http://www.nytimes.com/services/xml/rss/nyt/World.xml',
            'feed://feeds.washingtonpost.com/rss/world']


# """
# runs the Twitter Location Collector
# """
# twitter_location = twitter_location_collector.TwitterLocationCollector(location, error_log, debug)
# location_collection = twitter_location.twitter_location_ingestor(location, error_log, debug)
# """
# runs the Twitter Track Collector
# """
# twitter_track = twitter_track_collector.TwitterTrackCollector(keywords, error_log, debug)
# track_collector = twitter_track.twitter_track_collector(keywords, error_log, debug)
# """
# runs the Twitter Follow Collector
# """
# twitter_follow = twitter_follow_collector.TwitterFollowCollector(accounts, error_log, debug)
# follow_collector = twitter_follow.twitter_follow_ingestor(accounts, error_log, debug)
"""
runs the RSS Collector
"""
rss = rss_collector.RSS_Collector(rss_urls, error_log, debug)
while True:
    for url in rss_urls:
        rss_collector = rss.rss_parser(url, error_log, debug)
    time.sleep(300)
