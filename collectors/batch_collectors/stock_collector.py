"""
This class downloads stock market data in real time.
"""


class StockCollector:

    def __init__(self):
        pass

    def stock_ingestor(self):
        import requests
        import pprint
        import _keys_and_secrets

        api_url = 'https://www.alphavantage.co/query'

        api_function = 'TIME_SERIES_INTRADAY'
        symbol = 'tran'
        interval = '5min'
        output_size = 'compact'
        api_key = _keys_and_secrets.alphavantage_api_key

        data = {'function': api_function,
                'symbol': symbol,
                'interval': interval,
                'apikey': api_key
                }

        info = requests.get(api_url, params=data)

        print(info.url)
        pprint.pprint(info.json())


stocks = StockCollector()
stocks.stock_ingestor()

