"""
This class sets up the required files, databases, and other things needed for the scripts to run properly.
"""


class InformationCollectorSetup:

    def __init__(self):
        pass

    def initiate(self):
        self.database_setup()
        self.metadata_setup()

    def database_setup(self):
        import sqlite3
        import os

        database = os.path.join('real-time_information.sqlite3')
        conn = sqlite3.connect(database)
        c = conn.cursor()

        # this creates the table that correlates ISO 3166-1 alpha 3 country codes, ISO 3166/MA short country names,
        # ISO 4217 currency codes, and currency names
        table_countries = 'CREATE TABLE IF NOT EXISTS countries (country_code TEXT, country_name TEXT, ' \
                          'currency_code TEXT, currency_name TEXT)'
        c.execute(table_countries)

        # this creates the table that takes in data from the tweet_collector
        table_tweets = 'CREATE TABLE IF NOT EXISTS tweets (name TEXT, screenname TEXT, published TEXT, text_text TEXT, ' \
                       'coordinates_long INTEGER, coordinates_lat INTEGER, place_name TEXT, place_type TEXT, ' \
                       'place_country TEXT, place_sw_point_long INTEGER, place_sw_point_lat INTEGER, ' \
                       'place_nw_point_long INTEGER, place_nw_point_lat INTEGER, place_ne_point_long INTEGER, ' \
                       'place_ne_point_lat INTEGER, place_se_point_long INTEGER, place_se_point_lat INTEGER, lang TEXT)'
        c.execute(table_tweets)

        # this creates the table that takes in data from the rss_collector
        table_rss = 'CREATE TABLE IF NOT EXISTS rss (name TEXT, country TEXT, published TEXT, ' \
                    'imported TEXT, title TEXT, summary TEXT, url TEXT)'
        c.execute(table_rss)

        # this code block creates the table that takes in data from the stock_collector
        table_stock_markets = 'CREATE TABLE IF NOT EXISTS stock_markets (name TEXT, symbol TEXT, country TEXT, ' \
                              'published TEXT, imported TEXT, open REAL, high REAL, low REAL, close REAL)'
        c.execute(table_stock_markets)

        # this code block creates the table that takes in data from the currency_collector
        table_currencies = 'CREATE TABLE IF NOT EXISTS currencies (base_currency_code TEXT, base_currency_name TEXT, ' \
                           'counter_currency_code TEXT, counter_currency_name TEXT, exchange_rate REAL, ' \
                           'published TEXT, imported TEXT)'
        c.execute(table_currencies)

        # these code blocks create the tables that takes in data from the market_sector_collector for one day, three
        # day, one month, three month, and one year performance
        table_one_day_market_sectors = 'CREATE TABLE IF NOT EXISTS one_day_market_sectors (energy REAL, real_estate REAL, ' \
                               'utilities REAL, consumer_discretionary REAL, information_technology REAL, ' \
                               'industrials REAL, financials REAL, materials REAL, consumer_staples REAL, ' \
                               'health_care REAL, telecom_services REAL, published REAL, imported REAL)'
        c.execute(table_one_day_market_sectors)

        table_five_day_market_sectors = 'CREATE TABLE IF NOT EXISTS five_day_market_sectors (energy REAL, real_estate REAL, ' \
                               'utilities REAL, consumer_discretionary REAL, information_technology REAL, ' \
                               'industrials REAL, financials REAL, materials REAL, consumer_staples REAL, ' \
                               'health_care REAL, telecom_services REAL, published REAL, imported REAL)'
        c.execute(table_five_day_market_sectors)

        table_one_month_market_sectors = 'CREATE TABLE IF NOT EXISTS one_month_market_sectors (energy REAL, real_estate REAL, ' \
                               'utilities REAL, consumer_discretionary REAL, information_technology REAL, ' \
                               'industrials REAL, financials REAL, materials REAL, consumer_staples REAL, ' \
                               'health_care REAL, telecom_services REAL, published REAL, imported REAL)'
        c.execute(table_one_month_market_sectors)

        table_three_month_market_sectors = 'CREATE TABLE IF NOT EXISTS three_month_market_sectors (energy REAL, real_estate REAL, ' \
                               'utilities REAL, consumer_discretionary REAL, information_technology REAL, ' \
                               'industrials REAL, financials REAL, materials REAL, consumer_staples REAL, ' \
                               'health_care REAL, telecom_services REAL, published REAL, imported REAL)'
        c.execute(table_three_month_market_sectors)

        table_one_year_market_sectors = 'CREATE TABLE IF NOT EXISTS one_year_market_sectors (energy REAL, real_estate REAL, ' \
                               'utilities REAL, consumer_discretionary REAL, information_technology REAL, ' \
                               'industrials REAL, financials REAL, materials REAL, consumer_staples REAL, ' \
                               'health_care REAL, telecom_services REAL, published REAL, imported REAL)'
        c.execute(table_one_year_market_sectors)

        c.close()

    def metadata_setup(self):
        # Python library imports
        import sqlite3
        import os
        import csv

        # local file imports
        import error as error_class

        # instantiates the error class
        error = error_class.Error()

        # instantiates the database connection
        database = os.path.join('real-time_information.sqlite3')
        conn = sqlite3.connect(database)
        c = conn.cursor()

        # this is the file path to the CSV file that contains the data to be imported
        country_metadata = os.path.join('setup', 'country_meta.csv')

        # this loads the CSV file, parses it, and adds each field of data into the database
        with open(country_metadata, 'rU', encoding='utf-8', errors='ignore') as f:
            reader = csv.reader(f)
            for row in reader:
                currency_code = row[0]
                currency_name = row[1]
                country_code = row[2]
                country_name = row[3]

                # this block compares the current row data with data already imported to the database
                c.execute('SELECT country_code FROM countries WHERE country_code IS (?)', (country_code,))
                published_in_database = c.fetchall()

                if country_code not in str(published_in_database):
                    c.execute('INSERT INTO countries VALUES (?,?,?,?)',
                              (country_code, country_name, currency_code, currency_name))
                    conn.commit()
