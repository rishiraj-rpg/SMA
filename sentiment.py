import numpy as np
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sentiment.csv")
print(df)

positive=0
negative=0
neutral =0
for i in (df['text']):
    num = TextBlob(i).sentiment.polarity
    if num>0: positive+=1
    elif num<0: negative+=1
    elif num==0: neutral+=1

print("Positive ",positive)
print("Negative ",negative)
print("Neutral ",neutral)

classes = ["Positive","Negative","Neutral"]
values = [positive,negative,neutral]

# plt.bar(classes,values)
# plt.show()
#
# sns.scatterplot(x=classes,y=values)
# plt.show()

# plt.plot(classes,values)
# plt.show()

# plt.pie(values,labels=classes)
# plt.show()

# sns.kdeplot(values)
# plt.show()

# vlaues=[1,1,1,1,2,2,2,2,3]
# plt.hist(vlaues)
# plt.show()
