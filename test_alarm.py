import unittest
from datetime import datetime, time

from alarm import parse_time, next_alarm


class TestAlarm(unittest.TestCase):

    def test_parse_invalid_time(self):
        with self.assertRaises(ValueError):
            parse_time("25:00")

        with self.assertRaises(ValueError):
            parse_time("not-a-time")

    def test_future_alarm_is_today(self):
        current = datetime(2026, 10, 1, 10, 0)
        alarm_time = time(11, 30)

        result = next_alarm(current, alarm_time)

        expected = datetime(2026, 10, 1, 11, 30)
        self.assertEqual(result, expected)

    def test_past_alarm_is_tomorrow(self):
        current = datetime(2026, 10, 1, 22, 0)
        alarm_time = time(7, 30)

        result = next_alarm(current, alarm_time)

        expected = datetime(2026, 10, 2, 7, 30)
        self.assertEqual(result, expected)

    def test_alarm_exactly_now(self):
        current = datetime(2026, 10, 1, 10, 0)
        alarm_time = time(10, 0)

        result = next_alarm(current, alarm_time)

        expected = datetime(2026, 10, 2, 10, 0)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()