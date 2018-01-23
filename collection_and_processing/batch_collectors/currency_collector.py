"""
This class imports global currency data in batches.
"""


class CurrencyCollector:

    def __init__(self):
        pass

    def currency_ingestor(self):
        # Python library imports
        import sqlite3
        import sys
        import datetime
        import os
        import time
        import requests
        import traceback
        # local file imports
        import error as error_class
        import _keys_and_secrets
        import control

        # this instantiates the error class
        error = error_class.Error()

        # this loads the database instance
        sqlite_relative_path = os.path.join('collector.sqlite3')
        sqlite_absolute_path = os.path.abspath(sqlite_relative_path)
        conn = sqlite3.connect(sqlite_absolute_path)
        c = conn.cursor()

        """
        Currencies are quoted by comparing a base currency to a counter currency. For example, if we are looking for 
        the value of the Euro relative to the US Dollar, we would look at EUR/USD. If EUR/USD = 1.2500, it means that 
        one Euro is exchanged 1.2500 US Dollars. 
        
        What we will do here, then, is to compare every available currency against the Bank for International 
        Settlements' Triennial Central Bank Survey: Foreign Exchange Turnover in April 2016's top 8 currencies - the 
        majors.
        """

        major_currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY']

        currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNY', 'AED', 'AFN', 'ALL', 'AMD', 'AOA', 'ARS',
                      'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BTN',
                      'BWP', 'BZD', 'CDF', 'CLF', 'CLP', 'COP', 'CRC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DZD',
                      'EGP', 'ERN', 'ETB', 'FJD', 'GEL', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK',
                      'HTG', 'HUF', 'IDR', 'ILS', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'KES', 'KGS', 'KHR',
                      'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LYD', 'MAD', 'MDL',
                      'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MZN', 'NAD', 'NGN', 'NIO',
                      'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD',
                      'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOS', 'SRD', 'STD', 'SVC',
                      'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'UYU',
                      'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XCD', 'XOF', 'XPF', 'YER', 'ZAR', 'ZMW', 'ZWL', 'XAG', 'XAU']

        # this code block sets all of the static Alpha Vantage API variables
        api_url = 'https://www.alphavantage.co/query'
        api_function = 'CURRENCY_EXCHANGE_RATE'

        if control.debug is True:
            current_time_int = int(time.time())
            current_time_struct = time.gmtime(current_time_int)
            current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
            print('------------------------------------------------------------------------------\n'
                  'currency ingestor initiated on %s UTC\n'
                  '------------------------------------------------------------------------------\n'
                  % current_time)

        # this code block sets all of the Alpha Vantage API variables that change depending on what needs to be called
        for currency in currencies:
            for major_currency in major_currencies:
                if currency != major_currencies:
                    from_currency = currency
                    to_currency = major_currency
                    api_key = _keys_and_secrets.alphavantage_api_key

                    data = {'function': api_function,
                            'from_currency': from_currency,
                            'to_currency': to_currency,
                            'apikey': api_key
                            }
                    try:
                        currency_raw = requests.get(api_url, params=data)
                        currency_json = currency_raw.json()
                        currency_parsed = currency_json['Realtime Currency Exchange Rate']
                    except:
                        e = sys.exc_info()
                        full_e = traceback.format_exc()
                        currency_raw.close()
                        error.if_error(str(e), full_e, 'currency_ingestor()', 'Alpha Vantage API call')
                        break

                    try:
                        base_currency_code = currency_parsed['1. From_Currency Code']
                        base_currency_name = currency_parsed['2. From_Currency Name']
                        counter_currency_code = currency_parsed['3. To_Currency Code']
                        counter_currency_name = currency_parsed['4. To_Currency Name']
                        exchange_rate = currency_parsed['5. Exchange Rate']
                        published = currency_parsed['6. Last Refreshed']
                    except:
                        e = sys.exc_info()
                        full_e = traceback.format_exc()
                        error.if_error(str(e), full_e, 'currency_ingestor()', 'currency price data')

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
                        error.if_error(str(e), full_e, 'currency_ingestor()', 'imported time')

                    if control.debug is True:
                        print('base currency code: %s\n'
                              'base currency name: %s\n'
                              'counter currency code: %s\n'
                              'counter currency name: %s\n'
                              'exchange rate: %s\n'
                              'published at: %s\n\n'
                              % (base_currency_code, base_currency_name, counter_currency_code, counter_currency_name,
                                 exchange_rate, published))

                    c.execute('INSERT INTO currencies VALUES (?,?,?,?,?,?,?)',
                              (base_currency_code, base_currency_name, counter_currency_code, counter_currency_name,
                               exchange_rate, published, imported))
                    try:
                        conn.commit()
                    except:
                        e = sys.exc_info()
                        full_e = traceback.format_exc()
                        error.if_error(str(e), full_e, 'currency_ingestor()', 'database commit')
                        return
