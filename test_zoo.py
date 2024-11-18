import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    # Add your additional test cases here.
    def test_child_ticket_price_1(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)
    def test_child_ticket_price_2(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_child_ticket_price_3(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_child_ticket_price_4(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_child_ticket_price_5(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)

if __name__ == '__main__':
    unittest.main()