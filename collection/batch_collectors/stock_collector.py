"""
This class downloads stock market data in real time.
"""


class StockCollector:

    def __init__(self):
        pass

    def stock_ingestor(self, input_symbol):
        # Python library imports
        import sqlite3
        import sys
        import datetime
        import os
        import time
        import requests
        import pandas
        from io import StringIO
        # local file imports
        import _keys_and_secrets
        import control
        import dissemination.sms_alerts.alerts as sms

        # this code block instantiates the SMS alert feature
        sms_alerts = sms.SMS_alerts()

        # this code block loads the database instance
        sqlite_relative_path = os.path.join('collector.sqlite3')
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
            stocks_last10_df = stocks_df.iloc[:10]
        except:
            e = sys.exc_info()[0]
            print('website request or parsing failed\n' + str(e) + '\n')

        if control.debug is True:
            current_time_int = int(time.time())
            current_time_struct = time.gmtime(current_time_int)
            current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
            print('--------------------------------------------------------------------------------------------\n'
                  'batch ingested from stock market feed on %s: comparing entries to database\n'
                  '--------------------------------------------------------------------------------------------\n'
                  % current_time)

        # this block compares the current row (1 minute worth) of stock market data with data already imported to
        # the database
        c.execute('SELECT published FROM stock_markets WHERE symbol IS (?)', (input_symbol,))
        published_in_database = c.fetchall()
        for index, row in stocks_last10_df.iterrows():
            try:
                published_raw = row['timestamp']
            except KeyError as e:
                message = ("Stock_Collector stock_ingestor()\n"
                           "timestamp failure"
                           "%s" % str(e))
                print(message)
                sms_alerts.critic_sms(message)

            # if the row is not already in the database, proceeds
            if published_raw not in str(published_in_database):
                print('-------------------------------------------------\n'
                      'row %s not in database: proceeding\n'
                      '-------------------------------------------------\n'
                      % row['timestamp'])

                # this block returns the date and time when the row was imported
                try:
                    imported_int = int(time.time())
                    imported_struct = time.gmtime(imported_int)
                    imported = str(datetime.datetime.fromtimestamp(time.mktime(imported_struct)))
                    if control.debug is True:
                        print('imported: ' + imported)
                except:
                    imported = 'None'
                    e = sys.exc_info()
                    print('imported error\n' + str(e))

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

                    if control.debug is True:
                        print('name: ' + name)
                except:
                    e = sys.exc_info()[0]
                    name = 'None'
                    print('name of index failed\n' + str(e) + '\n')

                # this block returns the country that the stock index nominally tracks or belongs to
                if input_symbol == 'SPX' or input_symbol == 'DJI' or input_symbol == 'RUT':
                    country = 'USA'
                elif input_symbol == 'BURCAP':
                    country = 'ARG'
                elif input_symbol == 'UKX':
                    country = 'GBR'
                elif input_symbol == 'SX5E':
                    country = 'EEE'
                elif input_symbol == 'SENSEX':
                    country = 'IND'
                if control.debug is True:
                    print('country: ' + country)

                # this block returns the timestamp data returned from the market index API itself
                try:
                    published = row['timestamp']
                    if control.debug is True:
                        print('published: ' + published)
                except:
                    e = sys.exc_info()[0]
                    print('timestamp data failed' + str(e) + '\n')

                # this block returns the market pricing data returned from the market index API itself
                try:
                    stock_open = row['open']
                    stock_high = row['high']
                    stock_low = row['low']
                    stock_close = row['close']
                    if control.debug is True:
                        print('open: %s\n'
                              'high: %s\n'
                              'low: %s\n'
                              'close: %s\n'
                              % (stock_open, stock_high, stock_low, stock_close))
                except:
                    e = sys.exc_info()[0]
                    print('stock information failed' + str(e) + '\n')

                # saves each variable to the database using DB-API's parameter substitution, where '?' is a stand-in
                # for a tuple element containing the actual values
                c.execute('INSERT INTO stock_markets VALUES (?,?,?,?,?,?,?,?,?)',
                          (name, symbol, country, published, imported, stock_open, stock_high, stock_low, stock_close))
                try:
                    conn.commit()
                except sqlite3.Error as e:
                    print('database commit error\n' + str(e))

            else:
                if control.debug is True:
                    print('------------------------------------------\n'
                          'ingested item present in database: passing\n'
                          '------------------------------------------\n')
        if control.debug is True:
            print('=================================================\n'
                  'all entries for %s pre-processed on %s: continuing to next run\n'
                  % (input_symbol, current_time))
