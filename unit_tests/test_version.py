import unittest
import os
import scriptum.version

class VersionTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_VERSION(self):
        self.assertIsNotNone(scriptum.version.VERSION)
        self.assertRegex(scriptum.version.VERSION, "\d+\.\d+\.\d+")
