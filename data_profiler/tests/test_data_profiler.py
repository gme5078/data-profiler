from __future__ import print_function

from .. import Data, Profiler
from . import test_utils

import unittest
from unittest import mock
import os


# This is taken from: https://github.com/rlworkgroup/dowel/pull/36/files
# undo when cpython#4800 is merged.
unittest.case._AssertWarnsContext.__enter__ = test_utils.patched_assert_warns


MODULE_PATH = os.path.dirname(os.path.abspath(__file__))
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class TestDataProfiler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        test_dir = os.path.join(MODULE_PATH, 'data')
        cls.input_file_names = [
            dict(path=os.path.join(test_dir, 'csv/aws_honeypot_marx_geo.csv'), type='csv'),
        ]

    def test_data_import(self):
        for file in self.input_file_names:
            data = Data(file['path'])
            self.assertEqual(data.data_type, file['type'])

    def test_data_profiling(self):
        for file in self.input_file_names:
            data = Data(file['path'])
            profile = Profiler(data)
            self.assertIsNotNone(profile.profile)
            self.assertIsNotNone(profile.report())

    def test_no_snappy(self):
        import sys
        import importlib
        import types
        orig_import = __import__
        # necessary for any wrapper around the library to test if snappy caught
        # as an issue

        def reload_data_profiler():
            """Recursively reload modules."""
            sys_modules = sys.modules.copy()
            for module_name, module in sys_modules.items():
                # Only reload top level of the data_profiler
                if ('data_profiler' in module_name and
                        len(module_name.split('.')) < 3):
                    if isinstance(module, types.ModuleType):
                        importlib.reload(module)

        def import_mock(name, *args):
            if name == 'snappy':
                raise ImportError('test')
            return orig_import(name, *args)

        with mock.patch('builtins.__import__', side_effect=import_mock):
            with self.assertWarns(ImportWarning) as w:
                import data_profiler
                reload_data_profiler()

        self.assertEqual(
            str(w.warning),
            'Snappy must be installed to use parquet/avro datasets.'
            '\n\n'
            'For macOS use Homebrew:\n'
            '\t`brew install snappy`'
            '\n\n'
            'For linux use apt-get:\n`'
            '\tsudo apt-get -y install libsnappy-dev`\n',
        )


if __name__ == '__main__':
    unittest.main()
