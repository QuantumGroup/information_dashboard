"""
This is the main control script.
"""

# Python library imports
import os
import time
import datetime
import sys
import traceback
# local file imports
from setup.setup import InformationCollectorSetup
from collection.real_time_collectors import twitter_location_collector, twitter_follow_collector, \
    twitter_track_collector
import collection.batch_collectors.headline_collector as rss_collector
import collection.batch_collectors.stock_collector as stock_collector
import collection.batch_collectors.currency_collector as currency_collector
import collection.batch_collectors.market_sector_collector as market_sector_collector
import error as error_class
import argparse
import startup_configs as configs

"""
instantiates the error class
"""
error = error_class.Error()

# saves HTML ETags and last-modified headers in a persistent variable to be referenced when pulling data from websites
# todo: is this ever used?
e_tags = {}
last_modifieds = {}


def run_collectors(debug, rss_urls, stock_markets, rss, stocks, currencies, market_sectors):
    # this runs all of the collectors in perpetuity
    try:
        while True:
            # this runs the batch collectors
            if debug is True:
                print('===================================================================================\n'
                      'headline collection starting\n'
                      '===================================================================================\n')
            for url in rss_urls:
                rss.rss_parser(url)
            if debug is True:
                print('========================================================================================\n'
                      'all headline entries pre-processed: continuing to next collector...\n'
                      '========================================================================================\n')

            # this runs the Market Sector Collector
            if debug is True:
                print('================================================================================\n'
                      'market sector collection starting\n'
                      '================================================================================\n')
            market_sectors.market_sector_ingestor()
            if debug is True:
                print('==============================================================================================\n'
                      'all market sector entries pre-processed: continuing to next collector...\n'
                      '==============================================================================================\n')

            # this runs the Stock Collector
            if debug is True:
                print('===================================================================================\n'
                      'stock market collection starting\n'
                      '===================================================================================\n')
            for stock_market in stock_markets:
                stocks.stock_ingestor(stock_market)
            if debug is True:
                print(
                    '===============================================================================================\n'
                    'all stock index entries pre-processed: continuing to next collector...\n'
                    '===============================================================================================\n')

            # this runs the Currency Collector
            if debug is True:
                print('================================================================================\n'
                      'currency collection starting\n'
                      '================================================================================\n')
            currencies.currency_ingestor()
            if debug is True:
                print('==============================================================================================\n'
                      'all currency index entries pre-processed: continuing to next run...\n'
                      '==============================================================================================\n')
    except (KeyboardInterrupt, SystemExit):
        os._exit(1)
    except:
        e = sys.exc_info()
        full_e = traceback.format_exc()
        error.if_error(str(e), full_e, 'control', 'FLASH FAILURE')
        try:
            os.execv(sys.executable, ['python3'] + sys.argv)
        except:
            e = sys.exc_info()
            full_e = traceback.format_exc()
            error.if_error(str(e), full_e, 'control', 'CRITIC FAILURE', sms=True)


# todo: tweets are not able to be ingested at this time: investigate
# todo: replace current Twitter collection scrips with more generic sample firehose-like API calls
def init_social_media(accounts, location, keywords):
    """
    runs the Twitter Follow Collector
    """
    twitter_follow = twitter_follow_collector.TwitterFollowCollector(accounts)
    twitter_follow.twitter_follow_ingestor(accounts)
    """
    runs the Twitter Location Collector
    """
    twitter_location = twitter_location_collector.TwitterLocationCollector(location)
    twitter_location.twitter_location_ingestor(location)
    """
    runs the Twitter Track Collector
    """
    twitter_track = twitter_track_collector.TwitterTrackCollector(keywords)
    twitter_track.twitter_track_ingestor(keywords)
    return


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", help="Sets debug mode (debug console output)")
    parser.add_argument("--social", help="Turn on social network collection")
    parsed_args = parser.parse_args()
    print(parsed_args.debug)
    """
    sets up files necessary files
    """
    setup = InformationCollectorSetup()
    setup.initiate()

    if parsed_args.social is not None:
        init_social_media(configs.accounts, configs.location, configs.keywords)

    """
    runs the batch collectors
    """
    # instantiates the batch collector classes
    rss = rss_collector.RSS_Collector()
    stocks = stock_collector.StockCollector()
    currencies = currency_collector.CurrencyCollector()
    market_sectors = market_sector_collector.MarketSectorCollector()

    # prints upon starting the script, whether in debug mode or not
    current_time_int = int(time.time())
    current_time_struct = time.gmtime(current_time_int)
    current_time = str(datetime.datetime.fromtimestamp(time.mktime(current_time_struct)))
    print('\n'
          '=======================================================\n'
          'starting the Global Real-time Information Dashboard\n'
          'release-0.0.1 2018-02-19 running at %s\n'
          '=======================================================\n'
          % current_time)

    run_collectors(parsed_args.debug, configs.rss_urls, configs.stock_markets,
                   rss, stocks, currencies, market_sectors)
    return


if __name__ == "__main__":
    main(sys.argv[1:])
