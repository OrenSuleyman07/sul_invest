import threading
import unittest
from collections import namedtuple
import main

class case(unittest.TestCase):
    request_list = namedtuple('Request', 'Quantity Price')
    
    def test_buy_add(self):
        buy_example = main.buy()
        request_id_1, actual_1, expected_1 = buy_example.add(9, 4)
        self.assertEqual(actual_1, expected_1)

        request_id_2, actual_2, expected_2 = buy_example.add(37, 95)
        self.assertEqual(actual_2, expected_2)

        buy_example.delete(request_id_2)

        request_id_3, actual_3, expected_3 = buy_example.add(64, 46)
        self.assertEqual(actual_3, expected_3)

        self.assertEqual(actual_2, expected_2)

    def test_buy_view(self):
        buy_example = main.buy()
        buy_example.add(195, 29)
        buy_example.add(1, 8)
        actual = buy_example.view()
        expected = [self.request_list(1, 8), self.request_list(195, 29)]
        self.assertEqual(actual, expected)
    
    def test_sale_add(self):
        sale_example = main.sale()
        request_id_1, actual_1, expected_1 = sale_example.add(5, 1)
        self.assertEqual(actual_1, expected_1)
        
        request_id_2, actual_2, expected_2 = sale_example.add(3, 16)
        self.assertEqual(actual_2, expected_2)

        sale_example.delete(request_id_2)

        request_id_3, actual_3, expected_3 = sale_example.add(8, 47)
        self.assertEqual(actual_3, expected_3)

        self.assertEqual(actual_2, expected_2)

    def test_sale_view(self):
        sale_example = main.sale()
        sale_example.add(36, 289)
        sale_example.add(9, 5)
        actual = sale_example.view()
        expected = [self.request_list(9, 5), self.request_list(36, 289)]
        self.assertEqual(actual, expected)   

test = case()

if __name__ == "__main__":
   unittest.main()