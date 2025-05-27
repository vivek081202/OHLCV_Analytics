# utils/data_loader.py
import pandas as pd
import ast

def load_tsla_data(path: str = '../data/TSLA_data.csv'):
    df = pd.read_csv(path)

    # Convert support/resistance string lists to actual lists of floats
    df['Support'] = df['Support'].apply(lambda x: list(map(float, ast.literal_eval(x))) if pd.notna(x) else [])
    df['Resistance'] = df['Resistance'].apply(lambda x: list(map(float, ast.literal_eval(x))) if pd.notna(x) else [])
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.sort_values(by='timestamp')
    df.reset_index(drop=True, inplace=True)
    return df
