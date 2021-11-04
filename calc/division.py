"""Division"""

from calc.calculation import Calculation

class Division(Calculation):
    """something"""
    def get_result(self):
        """idk"""
        try:
            return self.value_a / self.value_b
        except ZeroDivisionError:
            return "Can't divide by zero"
