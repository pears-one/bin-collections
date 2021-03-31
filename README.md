![screenshot](https://github.com/evanfpearson/bin-collections/blob/main/screenshot.jpg)

## What?

This is a cron service, written in Python which will SMS you when the bins need taking out. It currently only has support for UK councils. 

## Requirements

- Twilio account
- Sqlite3 database

## How does it work?

When triggered, this service will iterate through all properties in the Sqlite3 database, and scrape the council website for those properties' bin collections. If there are bins to be collected the next day, the service will text the residents at that property.

## How to run

A number of environment variables are needed to run this script. 
- `BIN_VENV` base directory of the Python virtual environment for this project
- `ACCOUNT_SID` Twilio Account ID
- `AUTH_TOKEN` Twilio Auth token
- `NUMBER` phone number that the texts will be sent from
- `DELAY_IN_DAYS` number of days before the collection that the texts should be sent
- `DB_ADDRESS` path to the Sqlite3 db file
- `LOG_FILE` output log file

### Test mode

To run the service in test mode you can use the shell script provided.

```shell
./run.sh 
```
This will not send out any SMS messages, but will print the message and recipient to STDOUT.

### Live

```shell
./run.sh live
```
This will run the service in the same way - but texts will be sent out to the residents of the properties which have bin collections.

## Adding Extensions

This service has been written with extensibility in mind, so adding new councils should be very simple. See the `CollectionScraper` class to understand what interfaces should be followed.

## TODO

- Unit testing
- Asynchronous requests
