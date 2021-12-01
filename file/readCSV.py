'''Read CSV and performs operation'''
#pylint: disable=E0401,E1136,E0213,E1135,C0103
import pandas as pd
from calculator.calculator import Calculator

class Reading:
    '''Reading Class'''
    def read(file_path):
        '''Read CSV and find what operation is needed'''
        data = pd.read_csv(file_path).to_numpy()
        Calculator.clear_history()
        if "add" in file_path:
            return Reading.data_add(data)
        if "sub" in file_path:
            return Reading.data_sub(data)
        if "multi" in file_path:
            return Reading.data_multi(data)
        return Reading.data_div(data)

    def data_add(data):
        '''Add rows'''
        for row in enumerate(data):
            Calculator.add_numbers(tuple(row[1]))
        return "add",Calculator.history

    def data_sub(data):
        '''Subtract rows'''
        for row in enumerate(data):
            Calculator.subtract_numbers(tuple(row[1]))
        return 'subtract',Calculator.history

    def data_multi(data):
        '''Multiply rows'''
        for row in enumerate(data):
            Calculator.multiply_numbers(tuple(row[1]))
        return 'multiply',Calculator.history

    def data_div(data):
        '''Divide rows'''
        for row in enumerate(data):
            Calculator.divide_numbers(tuple(row[1]))
        return 'divide',Calculator.history
