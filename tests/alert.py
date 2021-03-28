import unittest
from model.alert import Alert, AlertError
from collection.bin_day import BinDay
from model.person import Person
from datetime import date


class TestAlert(unittest.TestCase):

    def test_get_message(self):
        this_year = date.today().year
        msg = "there is an issue with the Alert.get_message method, %s != %s"
        march28 = date(this_year + 1, 3, 28)
        may3 = date(this_year + 1, 5, 3)
        may28 = date(this_year - 1, 5, 28)
        tests = [
            {
                "person": Person("Json", "+447987654321", "1000000"),
                "bin_day": BinDay(march28, ['brown', 'green', 'black']),
                "message": f"Hi Json, the brown, green and black bins are getting collected on {march28.strftime('%A')}, 28th March.",
                "should_fail": False
            },
            {
                "person": Person("Pedantic Nick", "+447777777777", "1000001"),
                "bin_day": BinDay(may3, ['paper']),
                "message": f"Hi Pedantic Nick, the paper bins are getting collected on {may3.strftime('%A')}, 3rd May.",
                "should_fail": False
            },
            {
                "person": Person("EP", "+447910777777", "1000002"),
                "bin_day": BinDay(may28, ['paper']),
                "message": f"Hi EP, the bins are getting collected on {may28.strftime('%A')}, 28th May.",
                "should_fail": True
            },
            {
                "person": Person("Boris", "+447000111222", "1000002"),
                "bin_day": BinDay(may3, []),
                "message": f"Hi EP, the bins are getting collected on {may3.strftime('%A')}, 3rd May.",
                "should_fail": True
            }
        ]
        for test in tests:
            expected = test["message"]
            actual = Alert(test["person"], test["bin_day"])
            if test["should_fail"]:
                with self.assertRaises(AlertError):
                    actual.get_message()
                continue
            self.assertEqual(expected, actual.get_message(), msg.format(expected, actual))
