# CLI Alarm Clock

A simple command-line alarm clock implemented in Python using only the standard library.

The project intentionally keeps the scope small: it supports **one alarm at a time**, runs entirely in the terminal, and does not require a database, web UI, or external dependencies.

## Features

- Set a single alarm using 24-hour `HH:MM` format.
- Automatically schedules the alarm for:
  - Today, if the requested time is in the future.
  - Tomorrow, if the requested time has already passed or is exactly now.
- Waits until the scheduled time.
- Displays an alarm notification when triggered.
- Waits for the user to press **Enter** to turn off the alarm.
- Handles invalid time input.
- Handles `Ctrl+C` gracefully.
- Includes unit tests for the core time calculation logic.

## Project Structure

```text
.
├── alarm.py
├── test_alarm.py
└── README.md
```

### `alarm.py`

Contains the application logic:

- `parse_time()` — validates and parses the user's `HH:MM` input.
- `next_alarm()` — calculates the next occurrence of the requested alarm time.
- `wait_until()` — waits until the scheduled datetime.
- `trigger_alarm()` — displays the alarm and waits for the user to turn it off.
- `main()` — handles the CLI flow.

### `test_alarm.py`

Contains unit tests for the core scheduling behavior:

- Invalid time input.
- Future alarm scheduled for today.
- Past alarm scheduled for tomorrow.
- Alarm time exactly matching the current time.

## Requirements

- Python 3.8+
- No external packages are required.

The application uses only Python's standard library.

## Running the Application

From the project directory:

```bash
python alarm.py
```

You will be prompted to enter the alarm time:

```text
Alarm Clock

Enter alarm time (24-hour format, HH:MM): 07:30
Alarm set for 2026-10-02 07:30.
Waiting for alarm...
```

When the alarm triggers:

```text
🔔 ALARM! It's time!
Press Enter to turn off the alarm.
```

Press **Enter** to stop the alarm.

You can also press **Ctrl+C** while waiting to cancel the alarm.

## Running the Tests

Run the test suite with:

```bash
python -m unittest test_alarm.py
```

Expected result:

```text
....
----------------------------------------------------------------------
Ran 4 tests in ...
OK
```

## Design Decisions

### Single alarm

The application intentionally supports only one alarm. There is no alarm list, alarm IDs, or alarm management layer.

This keeps the implementation focused on the core scheduling problem.

### No database or persistence

Alarms exist only for the lifetime of the application. Once the program exits, the alarm is discarded.

A database would add unnecessary complexity for the current requirements.

### Standard library only

The implementation uses Python's built-in modules such as:

- `datetime`
- `time`
- `unittest`

No external dependencies are required.

### Testable time calculations

The scheduling logic is separated from the actual waiting logic.

For example, `next_alarm()` accepts the current datetime as an argument rather than directly depending on the system clock. This makes cases such as "future time is today" and "past time is tomorrow" deterministic and easy to test without waiting for a real alarm.

### Exact current time

If the requested alarm time is exactly the current time, it is treated as the **next occurrence tomorrow**. This avoids immediately triggering an alarm that has already reached its scheduled minute.

## Scope

The following features are intentionally outside the current scope:

- Multiple alarms
- Recurring alarms
- Snooze functionality
- Persistent alarms
- Database storage
- Web UI
- Desktop notifications
- Custom alarm sounds
- Time-zone selection
- Natural-language time input

These could be added later if the requirements expand.

## Testing Approach

The tests focus on the most important business logic rather than testing Python's standard-library behavior.

In particular, the tests verify:

1. Invalid user input is rejected.
2. A future alarm is scheduled for the current day.
3. A past alarm is scheduled for the following day.
4. An alarm exactly at the current time is scheduled for the following day.

The actual waiting loop is intentionally kept separate so unit tests do not need to wait for an alarm to occur.