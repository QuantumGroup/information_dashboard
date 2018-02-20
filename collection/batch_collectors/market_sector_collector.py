"""
This class imports stock data by market sector as batch inputs
"""

class MarketSectorCollector:

    def __init__(self):
        pass

    def market_sector_ingestor(self):
        # Python library imports
        import sqlite3
        import sys
        import datetime
        import os
        import time
        import requests
        import traceback
        import dateutil.parser
        # local file imports
        import error as error_class
        import _keys_and_secrets
        import control

        # this instantiates the error class
        error = error_class.Error()

        # this loads the database instance
        sqlite_relative_path = os.path.join('real-time_information.sqlite3')
        sqlite_absolute_path = os.path.abspath(sqlite_relative_path)
        conn = sqlite3.connect(sqlite_absolute_path)
        c = conn.cursor()

        # this code block sets all of the static Alpha Vantage API variables
        api_url = 'https://www.alphavantage.co/query'
        api_function = 'SECTOR'
        api_key = _keys_and_secrets.alphavantage_api_key

        if control.debug is True:
            current_time_int = int(time.time())
            current_time_struct = time.gmtime(current_time_int)
            current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
            print('---------------------------------------------------------------------------------\n'
                  'market sector ingestor initiated on %s UTC\n'
                  '---------------------------------------------------------------------------------\n'
                  % current_time)

        data = {'function': api_function,
                'apikey': api_key
                }

        try:
            sector_raw = requests.get(api_url, params=data)
            sector_json = sector_raw.json()
            sector_parsed = sector_json['Rank A: Real-Time Performance']
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            sector_raw.close()
            error.if_error(str(e), full_e, 'market_sector_ingestor()', 'Alpha Vantage API call')
            return

        try:
            energy = sector_parsed['Energy'][:-1]
            real_estate = sector_parsed['Real Estate'][:-1]
            utilities = sector_parsed['Utilities'][:-1]
            consumer_discretionary = sector_parsed['Consumer Discretionary'][:-1]
            information_technology = sector_parsed['Information Technology'][:-1]
            industrials = sector_parsed['Industrials'][:-1]
            financials = sector_parsed['Financials'][:-1]
            materials = sector_parsed['Materials'][:-1]
            consumer_staples = sector_parsed['Consumer Staples'][:-1]
            health_care = sector_parsed['Health Care'][:-1]
            telecom_services = sector_parsed['Telecommunication Services'][:-1]
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            sector_raw.close()
            error.if_error(str(e), full_e, 'market_sector_ingestor()', 'market variable saving call')

        if control.debug is True:
            print('energy: %s\n'
                  'real estate: %s\n'
                  'utilities: %s\n'
                  'consumer discretionary: %s\n'
                  'information technology: %s\n'
                  'industrials: %s\n'
                  'financials: %s\n'
                  'materials: %s\n'
                  'consumer staples: %s\n'
                  'health care: %s\n'
                  'telecommunication services: %s\n'
                  % (energy, real_estate, utilities, consumer_discretionary, information_technology,
                     industrials, financials, materials, consumer_staples, health_care, telecom_services))

        try:
            published_raw = sector_json['Meta Data']['Last Refreshed']
            published = dateutil.parser.parse(published_raw)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'market_sector_ingestor()', 'published time')

        # this block returns the date and time when the row was imported
        try:
            imported_int = int(time.time())
            imported_struct = time.gmtime(imported_int)
            imported = str(datetime.datetime.fromtimestamp(time.mktime(imported_struct)))
            if control.debug is True:
                print('imported: ' + imported)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'market_sector_ingestor()', 'imported time')

        c.execute('INSERT INTO market_sectors VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                  (energy, real_estate, utilities, consumer_discretionary, information_technology, industrials,
                   financials, materials, consumer_staples, health_care, telecom_services, published, imported))

        try:
            conn.commit()
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'market_sector_ingestor()', 'database commit')
            return
