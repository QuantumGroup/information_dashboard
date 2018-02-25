"""
This class downloads stock market data in batches.
"""
# Python library imports
import sqlite3
import sys
import datetime
import os
import time
import requests
import pandas
import traceback
from io import StringIO
# local file imports
import error as error_class
import _keys_and_secrets


class StockCollector:

    def __init__(self, debug=True):
        self.debug = True

    def stock_ingestor(self, input_symbol):

        # this code instantiates the error class
        error = error_class.Error()

        # this code block loads the database instance
        sqlite_relative_path = os.path.join('real-time_information.sqlite3')
        sqlite_absolute_path = os.path.abspath(sqlite_relative_path)
        conn = sqlite3.connect(sqlite_absolute_path)
        c = conn.cursor()

        # this code block sets all of the Alpha Vantage API variables
        api_url = 'https://www.alphavantage.co/query'
        api_function = 'TIME_SERIES_INTRADAY'
        symbol = input_symbol
        interval = '1min'
        output_size = 'compact'
        datatype = 'csv'
        api_key = _keys_and_secrets.alphavantage_api_key

        data = {'function': api_function,
                'symbol': symbol,
                'interval': interval,
                'output': output_size,
                'datatype': datatype,
                'apikey': api_key
                }

        try:
            stocks_raw = requests.get(api_url, params=data)
            stocks_str = stocks_raw.text
            stocks_df = pandas.read_csv(StringIO(stocks_str))
            stocks_last20_df = stocks_df.iloc[:20]
        except KeyError:
            return
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'stock_ingestor', 'Alpha Vantage API call')
            stocks_raw.close()
            return

        if self.debug is True:
            current_time_int = int(time.time())
            current_time_struct = time.gmtime(current_time_int)
            current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
            print('------------------------------------------------------------------------------------------------\n'
                  'batch ingested from stock market feed on %s UTC: comparing entries to database\n'
                  '------------------------------------------------------------------------------------------------\n'
                  % current_time)

        # this block compares the current row (1 minute worth) of stock market data with data already imported to
        # the database
        c.execute('SELECT published FROM stock_markets WHERE symbol IS (?)', (input_symbol,))
        published_in_database = c.fetchall()
        for index, row in stocks_last20_df.iterrows():
            try:
                published_raw = row['timestamp']
            except:
                e = sys.exc_info()
                full_e = traceback.format_exc()
                error.if_error(str(e), full_e, 'stock_ingestor', 'timestamp creation')
                return

            # if the row is not already in the database, proceeds
            if published_raw not in str(published_in_database):
                print('----------------------------------------------------\n'
                      'row %s not in database: proceeding\n'
                      '----------------------------------------------------\n'
                      % row['timestamp'])

                # this block returns the date and time when the row was imported
                try:
                    imported_int = int(time.time())
                    imported_struct = time.gmtime(imported_int)
                    imported = str(datetime.datetime.fromtimestamp(time.mktime(imported_struct)))
                    if self.debug is True:
                        print('imported: ' + imported)
                except:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'stock_ingestor()', 'imported time')

                # this block returns the name of the index being imported
                try:
                    if input_symbol == 'SPX':
                        name = 'S&P 500 INDEX'
                    if input_symbol == 'DJI':
                        name = 'DOW JONES INDUS. AVG'
                    if input_symbol == 'RUT':
                        name = 'RUSSELL 2000 INDEX'
                    if input_symbol == 'BURCAP':
                        name = 'ARGENTINA BURCAP INDEX'
                    if input_symbol == 'UKX':
                        name = 'FTSE 100 INDEX'
                    if input_symbol == 'SX5E':
                        name = 'Euro Stoxx 50'
                    if input_symbol == 'SENSEX':
                        name = 'S&P BSE SENSEX INDEX'

                    if self.debug is True:
                        print('name: ' + name)
                except:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'stock_ingestor()', 'stock index name')

                # this block returns the country that the stock index nominally tracks or belongs to
                try:
                    if input_symbol == 'SPX' or input_symbol == 'DJI' or input_symbol == 'RUT':
                        country = 'USA'
                    elif input_symbol == 'BURCAP':
                        country = 'ARG'
                    elif input_symbol == 'UKX':
                        country = 'GBR'
                    elif input_symbol == 'SX5E':
                        country = 'EUR'
                    elif input_symbol == 'SENSEX':
                        country = 'IND'
                    if self.debug is True:
                        print('country: ' + country)
                except:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'stock_ingestor()', 'stock index country')

                # this block returns the timestamp data returned from the market index API itself
                try:
                    published = row['timestamp']
                    if self.debug is True:
                        print('published: ' + published)
                except:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'stock_ingestor()', 'timestamp creation')

                # this block returns the market pricing data returned from the market index API itself
                try:
                    stock_open = row['open']
                    stock_high = row['high']
                    stock_low = row['low']
                    stock_close = row['close']
                    if self.debug is True:
                        print('open: %s\n'
                              'high: %s\n'
                              'low: %s\n'
                              'close: %s\n'
                              % (stock_open, stock_high, stock_low, stock_close))
                except:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'stock_ingestor()', 'stock index price data')

                # saves each variable to the database using DB-API's parameter substitution, where '?' is a stand-in
                # for a tuple element containing the actual values
                c.execute('INSERT INTO stock_markets VALUES (?,?,?,?,?,?,?,?,?)',
                          (name, symbol, country, published, imported, stock_open, stock_high, stock_low, stock_close))
                try:
                    conn.commit()
                except:
                    e = sys.exc_info()
                    full_e = traceback.format_exc()
                    error.if_error(str(e), full_e, 'stock_ingestor()', 'committing stock information to database')
                    return

            else:
                if self.debug is True:
                    print('--------------------------------------------\n'
                          'ingested item present in database: passing\n'
                          '--------------------------------------------\n')
        if self.debug is True:
            print('---------------------------------------------------------------\n'
                  'all entries for %s pre-processed on %s UTC\n'
                  '---------------------------------------------------------------\n'
                  % (input_symbol, current_time))
