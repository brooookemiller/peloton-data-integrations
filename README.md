# Leverage Your Peloton Data

I took the Peloton API and built some features around it to manage upcoming classes.

## Features

- Create Google calendar events for your upcoming Peloton classes ([create_reservation_events.py][7])
![UX Image](https://github.com/brooookemiller/peloton-data-integrations/blob/master/photos/user_experience.jpg)
- See your last completed ride and upcoming Peloton classes you've opted into ([peloton_report.py][8])

### Built With

Take a peek at the APIs and tools utilized:
![Architecture Image](https://github.com/brooookemiller/peloton-data-integrations/blob/master/photos/architecture_overview.jpg)

## Getting Started

### Clone this repository and install dependencies

Clone this repository and install the necessary dependences.

```bash
pip install -r requirements.txt
```

### Authenticate to Peloton

In order to access your Peloton data, you must authenticate to Peloton.

Create a `.env` file locally and add the following environment variables:

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

In order to read or write to your Google Calendar, you must authenticate to Google. Follow the [first step here][1] to turn on the Google Calendar API and download your `client_secret.json` file.

Once your `client_secret.json` file is created, run:

```bash
python3 google_integrations/google_authenticate.py
```

Follow the [fourth step here][2] to log into your Google account and authorize access.

### Test the feature script locally

Now that you have your secrets created and your dependencies installed, it's time to test the real deal.

Run the below command in your terminal:

```bash
python create_reservation_events.py
```

.... and voila!

### [Optional] Set up the infrastructure to run the scripts in Google Cloud

If you're looking to automate this, set up a cron job to run this script at whatever cadence you'd like, using Google App Engine.

[Watch this one-minute video][3] that summarizes how to deploy a Python app on Google Cloud.

- Visit the [Google Cloud console][4]
- Create a project (ex: peloton-data-integrations)
- Enable billing (you won't exceed the free features if you follow these steps)
- Install the [Google Cloud SDK][5] to more easily manage your AppEngine
- Run the below command to deploy the app

```bash
gcloud app deploy
```

- Create secrets in Google Secret Manager
- Create a cron job based on the cadence you prefer

## Peloton Client Library

Thanks to @geudrik, I leveraged [this peloton-client-library repo][9], which actually has very useful [Peloton API docs][10]! 
Super appreciative of these docs and the foundation he set up.

[1]: https://developers.google.com/calendar/quickstart/python#step_1_turn_on_the
[2]: https://developers.google.com/calendar/quickstart/python#step_4_run_the_sample
[3]: https://www.youtube.com/watch?v=T_4cGEtHqUs
[4]: console.cloud.google.com
[5]: https://cloud.google.com/sdk/docs/install
[6]: https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository
[7]: https://github.com/brooookemiller/peloton-data-integrations/blob/master/create_reservation_events.py
[8]: https://github.com/brooookemiller/peloton-data-integrations/blob/master/peloton_report.py
[9]: https://github.com/geudrik/peloton-client-library
[10]: https://github.com/geudrik/peloton-api/blob/master/API_DOCS.md
