import os, sys
sys.path.append(os.getcwd())

import unittest
from test import IndexTest

suite = unittest.TestLoader().loadTestsFromTestCase(IndexTest.IndexTest)
unittest.TextTestRunner(verbosity=2).run(suite)