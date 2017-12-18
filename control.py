"""
This is the main control script: in a production run, this should be replace by the web UI
"""
import os

import setup
import twitter_location_collector



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
sets up variables for Twitter collection
"""
location = [-98.7006, 29.2641, -98.3542, 29.6081]


"""
runs the Twitter Location Collector
"""
twitter_location = twitter_location_collector.TwitterLocationCollector(location, error_log, debug)
location_collection = twitter_location.twitter_ingestor(location, error_log, debug)
