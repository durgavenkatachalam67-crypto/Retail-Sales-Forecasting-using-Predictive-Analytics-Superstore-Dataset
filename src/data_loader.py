import pandas as pd

def load_data(path=None):
    if path is None:
        path = r'C:\projects\predictive-analytics\data\raw\Sample - Superstore.csv'
    df = pd.read_csv(path, encoding='latin-1')
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])
    df.drop_duplicates(inplace=True)
    return df

def get_monthly_sales(df):
    df['YearMonth'] = df['Order Date'].dt.to_period('M')
    monthly = df.groupby('YearMonth')['Sales'].sum().reset_index()
    monthly['YearMonth'] = monthly['YearMonth'].dt.to_timestamp()
    monthly['Month_Num'] = range(len(monthly))
    return monthly