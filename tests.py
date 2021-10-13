import unittest
from itertools import permutations
from functools import reduce
from order import OrderedElements, Element, InsertProof, insert_element, check_insert_proof, find_insert_proof, apply_insert_proof

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
    
    def test_check_insert_proof_b(self):

        el2 = Element("el2", 2)
        el3 = Element("el3", 3)
        el4 = Element("el4", 4)
        el5 = Element("el5", 5)

        p = [el5, el4, el3, el2]
        oe = reduce(insert_element, p, OrderedElements())

        ip = InsertProof(
            element_index = 5,
            value = 1,
            prev = 4,
            current = None,
            replace_next_index = 4,
            replace_next = 5,
            max_element = 1,
            last_key = 5,
        )

        self.assertTrue(check_insert_proof(oe, ip)[0])

    def test_check_insert_proof_m(self):

        el1 = Element("el1", 1)
        el2 = Element("el2", 2)
        el4 = Element("el4", 4)
        el5 = Element("el5", 5)

        p = [el5, el4, el2, el1]
        oe = reduce(insert_element, p, OrderedElements())

        ip = InsertProof(
            element_index = 5,
            value = 3,
            prev = 2,
            current = 3,
            replace_next_index = 2,
            replace_next = 5,
            max_element = 1,
            last_key = 5,
        )

        self.assertTrue(check_insert_proof(oe, ip)[0])

    def test_check_insert_proof_e(self):

        el1 = Element("el1", 1)
        el2 = Element("el2", 2)
        el3 = Element("el3", 3)
        el4 = Element("el4", 4)

        p = [el4, el3, el2, el1]
        oe = reduce(insert_element, p, OrderedElements())

        ip = InsertProof(
            element_index = 5,
            value = 5,
            prev = None,
            current = 1,
            replace_next_index = None,
            replace_next = None,
            max_element = 5,
            last_key = 5,
        )

        self.assertTrue(check_insert_proof(oe, ip)[0])
    
    def test_check_insert_proof_wrong(self):

        el1 = Element("el1", 1)
        el2 = Element("el2", 2)
        el3 = Element("el3", 3)
        el4 = Element("el4", 4)

        p = [el4, el3, el2, el1]
        oe = reduce(insert_element, p, OrderedElements())

        ip = InsertProof(
            element_index = 1,
            value = 2,
            prev = 3,
            current = 4,
            replace_next_index = 5,
            replace_next = 6,
            max_element = 7,
            last_key = 8,
        )

        self.assertFalse(check_insert_proof(oe, ip)[0])
        self.assertEqual(len(check_insert_proof(oe, ip)[1]), 5)
    
    def test_insert_find_check_apply(self):

        el1 = Element("el1", 1)
        el2 = Element("el2", 2)
        el3 = Element("el3", 3)
        el4 = Element("el4", 4)
        ps = permutations([el1, el2, el3, el4], 4)

        for p in ps:
            oe = OrderedElements()
            for e in p:
                proof = find_insert_proof(oe, e)
                self.assertTrue(check_insert_proof(oe, proof)[0])
                apply_insert_proof(oe, proof, e.name)

if __name__ == '__main__':
    unittest.main()