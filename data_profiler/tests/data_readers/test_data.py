import unittest
try:
    from unittest import mock
except ImportError:
    import mock

import pandas as pd

from ...data_readers.data import Data


class TestDataReadingWriting(unittest.TestCase):

    def test_read_data(self):
        """Ensure error logs for trying to save empty data."""
        data_types = ['csv', 'json', 'parquet', 'text']
        none_types = [pd.DataFrame(), pd.DataFrame(), "", ""]
        for data_type, none_type in zip(data_types, none_types):
            Data(data=none_type, data_type=data_type)


if __name__ == '__main__':
    unittest.main()
