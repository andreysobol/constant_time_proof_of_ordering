import unittest
from order import OrderedElements, Element, insert_element

class UnitTest(unittest.TestCase):

    def test_hello_world(self):
        assert(True)

    def test_insert_first_el(self):
        oe = OrderedElements()
        self.assertEqual(len({}), len(oe.set))
        new = insert_element(oe, Element("name", 120))

if __name__ == '__main__':
    unittest.main()