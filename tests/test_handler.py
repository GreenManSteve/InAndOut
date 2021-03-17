import unittest
import index
from patient.product import Product


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Hello World', result['body'])

    def test_barcode_is_valid(self):
        product = Product("5013655012088")
        assert product.is_valid()


if __name__ == '__main__':
    unittest.main()
