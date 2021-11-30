"""Testing the Calculator"""
import pytest
import pandas as pd
import main

@pytest.fixture(name="clear_history",autouse=True)
def fixture_clear_history():
    '''clear history function'''
    Calculator.clear_history()

def test_logging():
    main.logging()


