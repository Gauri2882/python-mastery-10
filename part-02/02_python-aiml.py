""" Project: Text Sentiment Analyzer """

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import tkinter as tk
from tkinter import messagebox

# Initialize VADER analyzer
analyzer = SentimentIntensityAnalyzer()

# Function using TextBlob
def analyze_sentiment_textblob():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text!")
        return
        
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        result = "Positive 😊"
    elif sentiment < 0:
        result = "Negative 😡"
    else:
        result = "Neutral 😐"
    
    result_label.config(text=f"TextBlob Result: {result}")

# Function using VADER
def analyze_sentiment_vader():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Warning", "Please enter some text!")
        return
        
    sentiment_score = analyzer.polarity_scores(text)["compound"]
    if sentiment_score >= 0.05:
        result = "Positive 😊"
    elif sentiment_score <= -0.05:
        result = "Negative 😡"
    else:
        result = "Neutral 😐"
    
    result_label.config(text=f"VADER Result: {result}")

# Create main window
root = tk.Tk()
root.title("Text Sentiment Analyzer")
root.geometry("400x300")

# Widgets
label = tk.Label(root, text="Enter your text below:", font=("Arial", 14))
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

button_txtblob = tk.Button(frame, text="Analyze with TextBlob", command=analyze_sentiment_textblob)
button_txtblob.pack(side=tk.LEFT, padx=5)

button_vader = tk.Button(frame, text="Analyze with VADER", command=analyze_sentiment_vader)
button_vader.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()