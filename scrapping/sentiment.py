# Import libraries
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
from wordcloud import STOPWORDS # need to update with more
import re
from matplotlib import style
style.use('ggplot')
stop_words = set(stopwords.words('english'))
import warnings
warnings.filterwarnings('ignore')


## READ CSV

df = pd.read_csv('scrapping/scraped_data.csv')

print(df.info())
