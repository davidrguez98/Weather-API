import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import unittest
from unittest.mock import patch
from backend import weather_functions

class Test(unittest.TestCase):

    @patch("requests.get")
    def test_good_request(self, mock_get):

        mock_response = {
            "resolvedAddress": "Seville, Spain",
            "days": [
                {
                    "datetime": "2025-02-25",
                    "temp": 20.5,
                    "tempmax": 25.0,
                    "tempmin": 15.0,
                    "precipprob": 10
                }
            ]
        }

        mock_get.return_value.json.return_value = mock_response
        result = weather_functions.get_weather_data("Seville", "3")

        self.assertEqual(result, mock_response)
        self.assertIn("resolvedAddress", result)
        self.assertIn("days", result)

    @patch("requests.get")
    def test_error_conection(self, mock_get):

        mock_get.side_effect = requests.exceptions.RequestException

        result = weather_functions.get_weather_data("Seville", "3")
        
        self.assertIsNone(result)

    @patch("requests.get")
    def test_error_city(self, mock_get):

        mock_get.return_value.status_code = 400
        mock_get.return_value.json.return_value = {}

        result = weather_functions.get_weather_data("CiudadInventada", "2")

        self.assertIsNone(result, "La función devuelve None")

    @patch("requests.get")
    def test_error_server(self, mock_get):
        
        mock_get.return_value.status_code = 500
        mock_get.return_value.json.return_value = {}

        result = weather_functions.get_weather_data("Seville", "2")

        self.assertIsNone(result, "La función devuelve None")

    @patch("requests.get")
    def test_empty_request(self, mock_get):
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {}

        result = weather_functions.get_weather_data("Seville", "2")

        self.assertIsNone(result, "La función devuelve None")

unittest.main()