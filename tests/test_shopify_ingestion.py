# tests/test_shopify_ingestion.py

import unittest
from streaming_function.shopify_ingestion_library import IngestionFramework

class TestShopifyDataIngestion(unittest.TestCase):
    def test_initialization(self):
        ingestion = IngestionFramework('subscription_name', 'conn_str', 'eventhub_name')
        self.assertEqual(ingestion.subscription_name, 'subscription_name')

    # More tests can be added here for other functionalities

if __name__ == '__main__':
    unittest.main()
