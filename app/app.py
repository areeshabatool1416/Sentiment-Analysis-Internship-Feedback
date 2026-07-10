import streamlit as st
import joblib
import re
import string
import nltk
from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# Page Configuration

st.set_page_config(
    page_title="Internship Feedback Sentiment Analysis",
    page_icon="💼"
)

st.title("💼 Internship Feedback Sentiment Analysis")

st.write("""
This application predicts the sentiment of internship feedback
using a Logistic Regression model trained on employee reviews.
""")


# Download NLTK Resources

nltk.download("punkt")
nltk.download("punkt_tab")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")


# Load Model and Vectorizer

BASE_DIR = Path(__file__).resolve().parent.parent

model = joblib.load(BASE_DIR / "models" / "logistic_model.pkl")
tfidf = joblib.load(BASE_DIR / "models" / "tfidf_vectorizer.pkl")

# Initialize NLP Tools

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# Text Preprocessing Function

def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{re.escape(string.punctuation)}]", "", text)

    words = word_tokenize(text)
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)


# User Input

review = st.text_area("Enter Internship Feedback:")


# Prediction

if st.button("Predict Sentiment"):

    if review.strip() == "":
        st.warning("⚠️ Please enter internship feedback before predicting.")

    else:
        clean_review = clean_text(review)
        vector = tfidf.transform([clean_review])
        prediction = model.predict(vector)[0]

        st.write("### Your Feedback")
        st.write(review)

        st.write("### Prediction")

        if prediction == "Positive":
            st.success("😊 Positive Feedback")

        elif prediction == "Negative":
            st.error("😞 Negative Feedback")

        else:
            st.info("😐 Neutral Feedback")