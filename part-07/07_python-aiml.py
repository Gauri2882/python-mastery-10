' Project: AI Chatbot with NLP '

import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline

# Download NLTK resources
nltk.download("punkt")
nltk.download("stopwords")
nltk.download('punkt_tab')  # Add this line to download the missing resource

# Preprocessing function
def clean_text(text):
    if not text or not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    try:
        tokens = word_tokenize(text)
        tokens = [word for word in tokens if word not in stopwords.words("english")]
        return " ".join(tokens)
    except:
        return text  # Fallback to original text if tokenization fails

# Rule-Based Responses
def simple_chatbot(user_input):
    user_input = clean_text(user_input)
    
    responses = {
        "hello": "Hi there! How can I assist you?",
        "hi": "Hi there! How can I assist you?",
        "how are you": "I'm doing great! How about you?",
        "bye": "Goodbye! Have a wonderful day!",
        "goodbye": "Goodbye! Have a wonderful day!",
        "thanks": "You're welcome! Let me know if you need anything else.",
        "thank you": "You're welcome! Let me know if you need anything else."
    }
    
    for key in responses:
        if key in user_input:
            return responses[key]
    
    return None  # Return None if no rule-based response is found

# Load AI-Powered Chatbot
try:
    chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")
except Exception as e:
    print(f"Error loading AI model: {e}")
    chatbot = None

def ai_chatbot(user_input):
    if not chatbot:
        return "I'm having technical difficulties. Please try again later."
    
    try:
        response = chatbot(user_input, max_length=100, num_return_sequences=1, truncation=True)
        return response[0]["generated_text"]
    except Exception as e:
        print(f"AI generation error: {e}")
        return "I'm not sure how to respond to that."

# Main Chatbot Function
def chatbot_system():
    print("Chatbot: Hello! Type 'exit' to stop.")
    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! 👋")
            break
        
        # First try rule-based responses
        response = simple_chatbot(user_input)
        
        # If no rule-based response, use AI
        if response is None and chatbot:
            response = ai_chatbot(user_input)
        elif response is None:
            response = "I'm not sure I understand. Can you rephrase?"
        
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot_system()