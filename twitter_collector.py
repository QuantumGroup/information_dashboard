"""
This class takes in the requirements from the control script or web UI and handles the collection and processing of
tweets based off of those requirements.
"""


class TwitterCollector:
    import json
    import os
    import re
    from tweepy import Stream
    from tweepy import OAuthHandler
    from tweepy.streaming import StreamListener
    # imports auth tokens, keys, and PII


    def __init__(self, locations, keywords, accounts, error_log, debug):
        self.locations = locations
        self.keywords = keywords
        self.accounts = accounts
        self.error_log = error_log
        self.debug = debug


    def twitter_ingestor(self, locations, keywords, accounts):
