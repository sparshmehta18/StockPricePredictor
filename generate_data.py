import pandas as pd
import numpy as np

dates = pd.date_range(start='1/1/2010', end=pd.Timestamp.today().normalize())
for sym in ['FB', 'GOOG']:
    df = pd.DataFrame({
        'ID': range(len(dates)),
        'symbol': [sym] * len(dates),
        'Date': dates,
        'open': np.random.uniform(50, 150, size=len(dates)),
        'High': np.random.uniform(50, 150, size=len(dates)),
        'Low': np.random.uniform(50, 150, size=len(dates)),
        'Close': np.random.uniform(50, 150, size=len(dates)),
        'Volume': np.random.uniform(1000, 10000, size=len(dates)),
        'Adj_Close': np.random.uniform(50, 150, size=len(dates)),
        'Return_Out': np.random.uniform(-0.05, 0.05, size=len(dates)),
    })
    df.to_csv(f'input/{sym}.csv', index=False)
