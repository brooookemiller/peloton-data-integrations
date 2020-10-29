from google_integrations.google_authenticate import get_calendar_service


def create_event(summary, description, start, end, timezone):
    service = get_calendar_service()

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start,
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end,
            'timeZone': timezone,
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'popup', 'minutes': 45},
                {'method': 'popup', 'minutes': 30},
                {'method': 'popup', 'minutes': 15},
            ],
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()

    return print('Event created: %s' % (event.get('htmlLink')))


def get_events(start, end):
    service = get_calendar_service()

    page_token = None
    while True:
        events = service.events().list(
            calendarId='primary',
            timeMin=start,
            timeMax=end,
            pageToken=page_token
        ).execute()

        page_token = events.get('nextPageToken')
        if not page_token:
            break
    return events['items']
