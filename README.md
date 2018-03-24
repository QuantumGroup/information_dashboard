release 0.0.0. 2018-03-24

# The Information Edge Tool (working title)

## About the Information Edge Tool (working title)

The foundational piece of all of Serendipity Research's future efforts, this project is a platform designed to collect, process, and analyze open source information in order to recognize breaking news events before they become breaking news.

This project is designed to take in information from as many sources as possible in order to provide analytical judgements, based on techniques grounded in political science research and powered by techniques from computer science.

## How it Works
Not only is this project built using iterative project management techniques, but the platform itself is meant to be iterative - there will always be new means of collecting information, more sources of information, and more methods by which to analyze them. As such, there is no concrete list of all the kinds of sources and methods that will be used, but the following give an idea of the operational concept.

### Taxonomy of Data

#### "Verified events"
These events make up our baseline for what an event is.

In our parlance, an event is "a present-time news event concerning important people, places, things, and ideas," and we search for these wherever they are to be found. A verified event, then, is an event that has been confirmed by reputable sources, either internal or external.

#### "Potential events"
In our search for events, we look at tradition sources for verification, backtesting, and backstopping of our more experimental methods. However, since our goal is to recognize events before traditional organizations, we must look towards these experimental methods to pinpoint potential events.

Potential events, then, are events that are sourced from non-reputable sources, and must be corroborated through other means. These potential events usually begin as social events, which are events that are planned by people, attended by people, and for which the social multimedia is also captured by people.

It is therefore the ultimate objective of the information edge tool to corroborate potential events, transforming them into verified events before they become breaking news.

#### Indicators of events
In looking for events, we also look for environmental variables that could lead to events. Most of these come from automated sources, and although their veracity is usually without a doubt, their ability to lead to an event must be verified. For example, automated sensors pick up earthquakes of magnitude 5.0 or greater worldwide almost immediately, but the difference between such an earthquake occurring in a remote ocean trench as opposed to one occurring in a densely populated area is the difference between this being an event or merely an indicator.

However, having access to such indicators can strengthen our ability to turn potential events into verified events, and in certain circumstances can circumvent the usual sources of potential events and be used as the basis for an alert based only on automated indicator collection.

### Sources of Data

#### News organizations
These include national papers of record, global news wires, and other news sources of import. They are used to collect verified events.

The purpose behind collecting these is that they, collectively and in aggregate, are a record of events. As such, they allow for backtesting of experimental methods applied to other sources.

#### Social networks
These include social media sites that are used by the general public to upload breaking information, such as Twitter, Facebook, Instagram, and others. They are used to collect potential events.

#### Companies
These (mostly) include geospatial and remote sensing companies, such as Digital Globe, Spot Image, and others. They are used primarily to collect indicators of events.

#### Governmental organization
These include (mostly) American and European governmental agencies, such as the United States Geological Service, Centers for Disease Control and Prevention, National Aeronautics and Space Administration, and others. They are used primarily to collect indicators of events.

#### Non-governmental organizations
These include organizations the report on human health, natural hazards, and economic, political, and demographic indicators.

## Components

### Collectors

A number of collectors will be built for different sources, each with different capabilities. Examples to date include collectors that take in data from the Twitter API and collectors that take in news site RSS feeds live. These collectors will also be in charge of data pre-processing, i.e. converting the data into a machine-readable format.

### Analyzers

Pre-processed data will be run through a number of analyzers, starting with natural language processors that will prepare the data to be further broken down using speech tagging, topic modeling, sentiment analysis, and other machine learning and statistical techniques.

### Disseminators

Finally, the processed and/or analyzed data will need to be disseminated to end users,  with a 2-tier data feed system providing information to users - one is an automated feed that depends solely on the machine learning algorithms, while another feed is human-curated feed of verified actionable information.

### User Interface

FOr those without access to the primary data feed, a web-based UI will be one of the ways of demonstrating the results from the collectors.

## Modules

### analysis/

This directory will contain the analzyers that turn our raw data into actionable information.

### collection/

This directory contains the collection and pre-processing scripts, divided by temporal type.

#### batch_collectors

- headline_collector.py

This is the collectors that takes in data from a variety of news organizations, parses their outputs, and adds that parsed data to the database.

#### real_time_collectors

- twitter_sample_collector.py

This is the Twitter collector that takes in a portion of the entire Twitter stream and saves it for further analysis

### dissemination/

This directory contains the scripts that send out the analyzed data.

#### sms_alerts

This disseminator will send out alerts in the form of SMS messages.

### setup/

This directory contains the files that set up the other files and directories needed to run the rest of the project.

### user_interface/

This directory will contain the HTML and CSS files, along with the Django backend, that will make up the web UI.

### control.py

This is the control script that runs the rest of the project.

### error.py

This is the scripts that controls what processes are run whenever errors are encountered.

## Dependencies

This code relies on a few libraries that are not included in the standard Python 3 library. These are:

### feedparser

This is a library used in the Headline Collector for collecting RSS feeds from given URLs.

### tweepy

This is used in the various Twitter Collectors in order to connect to the Twitter streaming API.

### twilio

This is used by in SMS_alerts to send text messages whenever there are critical events taking place.

### _keys_and_secrets

This is not a library - it is a Python file used to store and call passwords, keys, secrets, and other PII. The code that relies on such PII calls this file, and it makes for a convenient place to store such data.