# Information Collector

## Purpose

This project is to be a tool that take in requirements, such as keywords or locations, and collects 
data from open sources that corresponds to those requirements. In its final form, this will consist of 
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
will prepare the data to be further analyzed using speech tagging, topic modeling, sentiment analysis, 
and other forms of machine learning and statistical techniques.  

### Disseminators

Finally, processed or analyzed data will need to be disseminated to end users, with the option for both 
machine-readable and human-readable formats.  

## Modules

### setup.py

The file that sets up the files and directories needed to run the other scripts

### control.py

The control script that runs all of the other scripts.

### twitter_location_collector.py

The Twitter collector that takes in data based off of location inputs, parses the collected 
tweets, and adds the parsed data to the SQLite database.

### collector.sqlite3

The SQLite database that holds the data collected by the collectors.