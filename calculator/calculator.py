""" This is the increment function"""

from calc.addition import Addition
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
from calc.division import Division

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        '''result of first entry'''
        return Calculator.history[0].get_result()
    @staticmethod
    def clear_history():
        '''clear list'''
        Calculator.history.clear()
        return True
    @staticmethod
    def get_last_calculation():
        '''get last calc'''
        return Calculator.history[-1]
    @staticmethod
    def get_first_calculation():
        '''get first calc'''
        return Calculator.history[0]
    @staticmethod
    def history_count():
        '''len(list)'''
        return len(Calculator.history)
    @staticmethod
    def get_history():
        '''return list'''
        return Calculator.history
    @staticmethod
    def add_calculation_to_history(calculation):
        '''add calculation object to list'''
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        '''get last result'''
        return Calculator.history[-1].get_result()
    @staticmethod
    def get_calculation_object(num):
        '''get specified object'''
        return Calculator.history[num]
    @staticmethod
    def add_number(*args):
        """ adds number to result"""
        addition = Addition(args)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def subtract_number(*args):
        """ subtract number from result"""
        subtraction = Subtraction(args)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def multiply_numbers(*args):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication(args))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers(*args):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division(args))
        return Calculator.get_result_of_last_calculation_added_to_history()
