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
    def get_last_calculation_object():
        '''get last object'''
        return Calculator.history[-1]
    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        addition = Addition.create(value_a,value_b)
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        subtraction = Subtraction.create(value_a, value_b)
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()

    @staticmethod
    def divide_numbers(value_a, value_b):
        """ divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
