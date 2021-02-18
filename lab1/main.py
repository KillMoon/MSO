import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

if __name__ == '__main__':
    data = pd.read_csv('BankChurners.csv', delimiter=',')
    print(data.head())
