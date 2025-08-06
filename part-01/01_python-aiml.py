""" Project: Spam Email Detector """

import pandas as pd
import numpy as np
import re
import nltk # natural language toolkit
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer # to reduce words to the root forms eg. running -> run
from sklearn.feature_extraction.text import TfidfVectorizer # convert text into numerical data so ML model can understand
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# download stopwords
nltk.download("stopwords")
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))

# load dataset
df = pd.read_csv("part-01/spam.csv", encoding = "latin-1")[['v1', 'v2']]
df.columns = ['label', 'message']
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# text processing
def preprocess_text(text):
    text = re.sub(r"\W", " ", text) # remove special characters
    text = text.lower()
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words] # remove stopwords and stem words
    return " ".join(words)

df['cleaned_message'] = df['message'].apply(preprocess_text)
print(df.head())

# converting text into numerical data
vectorizer = TfidfVectorizer(max_features= 3000)
X = vectorizer.fit_transform(df['cleaned_message'])
y = df['label']

# train-test splitting
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

# model training
model = LogisticRegression()
model.fit(X_train, y_train)

# evaluation
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) * 100 :.2f}")
print(classification_report(y_test, y_pred))

# custom email
def predict_email(email_text):
    processed_text = preprocess_text(email_text)
    vectorized_text = vectorizer.transform([processed_text])
    prediction = model.predict(vectorized_text)
    return "Spam" if prediction[0] == 1 else "Not Spam"

# example
email = "Congratulations! You've won a free iPhone. Click here to claim now."
print(f"Email {email}\nPrediction: {predict_email(email)}")