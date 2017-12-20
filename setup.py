"""
This class sets up the required files, databases, and other things needed for the scripts to run properly.
"""


class InformationCollectorSetup:

    def __init__(self):
        # todo: create flag that checks if setup has been run and skips process if True
        pass

    def database_setup(self):
        import sqlite3
        import os

        database = os.path.join('collector.sqlite3')

        conn = sqlite3.connect(database)
        c = conn.cursor()

        # this creates the table that takes in data from the tweet_parser
        table_tweets = 'CREATE TABLE IF NOT EXISTS tweets (id_str INTEGER,name TEXT, screename TEXT, ' \
                       'timestamp REAL, tweet TEXT, coordinates_long REAL, coordinate_lat REAL,  ' \
                       'place_sw_point_long REAL, place_sw_point_lat REAL, place_nw_point_long REAL, ' \
                       'place_nw_point_lat REAL, place_ne_point_long REAL, place_ne_point_lat REAL, ' \
                       'place_se_point_long REAL, place_se_point_lat REAL)'
        c.execute(table_tweets)

        # this creates the table that takes in data from the rss_feed_parser
        table_rss = 'CREATE TABLE IF NOT EXISTS rss (uid INTEGER, organization TEXT, published REAL, title TEXT, ' \
                    'summary TEXT, content TEXT)'
        c.execute(table_rss)

        c.close()
