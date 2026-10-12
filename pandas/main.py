import pandas as pd
df = pd.read_csv('mckinsey.csv')

print(df['country'].value_counts())