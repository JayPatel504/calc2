"""Testing the Calculator"""
import pytest
import pandas as pd

from calculator.calculator import Calculator

@pytest.fixture(name="clear_history",autouse=True)
def fixture_clear_history():
    '''clear history function'''
    Calculator.clear_history()

def test_add_number():
    """Testing the Add function of the calculator"""
    df = pd.read_csv('./files/addition1.csv').to_numpy()
    for i in range(1,len(df)):
        Calculator.add_numbers(tuple(df[i][:-1]))
        assert Calculator.get_last_calculation().get_result() == df[i][-1]

def test_subtract_numbers():
    """Testing the subtract method of the calculator"""
    df = pd.read_csv('./files/subtraction1.csv').to_numpy()
    for i in range(1,len(df)):
        Calculator.subtract_numbers(tuple(df[i][:-1]))
        assert Calculator.get_last_calculation().get_result() == df[i][-1]

def test_multiply_numbers():
    """ tests multiplication of two numbers"""
    df = pd.read_csv('./files/multiplication1.csv').to_numpy()
    for i in range(1,len(df)):
        Calculator.multiply_numbers(tuple(df[i][:-1]))
        assert Calculator.get_last_calculation().get_result() == df[i][-1]

def test_divide_numbers():
    """ tests division of two numbers"""
    df = pd.read_csv('./files/division1.csv').to_numpy()
    for i in range(1,len(df)):
        Calculator.divide_numbers(tuple(df[i][:-1]))
        assert Calculator.get_last_calculation().get_result() == df[i][-1]
