# -*- coding: utf-8 -*-
import requests
import json

PRIVATE_TOKEN = '' # https://www.eventbrite.com/platform/api-keys

def get_userID():
    ''' Returns str '''
    url = 'https://www.eventbriteapi.com/v3/users/me/'
    headers = {
        'Authorization': 'Bearer '+PRIVATE_TOKEN,
    }
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)
    
    if response.status_code == 200:
        userID = resp['id']
        return userID
    else:
        raise ValueError(resp['error_description'])

def get_orgs(userID):
    ''' Returns dict {org_name: org_id} '''
    url = 'https://www.eventbriteapi.com/v3/users/{}/organizations/'.format(userID)
    headers = {
        'Authorization': 'Bearer '+PRIVATE_TOKEN,
    }
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    if response.status_code == 200:
        orgs = {}
        for org in resp['organizations']:
            orgs[org['name']] = org['id']
        return orgs
    else:
        raise ValueError(resp['error_description'])

def create_event(orgID):
    ''' 
    Creates an Event with Data. 
    Ref URL: https://www.eventbrite.com/platform/docs/create-events
    Returns str 
    '''
    url = 'https://www.eventbriteapi.com/v3/organizations/{}/events/'.format(orgID)
    headers = {
        'Authorization': 'Bearer '+PRIVATE_TOKEN,
        'Accept': 'application/json',
    }
    data = {'event.name.html': 'API Event',
            'event.start.timezone': 'America/Los_Angeles',
            'event.start.utc': '2020-12-01T02:00:00Z',
            'event.end.timezone': 'America/Los_Angeles',
            'event.end.utc': '2020-12-01T05:00:00Z',
            'event.currency': 'USD',
            }
    response = requests.post(url, headers=headers, data=data)
    resp = json.loads(response.text)
    
    if response.status_code == 200:
        return resp['id']
    else:
        raise ValueError(resp['error_description'])
        
def add_ticket_class(eventID):
    '''
    Ref URL: https://www.eventbrite.com/platform/docs/ticket-classes
    Returns bool
    '''
    url = 'https://www.eventbriteapi.com/v3/events/{}/ticket_classes/'.format(eventID)
    headers = {
        'Authorization': 'Bearer '+PRIVATE_TOKEN,
        'Accept': 'application/json',
    }
    data = {'ticket_class.name': 'TicketClass',
            'ticket_class.quantity_total': 10,
            'ticket_class.free': True,
            #'ticket_class.cost': 'USD,1' # If not free
            }
    response = requests.post(url, headers=headers, data=data)
    resp = json.loads(response.text)

    if response.status_code == 200:
        return True
    else:
        raise ValueError(resp['error_description'])

def publish_event(eventID):
    ''' Returns bool '''
    url = 'https://www.eventbriteapi.com/v3/events/{}/publish/'.format(eventID)
    headers = {
        'Authorization': 'Bearer '+PRIVATE_TOKEN,
        'Accept': 'application/json',
    }
    response = requests.post(url, headers=headers)
    resp = json.loads(response.text)
    
    if response.status_code == 200:
        return True
    else:
        raise ValueError(resp['error_description'])

def get_event_attendees(eventID):
    ''' Returns list of Attendee Email IDs '''
    url = 'https://www.eventbriteapi.com/v3/events/{}/attendees/'.format(eventID)
    headers = {
        'Authorization': 'Bearer '+PRIVATE_TOKEN,
    }
    response = requests.get(url, headers=headers)
    resp = json.loads(response.text)

    if response.status_code == 200:
        return [att['profile']['email'] for att in resp['attendees']]
    else:
        raise ValueError(resp['error_description'])

userID = get_userID()
orgs = get_orgs(userID)
orgID = list(orgs.values())[0] # Pick Organization ID
eventID = create_event(orgID)
add_ticket_class(eventID)
publish_event(eventID)
attendees = get_event_attendees(eventID)
print(attendees)


