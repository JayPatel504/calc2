"""Division Class"""

from calc.calculation import Calculation

class Division(Calculation):
    """division calculation object"""
    def get_result(self):
        """get the division results"""
        dv_of_values = self.values[0]
        try:
            for i, v_suck in enumerate(self.values):
                if i==0:
                    continue
                dv_of_values/=v_suck
            return dv_of_values
        except ZeroDivisionError:
            return "Can't divide by zero"
