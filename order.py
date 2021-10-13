class Element():
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next_index = None

    def copy(self):
        new = type(self)()
        new.name = self.name
        new.value = self.value
        new.next_index = self.next_index
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