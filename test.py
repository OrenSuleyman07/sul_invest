import threading
import unittest
from random import randint
from collections import namedtuple
import main

class case(unittest.TestCase):
    request_tuple = namedtuple('Request', 'Quantity Price')

    def AddItems(self, quantity, glass, type):
        example = glass
        count = 0
        while count<quantity and (type == 'addThread' or type == 'viewThread'):
            # sale_dict[count] = (self.request_tuple(randint(0,1000),randint(0,1000)))
            request_id, actual, expected = example.add(randint(0,1000),randint(0,1000))
            self.assertEqual(actual, expected)
            count += 1
        if type == 'viewThread':
            count = 0
            checklist = example.view()                
            while count<quantity-1:
                self.assertLessEqual(checklist[count][1], checklist[count+1][1])
                count += 1
        while count<quantity and type == 'voidThread':
            request_id, actual, expected = example.add(randint(0,1000), '')
            self.assertEqual(actual, expected)
            count += 1
 
    # add tests 
    def test_sale_AddItems(self):
        thr = threading.Thread(target=self.AddItems, args=(100, main.sale(), 'addThread'), name='saleAddThread')
        thr.run()

    def test_buy_addItems(self):
        thr = threading.Thread(target=self.AddItems, args=(100, main.buy(), 'addThread'), name='buyAddThread')
        thr.run()
    # view tests
    def test_sale_viewItems(self):
        thr = threading.Thread(target=self.AddItems, args=(100, main.sale(), 'viewThread'), name='saleViewThread')
        thr.run()

    def test_buy_viewItems(self):
        thr = threading.Thread(target=self.AddItems, args=(100, main.buy(), 'viewThread'), name='buyViewThread')
        thr.run()
    # void price tests
    def test_sale_voidPrice(self):
        thr = threading.Thread(target=self.AddItems, args=(100, main.sale(), 'voidThread'), name='saleVoidThread')
        thr.run()
    
    def test_buy_voidPrice(self):
        thr = threading.Thread(target=self.AddItems, args=(100, main.buy(), 'voidThread'), name='buyVoidThread')
        thr.run()

# test = case()

if __name__ == "__main__":
    unittest.main()