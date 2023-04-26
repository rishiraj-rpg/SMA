import numpy as np
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('trend_analysis.csv')
print(df)

df['date'] = pd.to_datetime(df['date'])
df.set_index('date',inplace=True)
daily_counts = df.resample('D').count()
print(daily_counts)

# plt.plot(daily_counts)
# plt.show()

plt.bar(daily_counts.index,daily_counts['id'])
plt.show()