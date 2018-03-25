"""
This class takes in the keyword requirements from the control script and handles collection and
pre-processing of those tweets based off of those requirements.
"""

# Python library imports
from tweepy import StreamListener, Stream, OAuthHandler
import json
import re
import sqlite3
import os
import traceback
import time
import datetime
import sys
# local file imports
import error as error_class
import _keys_and_secrets as keys


class TwitterSample(StreamListener):

    def __init__(self):
        super().__init__()
        self.debug = False

    def twitter_sample_ingestor(self):

        # handles Twitter API authentication
        auth = OAuthHandler(keys.twitter_consumer_key_3, keys.twitter_consumer_secret_3)
        auth.set_access_token(keys.twitter_access_token_key_3, keys.twitter_access_token_secret_3)
        twitter_stream = Stream(auth, TwitterSample())
        twitter_stream.sample(async=True)

    def on_data(self, raw_data):

        # instantiates error class
        error = error_class.Error()

        # establishes connection to database
        sql_database = os.path.join('real-time_information.sqlite3')
        conn = sqlite3.connect(sql_database)
        c = conn.cursor()

        # creates regex search that looks for retweets in standard Twitter formats
        retweets = re.compile(r'^RT|^@')

        # loads tweets as JSON objects
        try:
            tweet = json.loads(raw_data)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in loading tweets as JSON objects')

        # searches through tweets and removes them from sample if certain conditions exist
        try:
            # searches tweet to ensure that tweet body exists and is not a Twitter delete notification
            if 'delete' in str(tweet):
                return True
            # searches through tweet for retweet regex and returns if found
            if retweets.search(str(tweet['text'])):
                return True
            # this block parses the selected language of the tweet, returns if not 'en', continues otherwise
            language = tweet['user']['lang']
            if language != 'en':
                return True
            if self.debug is True:
                print('language: ' + language + '\n\n')
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in searching through tweets for removal on conditions')

        try:
            # this block saves the human-readable account name
            name = tweet['user']['name']
            if self.debug is True:
                print('name: ' + name)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in saving human-readable account name')

        try:
            # this block saves the account '@' screenname
            screenname = tweet['user']['screen_name']
            if self.debug is True:
                print('screen name: @' + screenname)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in saving account @ account name')

        try:
            # this block saves the time the tweet was published
            published_raw = tweet['created_at']
            published_struct = time.strptime(published_raw, '%a %b %d %H:%M:%S %z %Y')
            published = str(datetime.datetime.fromtimestamp(time.mktime(published_struct)))
            if self.debug is True:
                print('time: ' + published)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in saving time the tweet was published')

        try:
            # this block saves the actual tweet body text
            text = tweet['text']
            if self.debug is True:
                print('text: ' + text)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in saving tweet body text')

        try:
            # this block saves the exact location of a tweet (when present): if no location is available, ths is null.
            # If not null, this saves a [long, lat] array of the exact coordinates
            coordinates = str(tweet['coordinates'])
            # this checks if the coordinate exist, and saves them if they do, saving a null identifier otherwise
            if coordinates != 'None':
                twitter_generated_coordinates = tweet['coordinates']['coordinates']
                coordinates_long = str(twitter_generated_coordinates[0])
                coordinates_lat = str(twitter_generated_coordinates[1])
            else:
                coordinates_long = 'None'
                coordinates_lat = 'None'
            if self.debug is True:
                print('coordinates: ' + coordinates_long, coordinates_lat)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in saving tweet location data')

        try:
            # this block saves places that are tagged by users in their tweets. Tweets do not necessarily originate
            # from the locations tagged.
            place = str(tweet['place'])
            if place != 'None':
                # this saves the given name of the tagged place
                place_name = tweet['place']['full_name']
                # this saves the type of place
                place_type = tweet['place']['place_type']
                # this saves the country code of the place
                place_country = tweet['place']['country_code']
                # this block saves the coordinates of the bounding box enclosing the place
                place_coordinates = tweet['place']['bounding_box']['coordinates']
                place_sw_point_long = str(place_coordinates[0][0][0])
                place_sw_point_lat = str(place_coordinates[0][0][1])
                place_nw_point_long = str(place_coordinates[0][1][0])
                place_nw_point_lat = str(place_coordinates[0][1][1])
                place_ne_point_long = str(place_coordinates[0][2][0])
                place_ne_point_lat = str(place_coordinates[0][2][1])
                place_se_point_long = str(place_coordinates[0][3][0])
                place_se_point_lat = str(place_coordinates[0][3][1])
            else:
                place_name = 'None'
                place_type = 'None'
                place_country = 'None'
                place_sw_point_long = 'None'
                place_sw_point_lat = 'None'
                place_nw_point_long = 'None'
                place_nw_point_lat = 'None'
                place_ne_point_long = 'None'
                place_ne_point_lat = 'None'
                place_se_point_long = 'None'
                place_se_point_lat = 'None'
            if self.debug is True:
                print('place name: ' + place_name)
                print('place type: ' + place_type)
                print('place country: ' + place_country)
                print('place southwest coordinate: ' + place_sw_point_long, place_sw_point_lat)
                print('place northwest coordinate: ' + place_nw_point_long, place_nw_point_lat)
                print('place northeast coordinate: ' + place_ne_point_long, place_ne_point_lat)
                print('place southeast coordinate: ' + place_se_point_long, place_se_point_lat)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'error in saving tweet place data')

        try:
            # saves each variable to the database uses DB-API's parameter substitution, where ? is a stand-in for a
            # tuple containing the values
            c.execute('INSERT INTO tweets VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
                      (name, screenname, published, text, coordinates_long, coordinates_lat, place_name, place_type,
                       place_country, place_sw_point_long, place_sw_point_lat, place_nw_point_long, place_nw_point_lat,
                       place_ne_point_long, place_ne_point_lat, place_se_point_long, place_se_point_lat,
                       language))
            # this block commits changes to the database, stopping the process if the database export fails
            conn.commit()
        except sqlite3.Error as e:
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'module twitter_sample_collector, class TwitterSample, method on_data',
                           'database commit error')

        return True
