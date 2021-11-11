"""
Smoke tests for blackfowl

These are tests that should be picked up and run by whichever testrunner is being used by the project. If these are not being picked up, then it needs to be configured.

"""

import unittest


class BlackfowlSmokeTest(unittest.TestCase):
    # Simple tests meant to be detectable
    def test_basic_logic(self):
        self.assertTrue(True)
