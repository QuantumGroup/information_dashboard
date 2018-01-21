# Information Collector

## Purpose

The purpose of this project is to provide an at-a-glance view of global events, along with the national and regional information that is required to put that real-time data into context.

This project to be an aggregate of number of disparate information sources, which include the following:

- News organizations
    - These include national papers of record and global news wires.
- Social networks
    - At the moment, this includes only Twitter collectors.
- Financial markets
    - These include stock and stock futures markets, stock markets by industry sectors, commodities markets, currency markets, and fixed income markets.
- Country economic, political, and demographic indicators
    - Economic indicators include national financial markets, GDP statistics, inflation, import and export figures, and other such information.
    - Political indicators include regime type, election information, human development indices and other such information.
    - Demographic indicators include total population and population breakdowns, birth and death rates, GDP per capita, and other such information.
- Natural hazards indicators
    - These will include live weather data, climate predictions, tropical cyclone monitoring, earthquake information, and drought monitoring.
- Health hazard indicators
    - These include infectious disease outbreaks and other related hazards such as famine.
    
All of the components listed are to work together to a common end: to create a dashboard which contains timely, accurate, pre-processed, actionable information.

This is very much a work in progress - stay tuned.

## Components

### Collectors and Processors

A number of collectors will be built for different sources, each with different capabilities. Examples to date include collectors that take in data from the Twitter API and collectors that take in news site RSS feeds live. These collectors will also be in charge of data pre-processing, i.e. converting the data into a machine-readable format.

### Analyzers

Pre-processed data will be run through a number of analyzers, starting with natural language processors that will prepare the data to be further broken down using speech tagging, topic modeling, sentiment analysis, and other machine learning and statistical techniques.

### Disseminators

Finally, the processed and/or analyzed data will need to be disseminated to end users, with options for both machine-readable and human-readable formats. These disseminators will also include additional communications mediums, such as SMS alerts.

### User Interface

A web-based UI will be the main way of updating the collection requirements, as well as one of the ways of viewing the results from the collectors.

## Modules

### collection_and_processing/

This directory contains the collection and pre-processing scripts, divided by temporal type.

#### batch_collectors

- rss_collector.py

This is the collectors that takes in data from a variety of news organizations, parses their outputs, and adds that parsed data to the database.

- stock_collector.py

This collects stock market data, looking specifically at broad national market indexes, and adds the data to the database on a per-minute basis.

#### real_time_collectors

- twitter_follow_collector.py

This is the Twitter collector that takes in data based off of specific user accounts, parses the collected tweets, and adds the parsed data to the database.

- twitter_location_collector.py

This is the Twitter collector that takes in data based off of location inputs, parses the collected tweets, and adds the parsed data to the database.

- twitter_track_collector.py

This is the Twitter collector that takes in data based off of keywords, parses the collected tweets, and adds the parsed data to the database.

### analysis/

### dissemination/

#### sms_alerts

This disseminator will send out alerts in the form of SMS messages

### user_interface/

This directory will contain the HTML and CSS files, along with the Django backend, that will make up the web UI that controls this script.

### control.py

This is the control script that runs the rest of the project.

### setup.py

This is the file that sets up the other files and directories needed to run the rest of the project.

## Dependencies

This code relies on a few libraries that are not included in the standard Python 3 library. These are:

### feedparser

This is a library used in the RSS Collector for collecting RSS feeds from given URLs.

### tweepy

This is used in the various Twitter Collectors in order to connect to the Twitter streaming API.

### pandas

This is used in the Stock Collectors to convert the data into a usable format.

### twilio

This is used by in SMS_alerts to send text messages whenever there are critical events taking place.

### _keys_and_secrets

This is not a library - it is a Python file used to store and call passwords, keys, secrets, and other PII. The code that relies on such PII calls this file, and it makes for a convenient place to store such data.