import pandas as pd
import nltk
import gensim
from nltk.tokenize import word_tokenize
from gensim.parsing.preprocessing import remove_stopwords
import pyLDAvis
from pyLDAvis import gensim_models
import re

df = pd.read_csv("social_media_data.csv")

def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]','',text)
    text = remove_stopwords(text)
    words = word_tokenize(text)
    return words

df['text'] = df['text'].apply(preprocess)

dictionary = gensim.corpora.Dictionary(df['text'])
corpus = [dictionary.doc2bow(text) for text in df['text']]

num_topics = 5
model = gensim.models.LdaModel(corpus=corpus,id2word=dictionary,num_topics=num_topics)

print(model.print_topics())

vis = pyLDAvis.gensim_models.prepare(model,corpus,dictionary)
pyLDAvis.save_html(vis,'tp.html')


