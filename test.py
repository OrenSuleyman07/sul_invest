import threading
import unittest
from random import randint
from collections import namedtuple
import main
import time

class case(unittest.TestCase):
    request_example = namedtuple('Request', 'Quantity Price')
    def test_buy_add(self):
        buy_example = main.buy()
        request_id_1 = buy_example.add(9, 4)
        self.assertEqual(self.request_example(9, 4), buy_example.get(request_id_1))

        request_id_2 = buy_example.add(37, 95)
        self.assertEqual(self.request_example(37, 95), buy_example.get(request_id_2))

        buy_example.delete(request_id_2)

        request_id_3 = buy_example.add(64, 46)
        self.assertEqual(self.request_example(64, 46), buy_example.get(request_id_3))

        self.assertIsNone(buy_example.get(request_id_2))

    def test_buy_None(self):
        buy_example = main.buy()
        request_id = buy_example.add(randint(0, 1000), 0)
        self.assertIsNone(buy_example.get(request_id)[1])
    
    def test_sale_add(self):
        sale_example = main.sale()
        request_id_1 = sale_example.add(5, 1)
        self.assertEqual(self.request_example(5, 1), sale_example.get(request_id_1))
        
        request_id_2 = sale_example.add(3, 16)
        self.assertEqual(self.request_example(3, 16), sale_example.get(request_id_2))

        sale_example.delete(request_id_2)

        request_id_3 = sale_example.add(8, 47)
        self.assertEqual(self.request_example(8, 47), sale_example.get(request_id_3))

        self.assertIsNone(sale_example.get(request_id_2))

    def test_sale_None(self):
        sale_example = main.sale()
        request_id = sale_example.add(randint(0, 1000), 0)
        self.assertIsNone(sale_example.get(request_id)[1])


class threadTest(unittest.TestCase):
    request_example = namedtuple('Request', 'Quantity Price')
    sale_example = main.sale()
    buy_example = main.buy()
    def mainProtocol(self):
        for _ in range(500):
            self.sale_example.add(randint(0,1000), randint(0,1000))
            self.buy_example.add(randint(0,1000), randint(0,1000))
    
    def test_launchThread(self):
        for _ in range(100):
            thr = threading.Thread(target=self.mainProtocol, name="addThread")
            thr.run()
        # while threading.active_count() != 1:
        #     time.sleep(5)
    def test_sale_viewSorting(self):
        expected = self.sale_example.view()
        for k in range(len(expected)-1):
            if bool(expected[k][1]):
                self.assertLessEqual(expected[k][1], expected[k+1][1])

    def test_buy_viewSorting(self):
        expected = self.buy_example.view()
        for k in range(len(expected)-1):
            if bool(expected[k][1]):
                self.assertLessEqual(expected[k][1], expected[k+1][1])

if __name__ == "__main__":
    unittest.main()