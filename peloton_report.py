from peloton import PelotonWorkout, PelotonReservation, PelotonRideFromReservation
from pytz import timezone
from datetime import datetime


def convert_to_est(dt):
    fmt = "%Y-%m-%d %H:%M"
    converted = dt.astimezone(timezone('US/Eastern'))
    return converted.strftime(fmt)


def get_recent_workout():
    workouts = PelotonWorkout.list()
    workout = workouts[0]
    dir(workout)

    print("\n")
    print("Recently Completed:")
    print(workout.ride.title, "on", convert_to_est(workout.start_time))
    return True


def get_upcoming_reservations():
    reservations = PelotonReservation.list()
    dir(reservations)

    print("\n")
    print("Upcoming Reserved Live Classes:")
    for reservation in reservations:
        reservation = PelotonReservation.get(reservation.id)
        dir(reservation)

        ride_id = reservation.ride_id
        ride = PelotonRideFromReservation.get(ride_id)
        print(ride.title, "on", convert_to_est(reservation.scheduled_start))
    return True


def main():
    get_recent_workout()
    get_upcoming_reservations()


if __name__ == '__main__':
    main()
