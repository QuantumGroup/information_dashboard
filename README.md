# Information Collector

## Purpose

This project is to be a tool that takes in user requirements, such as keywords or locations, and collects 
data from open sources that correspond to those requirements. In its final form, this will consist of 
a few different components.

## Components

### User Interface

A web-based UI will be the main way of updating the collection requirements, as well as one of the ways 
of viewing the results from the collectors.

### Collectors

A number of collectors will be built for different sources, each with different capabilities. Examples 
to date include collectors that take in data from the Twitter API and collectors that take in news site RSS 
feeds live.

### Processors

Once data is collected from its various sources, it will be processed into a standardized format so that 
it can be either disseminated in that raw format or so that it can be further broken down for analysis 
purposes.

### Analyzers

Formatted data will be run through a number of analyzers, starting with natural language processors that 
will prepare the data to be further broken down using speech tagging, topic modeling, sentiment analysis, 
and other machine learning and statistical techniques.  

### Disseminators

Finally, the processed and/or analyzed data will need to be disseminated to end users, with options for both 
machine-readable and human-readable formats.  

## Modules

### setup.py

This is the file that sets up the other files and directories needed to run the rest of the project.

### control.py

This is the control script that runs the rest of the project.

### collector.sqlite3

This is the SQLite database that holds the data ingested by the collectors.

### alerts.py

### facebook_collector.py

### rss_collector.py

### twitter_location_collector.py

This is the Twitter collector that takes in data based off of location inputs, parses the collected 
tweets, and adds the parsed data to the SQLite database.

### twitter_follow_collector.py

### twitter_track_collector.py

## Dependencies

This code relies on a few libraries that are not included in the standard Python 3 library. These are:

- feedparser

This is a library used in the RSS Collector for collecting RSS feeds from given URLs.

- tweepy

This is used in the various Twitter Collectors in order to connect to the Twitter streaming API.

- _keys_and_secrets

This is not a library - it is a Python file used to store and call passwords, keys, secrets, and other PII. The 
code that relies on such PII calls this file, and it makes for a convenient place to store such data. 