import unittest
import json

from app import create_app

app_ = create_app('testing')

class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app_.test_client()
        self.tester_ride_offer = {}