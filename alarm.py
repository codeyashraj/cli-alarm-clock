from datetime import datetime, time, timedelta
import time as time_module


def parse_time(time_text):
    """Parse an HH:MM string into a datetime.time object."""
    try:
        return datetime.strptime(time_text.strip(), "%H:%M").time()
    except ValueError:
        raise ValueError("Invalid time. Please use HH:MM format.")


def next_alarm(current_datetime, alarm_time):
    """Return the next datetime at which the alarm should trigger."""
    alarm_datetime = datetime.combine(current_datetime.date(), alarm_time)

    # If the requested time is now or has already passed,
    # schedule it for tomorrow.
    if alarm_datetime <= current_datetime:
        alarm_datetime += timedelta(days=1)

    return alarm_datetime


def wait_until(alarm_datetime):
    """Wait until the specified alarm datetime."""
    try:
        while True:
            remaining = (alarm_datetime - datetime.now()).total_seconds()

            if remaining <= 0:
                break

            # Check approximately once per second.
            time_module.sleep(min(1, remaining))

    except KeyboardInterrupt:
        print("\nAlarm cancelled. Goodbye!")
        return False

    return True


def trigger_alarm():
    """Trigger the alarm notification."""
    print("\n🔔 ALARM! It's time!")
    input("Press Enter to turn off the alarm.")

def main():
    print("Alarm Clock")

    try:
        time_text = input("Enter alarm time (24-hour format, HH:MM): ")
        alarm_time = parse_time(time_text)

        current_datetime = datetime.now()
        alarm_datetime = next_alarm(current_datetime, alarm_time)

        print(f"Alarm set for {alarm_datetime.strftime('%Y-%m-%d %H:%M')}.")
        print("Waiting for alarm...")

        if wait_until(alarm_datetime):
            trigger_alarm()

    except ValueError as error:
        print(f"Error: {error}")
    except KeyboardInterrupt:
        print("\nAlarm cancelled. Goodbye!")


if __name__ == "__main__":
    main()