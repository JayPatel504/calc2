"""Testing the CSV feature"""
import os
import pytest
import pandas as pd
import main
from calculator.calculator import Calculator

@pytest.fixture(name="clear_history",autouse=True)
def fixture_clear_history():
    '''clear history function'''
    Calculator.clear_history()

def test_logging():
    '''this tests the whole CSV process'''
    abs_path= os.path.dirname(os.path.abspath(__file__))
    temp = os.path.join(abs_path,'files')
    main.logging(temp,temp,False)
    temp1 = os.path.join(abs_path,'files-result/addition1-result.csv')
    d_f = pd.read_csv(temp1).to_numpy()
    contents=[]
    temp = os.path.join(abs_path,'results/addition1.csv_log.txt')
    with open(temp,encoding="utf-8") as f_f:
        contents=f_f.readlines()
    for i, line in enumerate(contents):
        assert float(line.split(',')[4][:-1]) == d_f[i]
