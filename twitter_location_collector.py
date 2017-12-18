"""
This class takes in the requirements from the control script or web UI and handles the collection and processing of
tweets based off of those requirements.
"""
from tweepy import StreamListener


class TwitterLocationCollector(StreamListener):

    def __init__(self, locations, error_log, debug):
        self.locations = locations
        self.error_log = error_log
        self.debug = debug

    def twitter_ingestor(self, locations, error_log, debug):
        from tweepy import Stream
        from tweepy import OAuthHandler
        # imports auth tokens, keys, and PII
        import _keys_and_secrets as keys

        print('\n'
              'opening connection to Twitter API\n'
              '=================================\n\n'
              '--------------------------------------\n'
              'tracking the following location(s): %s\n'
              '--------------------------------------\n'
              % locations)

        # handles Twitter API authentication
        auth = OAuthHandler(keys.twitter_consumer_key, keys.twitter_consumer_secret)
        auth.set_access_token(keys.twitter_access_token_key, keys.twitter_access_token_secret)
        twitter_stream = Stream(auth, TwitterLocationCollector(locations, error_log, debug))
        twitter_stream.filter(locations=locations, async=True)

    def on_data(self, raw_data):
        import json
        import re
        import sqlite3
        import os
        import sys

        sql_database = os.path.join('collector.sqlite3')
        conn = sqlite3.connect(sql_database)
        c = conn.cursor()

        retweets = re.compile(r'^RT|^@')

        raw_data = json.loads(raw_data)
        if retweets.search(str(raw_data['text'])) is None:
            raw_tweet = raw_data
        else:
            return True

        # creates variables for all of the data we wish to save about each tweet
        id_str = raw_tweet['id_str']
        name = raw_tweet['user']['name']
        screenname = raw_tweet['user']['screen_name']
        timestamp = raw_tweet['created_at']
        tweet = raw_tweet['text']
        # from the Twitter docs: "the coordinates object is only present (non-null) when the Tweet is assigned an
        # exact location. If an exact location is provided, the coordinates object will provide a [long, lat] array
        # with the geographical coordinates
        coordinates = str(raw_tweet['coordinates'])
        if coordinates != 'None':
            twitter_generated_coordinates = raw_tweet['coordinates']['coordinates']
            coordinates_list = twitter_generated_coordinates

            coordinates_long = str(coordinates_list[0])

            coordinates_lat = str(coordinates_list[1])
        else:
            coordinates_long = 'None'
            coordinates_lat = 'None'
        # from Twitter docs: "Places are specific, named locations with corresponding geo coordinates. When users
        # decide to assign a location to their Tweet, they are presented with a list of candidate Twitter Places....
        # Tweets associated with Places are not necessarily issued from that location but could also potentially be
        # about that location."
        place = str(raw_tweet['place'])
        if place != 'None':
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
            place_sw_point_long = 'None'
            place_sw_point_lat = 'None'

            place_nw_point_long = 'None'
            place_nw_point_lat = 'None'

            place_ne_point_long = 'None'
            place_ne_point_lat = 'None'

            place_se_point_long = 'None'
            place_se_point_lat = 'None'

        # prints each variable to console for debugging purposes
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
        # commits changes to the database, stopping the process if the database export fails
        try:
            conn.commit()
        except sqlite3.Error as e:
            print(e)
            sys.exit(1)

        return True
