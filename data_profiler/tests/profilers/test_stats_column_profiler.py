from __future__ import print_function

from data_profiler.profilers.column_profile_compilers import \
    ColumnStatsProfileCompiler
from data_profiler.tests.profilers.test_base_column_profilers import \
    AbstractTestColumnProfiler

import os
import unittest


test_root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class TestColumnStatsProfiler(AbstractTestColumnProfiler, unittest.TestCase):

    column_profiler = ColumnStatsProfileCompiler
    profile_keys = ['data type', 'statistics']

    def setUp(self):
        AbstractTestColumnProfiler.setUp(self)

    @classmethod
    def setUpClass(cls):
        super(TestColumnStatsProfiler, cls).setUpClass()


if __name__ == '__main__':
    unittest.main()
