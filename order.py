from __future__ import annotations


class Element():
    
    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        self.next = None

    def copy(self) -> self:
        new = type(self)(self.name, self.value)
        new.next = self.next
        return new


class OrderedElements():

    def __init__(self):
        self.set = {}
        self.last_key = 0
        self.max_element = None

    def copy(self) -> self:
        new = type(self)()
        new.set = self.set.copy()
        new.last_key = self.last_key
        new.max_element = self.max_element
        return new


class InsertProof():

    def __init__(
        self,
        element_index: int,
        value: int,
        prev: int,
        current: int,
        replace_next_index: int,
        replace_next: int,
        max_element: int,
        last_key: int,
    ):
        self.element_index = element_index
        self.value = value
        self.prev = prev
        self.current = current
        self.replace_next_index = replace_next_index
        self.replace_next = replace_next
        self.max_element = max_element
        self.last_key = last_key


def insert_element(ordered_elements: OrderedElements, element: Element) -> OrderedElements:
    new_key = ordered_elements.last_key + 1
    if ordered_elements.max_element == None:
        new_element = element.copy()
        new_element.next = None
        new_ordered_elements = ordered_elements.copy()
        new_ordered_elements.set[new_key] = new_element
        new_ordered_elements.last_key = new_key
        new_ordered_elements.max_element = new_key
    else:

        def find_element(
            prev: int,
            current: int,
            ordered_elements: OrderedElements,
            value:int
        ) -> (int, int):
            if ordered_elements.set[current].value < value :
                return (prev, current)
            else:
                if ordered_elements.set[current].next == None:
                    return (current, None)
                else:
                    c = ordered_elements.set[current].next
                    p = current
                    return find_element(p, c, ordered_elements, value)

        (prev, current) = find_element(None, ordered_elements.max_element, ordered_elements, element.value)

        new_element = element.copy()
        new_element.next = current

        new_ordered_elements = ordered_elements.copy()
        new_ordered_elements.set[new_key] = new_element
        new_ordered_elements.last_key = new_key

        if prev != None :
            new_ordered_elements.set[prev].next = new_key
        else:
            new_ordered_elements.max_element = new_key

    return new_ordered_elements


def find_insert_proof(ordered_elements: OrderedElements, element: Element) -> InsertProof:

    last_key = ordered_elements.last_key + 1
    element_index = last_key

    value = element.value

    if ordered_elements.max_element == None:
        #new_element = element.copy()
        #new_element.next = None
        #new_ordered_elements = ordered_elements.copy()
        #new_ordered_elements.set[new_key] = new_element
        #new_ordered_elements.last_key = new_key
        prev = None
        current = None
    else:

        def find_element(
            prev: int,
            current: int,
            ordered_elements: OrderedElements,
            value:int
        ) -> (int, int):
            if ordered_elements.set[current].value < value :
                return (prev, current)
            else:
                if ordered_elements.set[current].next == None:
                    return (current, None)
                else:
                    c = ordered_elements.set[current].next
                    p = current
                    return find_element(p, c, ordered_elements, value)

        (prev, current) = find_element(None, ordered_elements.max_element, ordered_elements, element.value)

        #new_element = element.copy()
        #new_element.next = current

        #new_ordered_elements = ordered_elements.copy()
        #new_ordered_elements.set[new_key] = new_element
        #new_ordered_elements.last_key = new_key

    if prev != None :
        replace_next_index = prev
        replace_next = element_index
        max_element = ordered_elements.max_element
        #new_ordered_elements.set[prev].next = new_key
    else:
        replace_next_index = None
        replace_next = None
        max_element = element_index

    return InsertProof(
        element_index = element_index,
        value = value,
        prev = prev,
        current = current,
        replace_next_index = replace_next_index,
        replace_next = replace_next,
        max_element = max_element,
        last_key = last_key,
    )


def apply_insert_proof(
    ordered_elements: OrderedElements,
    insert_proof: InsertProof,
    name: str
) -> OrderedElements:
    
    new_ordered_elements = ordered_elements.copy()
    new_element = Element(name, insert_proof.value)
    new_element.next = insert_proof.current
    new_ordered_elements.set[insert_proof.element_index] = new_element

    if insert_proof.replace_next_index != None:
        replaced_element = new_ordered_elements.set[insert_proof.replace_next_index].copy()
        replaced_element.next = insert_proof.replace_next
        new_ordered_elements.set[insert_proof.replace_next_index] = replaced_element

    new_ordered_elements.max_element = insert_proof.max_element
    new_ordered_elements.last_key = insert_proof.last_key


def check_insert_proof(ordered_elements: OrderedElements, insert_proof: InsertProof) -> (bool, [str]):

    '''
    condition:

    element_index == oe.last_key + 1

    new_last_key = element_index

    if current != None
        oe.set[current].value < value

    if prev != None:
        oe.set[prev].value >= value

    if prev == None:
        new_max_element == element_index

    if prev != None:
        oe.max_element == new_max_element

    if prev != None:
        replace_next_index = prev
        replace_next == element_index
    else:
        replace_next_index = None
        replace_next = None

    if prev != None:
        oe.set[prev].next = current

    apply value name current
    '''
    conditions = [
        (
            insert_proof.element_index == ordered_elements.last_key + 1,
            "Incorrect element_index",
        ),
        (
            insert_proof.last_key == insert_proof.element_index,
            "Incorrect last_key",
        ),
        (
            (insert_proof.current == None) or 
            (insert_proof.value > ordered_elements.set[insert_proof.current].value),
            "Incorrect current position",
        ),
        (
            (insert_proof.prev == None) or 
            (insert_proof.value <= ordered_elements.set[insert_proof.prev].value),
            "Incorrect prev position",
        ),
        (
            (insert_proof.prev != None) or 
            (insert_proof.element_index == insert_proof.max_element),
            "Non replaced max_element",
        ),
        (
            (insert_proof.prev == None) or 
            (ordered_elements.max_element == insert_proof.max_element),
            "Replaced max_element",
        ),
        (
            (insert_proof.replace_next_index == insert_proof.prev),
            "Incorrect replace_next_index",
        ),
        (
            (insert_proof.prev == None) or 
            (insert_proof.replace_next == insert_proof.element_index),
            "Incorrect replace_next_value",
        ),
        (
            (insert_proof.prev != None) or 
            (insert_proof.replace_next == None),
            "Non null replace_next_value",
        ),
        (
            (insert_proof.prev == None) or 
            (insert_proof.current == ordered_elements.set[insert_proof.prev].next),
            "Incorrect prev.next",
        ),
    ]

    return (
        all([i[0] for i in conditions]),
        [i[1] for i in conditions if not i[0]]
    )