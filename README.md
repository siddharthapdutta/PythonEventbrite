# [Eventbrite](https://www.eventbrite.com/) API Implementation

[API Reference](https://www.eventbrite.com/platform/api)

## Requirements
* Private token for the Eventbrite API. Available [here](https://www.eventbrite.com/platform/api-keys).
* Event ID for the checkout widget.


## Steps
* Add private token to line 5 of **EventbriteEvent.py** file.
* Add event id to line 15 of **checkout.html** file.

## Screenshot
![screenshot](https://github.com/siddharthapdutta/PythonEventbrite/blob/master/eventorder.png?raw=true)

## Outcome
* The Python script returns a list of the event attendees.
* Alternatively, the order ID can be scraped from the widget and used. (Variable *orderID* implemented in **checkout.html** but not tested)