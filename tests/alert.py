import unittest
from model.alert import Alert
from collection.bin_day import BinDay
from model.person import Person
from datetime import date


class TestAlert(unittest.TestCase):

    def test_get_message(self):
        msg = "there is an issue with the Alert.get_message method, %s != %s"
        tests = [
            {
                "person": Person("Json", "+447987654321", "1000000"),
                "bin_day": BinDay(date(2021, 3, 28), ['brown', 'green', 'black']),
                "message": "Hi Json, the brown, green and black bins are getting collected on Sunday, 28th March."
            },
            {
                "person": Person("Pedantic Nick", "+447777777777", "1000001"),
                "bin_day": BinDay(date(1996, 5, 28), ['paper']),
                "message": "Hi Pedantic Nick, the paper bins are getting collected on Tuesday, 28th May."
            }
        ]
        for test in tests:
            expected = test["message"]
            actual = Alert(test["person"], test["bin_day"]).get_message()
            self.assertEqual(expected, actual, msg.format(expected, actual))
