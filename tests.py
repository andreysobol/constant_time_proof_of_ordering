import unittest
from itertools import permutations
from functools import reduce
from order import OrderedElements, Element, insert_element

class UnitTest(unittest.TestCase):

    def test_hello_world(self):
        assert(True)

    def test_insert_first_el(self):
        oe = OrderedElements()
        self.assertEqual(len({}), len(oe.set))
        new = insert_element(oe, Element("name", 120))
        self.assertEqual(1, len(new.set))

    def test_insert_with_different_order(self):

        el1 = Element("el1", 1)
        el2 = Element("el2", 2)
        el3 = Element("el3", 3)
        el4 = Element("el4", 4)
        ps = permutations([el1, el2, el3, el4], 4)
        rs = [4, 3, 2, 1]

        for p in ps:
            oe = reduce(insert_element, p, OrderedElements())
            index = oe.max_element
            for r in rs:
                self.assertEqual(r, oe.set[index].value)
                index = oe.set[index].next

if __name__ == '__main__':
    unittest.main()