
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load job dataset
df = pd.read_csv("data/jobs.csv")

# Combine job title and skills
df["job_info"] = df["job_title"] + " " + df["skills"]

# Convert text into numerical features
vectorizer = TfidfVectorizer()
job_vectors = vectorizer.fit_transform(df["job_info"])

# Save model data
with open("models/career_model.pkl", "wb") as file:
    pickle.dump((df, vectorizer, job_vectors), file)

print("Career recommendation model trained successfully!")
