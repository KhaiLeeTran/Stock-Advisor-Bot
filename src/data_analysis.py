import pandas as pd
import matplotlib.pyplot as plt

class DataAnalysis:
    def __init__(self, data_path: str):
        self._df = pd.read_csv(data_path)
    
    def create_df(self):
        self._df['Date'] = pd.to_datetime(self._df['Date'])
        self._df.set_index('Date', inplace=True)

        return self._df