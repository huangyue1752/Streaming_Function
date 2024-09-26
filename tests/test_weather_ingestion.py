# tests/test_ingestion.py

import unittest
from streaming_function.weather_streaming_function import WeatherDataIngestion

class TestWeatherDataIngestion(unittest.TestCase):
    def test_get_weather_data(self):
        # Replace with your city for testing
        ingestion = WeatherDataIngestion('New York', 'conn_str', 'eventhub_name')
        data = ingestion.get_weather_data()
        self.assertIsNotNone(data)  # Check if data is not None

if __name__ == '__main__':
    unittest.main()
