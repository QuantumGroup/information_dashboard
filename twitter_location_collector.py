"""
This class takes in the geographic location requirements from the control script or web UI and handles the
collection and pre-processing of tweets based off of those requirements.
"""
from tweepy import StreamListener


class TwitterLocationCollector(StreamListener):

    def __init__(self, locations, error_log, debug):
        self.locations = locations
        self.error_log = error_log
        self.debug = debug

    def twitter_location_ingestor(self, locations, error_log, debug):
        from tweepy import Stream
        from tweepy import OAuthHandler
        # imports auth secrets and keys
        import _keys_and_secrets as keys

        print('\n'
              'opening connection to Twitter API\n'
              '=================================\n\n'
              '--------------------------------------\n'
              'tracking the following location(s): %s\n'
              '--------------------------------------\n'
              % locations)

        # handles Twitter API authentication
        auth = OAuthHandler(keys.twitter_consumer_key_1, keys.twitter_consumer_secret_1)
        auth.set_access_token(keys.twitter_access_token_key_1, keys.twitter_access_token_secret_1)
        twitter_stream = Stream(auth, TwitterLocationCollector(locations, error_log, debug))
        twitter_stream.filter(locations=locations, async=True)

    def on_data(self, raw_data):
        import json
        import re
        import sqlite3
        import os
        import sys
        import time
        import calendar
        import random

        # establishes connection to database
        sql_database = os.path.join('collector.sqlite3')
        conn = sqlite3.connect(sql_database)
        c = conn.cursor()

        # creates regex object that looks for standard Twitter retweet format
        retweets = re.compile(r'^RT|^@')

        # loads Twitter data as JSON object
        raw_data = json.loads(raw_data)

        # looks through tweet JSON object for retweet regex, and skips the rest of the script if it finds the
        # retweet pattern
        if retweets.search(str(raw_data['text'])) is None:
            raw_tweet = raw_data
        else:
            return True

        # the following block creates the variables (from the tweet JSON object) that we wish to save
        # in the database

        # this is the 'human-readable' Twitter name
        name = raw_tweet['user']['name']
        # this is the Twitter '@' handle
        screenname = raw_tweet['user']['screen_name']
        # this is the time the tweet was created
        timestamp_raw = raw_tweet['created_at']
        timestamp_struct = time.strptime(timestamp_raw, '%a %b %d %H:%M:%S %z %Y')
        timestamp = time.strftime('%c', timestamp_struct)
        # uses the timestamp to create a unique ID for database purposes: uses time instead of built-in tweet id_str in
        # order to maintain consistency with out aspects of our code. Added benefit is that it minimizex long-term
        # chances of UID collisions, since the only collisions possible are with other articles, tweets, messages, or
        # other objects that are posted at the same second as each other - and even then, the addition of five random
        # digits at the end should minimize this further.
        timestamp_id = str(calendar.timegm(timestamp_struct))
        timestamp_addition = random.sample(range(99999), 1)
        id_str = timestamp_id + str(timestamp_addition[0])
        # this is the actual tweet body, or message
        tweet = raw_tweet['text']
        # from the Twitter docs: "the coordinates object is only present (non-null) when the Tweet is assigned an
        # exact location. If an exact location is provided, the coordinates object will provide a [long, lat] array
        # with the geographical coordinates
        coordinates = str(raw_tweet['coordinates'])
        if coordinates != 'None':
            # if 'coordinates' exist, this retrieves the Python list that contains the coordinates and saves them as
            # individual string objects
            twitter_generated_coordinates = raw_tweet['coordinates']['coordinates']
            coordinates_long = str(twitter_generated_coordinates[0])
            coordinates_lat = str(twitter_generated_coordinates[1])
        else:
            # if 'coordinates' do not exist, sends a 'None' string to the database
            coordinates_long = 'None'
            coordinates_lat = 'None'
        # from Twitter docs: "Places are specific, named locations with corresponding geo coordinates. When users
        # decide to assign a location to their Tweet, they are presented with a list of candidate Twitter Places....
        # Tweets associated with Places are not necessarily issued from that location but could also potentially be
        # about that location."
        place = str(raw_tweet['place'])
        if place != 'None':
            # if 'place' exists, this returns the Python list that contains the coordinates of each corner of the bound
            # box and saves them all as individual strings to send to the database
            user_generated_place = raw_tweet['place']['bounding_box']['coordinates']

            place_sw_point_long = str(user_generated_place[0][0][0])
            place_sw_point_lat = str(user_generated_place[0][0][1])

            place_nw_point_long = str(user_generated_place[0][1][0])
            place_nw_point_lat = str(user_generated_place[0][1][1])

            place_ne_point_long = str(user_generated_place[0][2][0])
            place_ne_point_lat = str(user_generated_place[0][2][1])

            place_se_point_long = str(user_generated_place[0][3][0])
            place_se_point_lat = str(user_generated_place[0][3][1])

        else:
            # if 'place' does not exist, this sends 'None' to the database
            place_sw_point_long = 'None'
            place_sw_point_lat = 'None'

            place_nw_point_long = 'None'
            place_nw_point_lat = 'None'

            place_ne_point_long = 'None'
            place_ne_point_lat = 'None'

            place_se_point_long = 'None'
            place_se_point_lat = 'None'

        # this block prints each variable to console for debugging purposes
        print(id_str + '\n' + name + ' (@' + screenname + ')\n' + timestamp + '\n' + tweet + '\n' + 'coordinates: '
              + coordinates_long + ' ' + coordinates_lat + '\n' + 'place boundary: ' + place_sw_point_long + ' ' +
              place_sw_point_lat + ', ' + place_nw_point_long + ' ' + place_nw_point_lat + ', ' +
              place_ne_point_long + ' ' + place_ne_point_lat + ', ' + place_se_point_long + ' ' +
              place_se_point_lat + '\n---\n')

        # saves each variable to the database uses DB-API's parameter substitution, where ? is a stand-in for a
        # tuple containing the values
        c.execute('INSERT INTO tweets VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (id_str, name, screenname, timestamp, tweet, coordinates_long, coordinates_lat,
                   place_sw_point_long, place_sw_point_lat, place_nw_point_long, place_nw_point_lat,
                   place_ne_point_long, place_ne_point_lat, place_se_point_long, place_se_point_lat))

        # this block commits changes to the database, stopping the process if the database export fails
        try:
            conn.commit()
        except sqlite3.Error as e:
            print(e)
            sys.exit(1)

        return True
