from main import Collection
import unittest
import datetime

class BinCollectionTest(unittest.TestCase):
    monday_blue = Collection("Blue", "Monday 4 Nov 2019")
    friday_brown = Collection("Brown", "Friday 6 Dec 2019")
    thursday_green = Collection("Green", "Thursday 21 Nov 2019")
    wednesday_grey = Collection("Grey", "Wednesday 13 Nov 2019")

    def test_get_date(self):
        self.assertEqual(self.monday_blue.get_date(), datetime.datetime(2019,11,4))
        self.assertEqual(self.friday_brown.get_date(), datetime.datetime(2019,12,6))
        self.assertEqual(self.thursday_green.get_date(), datetime.datetime(2019,11,21))
        self.assertEqual(self.wednesday_grey.get_date(), datetime.datetime(2019,11,13))

if __name__ == "__main__":
    unittest.main()
