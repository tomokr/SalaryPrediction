import os
import pandas as pd

def load_data(path, filename):
    filepath = os.path.join(path, filename)
    return pd.read_csv(filepath)

def check_df(df):
    # NaN
    print('# of NaN')
    print(df.isna().sum())
    # Duplicate
    print('\n # of Duplicate')
    print(df.duplicated().sum())

def save_data(path, df, filename):
	filepath = os.path.join(path, filename)
	df.to_csv(filepath)