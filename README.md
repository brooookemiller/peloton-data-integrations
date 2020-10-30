# Leverage Your Peloton Data

## Overview

Peloton has an API that we can hit to leverage our data and make use of it.

Features:

- See your last completed ride and upcoming Peloton classes you've opted into (peloton_report.py)
- Create Google calendar events for your upcoming Peloton classes (main.py)

## Installation and Usage

### Authenticate to Peloton

In order to get your Peloton data, you must authenticate to Peloton. You may specify the environment variables `PELOTON_USERNAME` and `PELOTON_PASSWORD` which will take precedence over the config file.

```bash
PELOTON_USERNAME = Your_Peloton_Username_Or_Email
PELOTON_PASSWORD = Your_Peloton_Password
```

### Authenticate to Google

In order to read or write to your Google Calendar, you must also authenticate to Google. Follow [these steps][1].

### Example Usage

## Peloton Client Library

Thanks to @geudrik, I leveraged this peloton-client-library repo (which actually has [API docs]((https://github.com/geudrik/peloton-api/blob/master/API_DOCS.md)!).

[1]: https://developers.google.com/calendar/quickstart/python
[2]: https://www.youtube.com/watch?v=T_4cGEtHqUs # How to Deploy a Python app on Google Cloud
