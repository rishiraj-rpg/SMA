import numpy as np
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('tweet_data.csv')
print(df)

dict = {}
for i in df['location']:
    if i not in dict.keys():
        dict[i]=1
    else: dict[i]+=1
print(dict)

plt.bar(dict.keys(),dict.values())
plt.show()