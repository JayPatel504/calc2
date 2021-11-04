"""Testing the Calculator"""
import pprint

import pytest

from calculator.calculator import Calculator
from calc.addition import Addition

@pytest.fixture
def clear_history():
    '''clear history function'''
    Calculator.clear_history()

def test_add_calculation_to_history(clear_history):
    '''test for add calc to list'''
    Calculator.add_calculation_to_history(Addition.create(3,2))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_last_calculation(clear_history):
    '''test to get last calc'''
    Calculator.add_number(1,2)
    Calculator.add_number(2, 2)
    Calculator.add_number(3, 2)
    assert Calculator.get_last_calculation().get_result() == 5

def test_get_last_calculation_object(clear_history):
    '''test to get last object'''
    Calculator.add_number(1,2)
    Calculator.add_number(2, 2)
    Calculator.add_number(3, 2)
    assert Calculator.get_last_calculation_object().get_result() == 5

def test_get_first_calculation(clear_history):
    '''test to get first calc'''
    Calculator.add_number(1,2)
    Calculator.add_number(2, 2)
    Calculator.add_number(3, 2)
    assert Calculator.get_first_calculation().get_result() == 3

def test_add_number(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    '''test to clear history'''
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() #== True
    assert Calculator.history_count() == 0

def test_history_count(clear_history):
    '''test to count history'''
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2

def test_get_history():
    '''test to get history'''
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(6, 2) == 8
    assert Calculator.get_history() == Calculator.history

def test_get_result_of_last_calculation_added_to_history(clear_history):
    '''test to get result of last calc'''
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_result_of_first_calculation_added_to_history(clear_history):
    '''test to get result of first calc'''
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2

def test_calculator_divide(clear_history):
    """ tests division of two numbers"""
    assert Calculator.divide_numbers(2,2) == 1
