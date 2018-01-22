"""
This class sets up the required files, databases, and other things needed for the scripts to run properly.
"""


class InformationCollectorSetup:

    def __init__(self):
        # todo: create flag that checks if setup has been run and skips process if True
        pass

    def initiate(self):
        self.database_setup()

    def database_setup(self):
        import sqlite3
        import os

        database = os.path.join('collector.sqlite3')

        conn = sqlite3.connect(database)
        c = conn.cursor()

        # this creates the table that takes in data from the tweet_collector
        table_tweets = 'CREATE TABLE IF NOT EXISTS tweets (name TEXT, screename TEXT, ' \
                       'published REAL, tweet TEXT, coordinates_long REAL, coordinate_lat REAL,  ' \
                       'place_sw_point_long REAL, place_sw_point_lat REAL, place_nw_point_long REAL, ' \
                       'place_nw_point_lat REAL, place_ne_point_long REAL, place_ne_point_lat REAL, ' \
                       'place_se_point_long REAL, place_se_point_lat REAL, collector TEXT, url REAL)'
        c.execute(table_tweets)

        # this creates the table that takes in data from the rss_collector
        table_rss = 'CREATE TABLE IF NOT EXISTS rss (name TEXT, country TEXT, published REAL, ' \
                    'imported TEXT, title TEXT, summary TEXT, url TEXT)'
        c.execute(table_rss)

        # this code block creates the table that takes in data from the stock_collector
        table_stock_markets = 'CREATE TABLE IF NOT EXISTS stock_markets (name TEXT, symbol TEXT, country TEXT, ' \
                              'published REAL, imported REAL, open REAL, high REAL, low REAL, close REAL)'
        c.execute(table_stock_markets)

        # this code block creates the table that takes in data from the currency_collector
        table_currencies = 'CREATE TABLE IF NOT EXISTS currencies (base_currency_code TEXT, base_currency_name TEXT, ' \
                           'counter_currency_code TEXT, counter_currency_name TEXT, exchange_rate REAL, ' \
                           'published TEXT, imported TEXT)'
        c.execute(table_currencies)

        c.close()
