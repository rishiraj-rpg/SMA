import numpy as np
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

df = pd.read_csv("tweet_data.csv")
print(df['id'])

hash_list=[]
for i in df['id']:
    hashtags = re.findall(r'\#\w+',i)
    # hashtags = hashtags[0]
    if len(hashtags)!=0:
        hash_list.append(hashtags[0])

print(hash_list)

dict = {}
for i in hash_list:
    if i not in dict.keys():
        dict[i]=1
    else: dict[i]+=1
print(dict)

plt.bar(dict.keys(),dict.values())
plt.show()
