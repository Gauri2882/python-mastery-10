' Project: Fake News Detector '

import pandas as pd
import numpy as np
import nltk 
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/lutzhamel/fake-news/refs/heads/master/data/fake_or_real_news.csv")

# download NLTK resources
# nltk.download("stopwords")
# nltk.download("punkt")

# preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(f"[^a-zA-Z0-9]", "", text)
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stopwords.words("english")]
    return " ".join(tokens)

df['cleaned_text'] = df['text'].apply(clean_text)

# converting text into numerical features
vectorizer = TfidfVectorizer(max_features= 5000)
X = vectorizer.fit_transform(df['cleaned_text'])
y = df['label'].map({'REAL':1, 'FAKE': 0}) # convert labels to binary (1 = real, 0 = fake)

# splitting data in training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

# training model 
model = LogisticRegression()
model.fit(X_train, y_train)

# evaluating model
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test,y_pred) * 100:.2f}%")
print(classification_report(y_test, y_pred))

# predict fake news 
def predict_news(news_text):
    cleaned_text = clean_text(news_text)
    vectorized_text = vectorizer.transform([cleaned_text])
    prediction = model.predict(vectorized_text)
    return "Real News" if prediction[0] == 1 else "Fake News"

# example test
news = "Breaking: Scientists discovered a new cure for cancer!"
print(f"Prediction: {predict_news(news)}")
