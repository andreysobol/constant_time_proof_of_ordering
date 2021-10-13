class Element():
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next = None

    def copy(self):
        new = type(self)(self.name, self.value)
        new.next = self.next
        return new

class OrderedElements():

    def __init__(self):
        self.set = {}
        self.last_key = 0
        self.max_element = None

    def copy(self):
        new = type(self)()
        new.set = self.set.copy()
        new.last_key = self.last_key
        new.max_element = self.max_element
        return new

def insert_element(ordered_elements, element):
    new_key = ordered_elements.last_key + 1
    if ordered_elements.max_element == None:
        new_element = element.copy()
        new_element.next = None
        new_ordered_elements = ordered_elements.copy()
        new_ordered_elements.set[new_key] = new_element
        new_ordered_elements.last_key = new_key
        new_ordered_elements.max_element = new_key
    else:
        def find_element(prev, current, ordered_elements, value):
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