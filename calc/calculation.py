"""This is our calculation base class / Abstract Class"""
class Calculation:
    '''idk'''
    def __init__(self,value_a, value_b):
        self.value_a = value_a
        self.value_b = value_b

    @classmethod
    def create(cls, value_a, value_b):
        """idk"""
        return cls(value_a,value_b)

    @property
    def value_a(self):
        '''qwpifh'''
        return self.value_a
