from google_integrations.calendar_api import create_event, get_events
from peloton import PelotonReservation, PelotonRideFromReservation
from datetime import datetime, timedelta
from pytz import timezone
import re
from flask import Flask, jsonify

app = Flask(__name__)

START = datetime.now()
END = START + timedelta(weeks=2)


def convert_to_est(dt):
    fmt = "%Y-%m-%d %H:%M"
    converted = dt.astimezone(timezone('US/Eastern'))
    return converted.strftime(fmt)


@app.route('/')
def create_calendar_event():
    reservations = PelotonReservation.list()
    messages = []

    for reservation in reservations:
        on_calendar = False
        reservation = PelotonReservation.get(reservation.id)

        # Get relevant ride details
        ride_id = reservation.ride_id
        ride = PelotonRideFromReservation.get(ride_id)
        summary = ride.title
        description = ride.description
        ride_start = reservation.scheduled_start
        ride_end = ride_start + timedelta(minutes=int(summary[0: 2]))

        # Clean up datetime variables to compare
        timezone = "America/New_York"
        report_start = convert_to_est(START)
        report_end = convert_to_est(END)
        ride_start_c = convert_to_est(ride_start)
        ride_end_c = convert_to_est(ride_end)

        if ride_start_c >= report_start and ride_end_c < report_end:
            cal_events = get_events(
                ride_start.isoformat(), ride_end.isoformat())
            if len(cal_events) > 0:
                for event in cal_events:
                    if re.search(ride.title, event['summary']):
                        on_calendar = True

            if on_calendar is True:
                print(ride.title + " on " + str(ride_start.date()) +
                      " is already on your calendar.")
                message = (ride.title + " on " + str(ride_start.date()) +
                           " is already on your calendar.")
                messages.append(message)
            else:
                print("About to schedule: " + ride.title)
                create_event(summary, description, ride_start.isoformat(
                ), ride_end.isoformat(), timezone)

                message = ("About to schedule: " + ride.title)
                messages.append(message)

    return jsonify(messages)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
