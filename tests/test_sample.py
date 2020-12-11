import unittest
import pandas as pd
from sample.sample import *


class MyTestCase(unittest.TestCase):
    def test_relativeDelta(self):
        delta = datetime.timedelta(0, 00, 12, 0o3)
        result = relativeDelta(pd.to_datetime('2019-11-01 00:48:41'), pd.to_datetime('2019-11-01 01:00:44'))
        self.assertEqual(result, delta)
        result = relativeDelta(pd.to_datetime('2019-11-01 00:48:41'), pd.to_datetime('2019-11-01 01:03:01'))
        self.assertFalse(result == delta)
        self.assertRaises(Exception, relativeDelta(pd.to_datetime('2019-11-01 00:48:41'), pd.to_datetime('2019-11-01 00:48:41')))

    def test_calculateEndTime(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
