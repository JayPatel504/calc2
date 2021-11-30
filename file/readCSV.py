import pandas as pd
from calculator.calculator import Calculator

class Reading:
    def read(p):
        df = pd.read_csv(p).to_numpy()
        Calculator.clear_history()
        if "add" in p:
            return Reading.df_add(df)
        elif "sub" in p:
            return Reading.df_sub(df)
        elif "multi" in p:
            return Reading.df_multi(df)
        elif "div" in p:
            return Reading.df_div(df)
    
    def df_add(df):
        for i in range(len(df)):
            Calculator.add_numbers(tuple(df[i]))
        return "add",Calculator.history
   
    def df_sub(df):
        for i in range(len(df)):
            Calculator.subtract_numbers(tuple(df[i]))
        return 'subtract',Calculator.history
    
    def df_multi(df):
        for i in range(len(df)):
            Calculator.multiply_numbers(tuple(df[i]))
        return 'multiply',Calculator.history
    
    def df_div(df):
        for i in range(len(df)):
            Calculator.divide_numbers(tuple(df[i]))
        return 'divide',Calculator.history
