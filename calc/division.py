"""Division"""

from calc.calculation import Calculation

class Division(Calculation):
    """something"""
    def get_result(self):
        """idk"""
        dv_of_values = 0.0
        try:
            for v in self.value:
                dv_of_values/=v
            return dv_of_values
        except ZeroDivisionError:
            return "Can't divide by zero"
