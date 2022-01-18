import requests
from django.test import TestCase
from unittest.mock import Mock, patch
import json

from elsys.processors.apiHandler import ApiHandler

class TestApi(TestCase):
    @patch("requests.get")
    def test_min_temp(self, mocked_requests):
            data = json.load(open('./elsys/temperatureTest.json'))
            mocked_requests.return_value.json = Mock(return_value = data)
            assert ApiHandler().minimum_temp() == 3

    @patch("requests.get")
    def test_max_temp(self, mocked_requests):
            data = json.load(open('./elsys/temperatureTest.json'))
            mocked_requests.return_value.json = Mock(return_value = data)
            assert ApiHandler().maximum_temp() == 8

    @patch("requests.get")
    def test_avg_temp(self, mocked_requests):
            data = json.load(open('./elsys/temperatureTest.json'))
            mocked_requests.return_value.json = Mock(return_value = data)
            assert ApiHandler().avg_temp() == 5.0