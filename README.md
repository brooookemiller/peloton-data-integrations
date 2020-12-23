# Leverage Your Peloton Data

## Overview

Helps Type A's keep their priorities (Peloton) in check and synchronizes their calendar accordingly.
Peloton has an API that we can hit to leverage our data and make use of it.

Features:

- See your last completed ride and upcoming Peloton classes you've opted into ([peloton_report.py][8])
- Create Google calendar events for your upcoming Peloton classes ([create_reservation_events.py][7])

## Installation and Usage

### Clone this repository and install dependencies

First things first: [clone][6] this repository. Open your code editor, navigate to the root folder, then run the below command to install the necessary dependences.

```bash
pip install -r requirements.txt
```

### Authenticate to Peloton

In order to access your Peloton data, you must authenticate to Peloton.

Create the environment variables: `PELOTON_USERNAME` and `PELOTON_PASSWORD` for local testing.

```bash
PELOTON_USERNAME = Your_Peloton_Username_Or_Email
PELOTON_PASSWORD = Your_Peloton_Password
```

Once you create these local environment variables, test your connection to peloton by running the command below in your terminal.

```bash
python peloton_report.py
```

This script will print your recent workouts and upcoming reservations to your terminal.

### Authenticate to Google

In order to read or write to your Google Calendar, you must authenticate to Google. Follow the [first step here][1] to turn on the Google Calendar API and download your client_secret.json file.

Once your client_secret.json file is created and stored locally, run:

```bash
python3 google_integrations/google_authenticate.py
```

Follow the [fourth step here][2] to log into your Google account and authorize access.

### Test the feature script locally

Now that you have your secrets created and your dependencies installed, it's time to test the real deal. (The real deal I'm referring to is the best feature included in this repo, which is to create Google calendar events for your upcoming reserved Peloton classes.)

Run the below command in your terminal:

```bash
python create_reservation_events.py
```

.... and voila!

### Set up the infrastructure to run the scripts in Google Cloud

Now that you can run this script locally, you obviously don't want to run it locally all the time. So, let's set it up on a cron job to run at whatever cadence you like without having to even think about it.

Google App Engine can accomplish this. [Watch this one-minute video][3] that summarizes how to deploy a Python app on Google Cloud.

- Visit the [Google Cloud console][4]
- Create a project (ex: peloton-data-integrations)
- Enable billing (you won't exceed the free features if you follow these steps)
- Install the [Google Cloud SDK][5] to more easily manage your AppEngine
- Run the below command to deploy the app

```bash
gcloud app deploy
```

- Create secrets in Google Secret Manager
- Create the cron job based on the cadece you prefer

## Peloton Client Library

Thanks to @geudrik, I leveraged this peloton-client-library repo (which actually has [API docs]((https://github.com/geudrik/peloton-api/blob/master/API_DOCS.md)!). Super appreciative of these docs and the foundation he set up.

[1]: https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the
[2]: https://developers.google.com/calendar/quickstart/python#step_4_run_the_sample
[3]: https://www.youtube.com/watch?v=T_4cGEtHqUs
[4]: console.cloud.google.com
[5]: https://cloud.google.com/sdk/docs/install
[6]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[7]: https://github.com/brooookemiller/peloton-data-integrations/blob/master/create_reservation_events.py
[8]: https://github.com/brooookemiller/peloton-data-integrations/blob/master/peloton_report.py
