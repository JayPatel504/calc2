"""Testing the Calculator"""
import pytest

from calculator.calculator import Calculator

@pytest.fixture(name="clear_history",autouse=True)
def fixture_clear_history():
    '''clear history function'''
    Calculator.add_numbers((1,2))
    yield
    Calculator.clear_history()

def test_get_result_of_first_calculation_added_to_history():
    '''test to get result of first calc'''
    assert Calculator.get_result_of_first_calculation_added_to_history() == 3.0

def test_clear_history():
    '''test to clear history'''
    assert Calculator.clear_history()
    assert Calculator.history_count() == 0

def test_get_last_calculation():
    '''test to get last calc'''
    assert Calculator.get_last_calculation().get_result() == 3.0

def test_get_first_calculation():
    '''test to get first calc'''
    assert Calculator.get_first_calculation().get_result() == 3.0

def test_history_count():
    '''test to count history'''
    assert Calculator.history_count() == 1

def test_add_calculation():
    '''test for add calc to list'''
    assert Calculator.history_count() == 1

def test_get_result_of_last_calculation_added_to_history():
    '''test to get result of last calc'''
    assert Calculator.get_result_of_last_calculation_added_to_history() == 3.0

def test_get_calculation_object():
    '''test to get object'''
    assert Calculator.get_calculation_object(0).get_result() == 3.0

def test_add_number():
    """Testing the Add function of the calculator"""
    Calculator.add_numbers((1,2,3,4))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 10.0

def test_subtract_numbers():
    """Testing the subtract method of the calculator"""
    Calculator.subtract_numbers((10,7))
    assert Calculator.get_result_of_last_calculation_added_to_history() == -17.0

def test_multiply_numbers():
    """ tests multiplication of two numbers"""
    Calculator.multiply_numbers((2,2,2))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 8.0

def test_divide_numbers():
    """ tests division of two numbers"""
    Calculator.divide_numbers((2,2))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 1.0
    Calculator.divide_numbers((2,0))
    assert Calculator.get_result_of_last_calculation_added_to_history() == "Can't divide by zero"
