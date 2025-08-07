" Project: Simple Recommendation System "

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset
data = {
    "Book": ["Python Crash Course", "Machine Learning for Beginners", "Deep Learning Fundamentals",
             "Data Science Handbook", "Artificial Intelligence Guide"],
    "Category": ["Programming", "Machine Learning", "Deep Learning", "Data Science", "AI"]
}

df = pd.DataFrame(data)

# Content-Based Filtering
vectorizer = TfidfVectorizer()
category_vectors = vectorizer.fit_transform(df["Category"])
similarity_matrix = cosine_similarity(category_vectors)

def recommend_books(book_name):
    if book_name not in df["Book"].values:
        return "Book not found!"
    
    index = df[df["Book"] == book_name].index[0]
    scores = list(enumerate(similarity_matrix[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    recommendations = [df["Book"][i] for i, _ in scores[1:3]]
    return recommendations

# Collaborative Filtering
user_ratings = {
    "User": ["Alice", "Bob", "Charlie", "David"],
    "Python Crash Course": [5, 3, 0, 4],
    "Machine Learning for Beginners": [4, 0, 5, 2],
    "Deep Learning Fundamentals": [0, 5, 4, 3],
    "Data Science Handbook": [2, 4, 3, 5],
    "Artificial Intelligence Guide": [5, 3, 0, 4]
}

ratings_df = pd.DataFrame(user_ratings).set_index("User")
user_similarity = cosine_similarity(ratings_df.fillna(0))
np.fill_diagonal(user_similarity, 0)
user_sim_df = pd.DataFrame(user_similarity, index=ratings_df.index, columns=ratings_df.index)

def recommend_for_user(user):
    if user not in ratings_df.index:
        return "User not found!"
    
    similar_users = user_sim_df[user].sort_values(ascending=False).index[0]
    recommended_books = ratings_df.loc[similar_users][ratings_df.loc[similar_users] == 5].index.tolist()
    
    return recommended_books

# Test the recommendation system
print("Content-Based Recommendation for 'Python Crash Course':", recommend_books("Python Crash Course"))
print("User-Based Recommendation for Charlie:", recommend_for_user("Charlie"))