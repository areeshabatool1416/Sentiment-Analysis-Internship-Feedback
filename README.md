# 💼 Sentiment Analysis of Internship Feedback

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikitlearn)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red?logo=streamlit)

An end-to-end **Machine Learning** and **Natural Language Processing (NLP)** project that analyzes internship feedback using **Logistic Regression** and **TF-IDF Vectorization**. The project includes an interactive **Streamlit** web application for real-time sentiment prediction.

## Live Demo

🌐 **Streamlit App:** https://sentiment-analysis-internship-feedback-jdufyxzlpjvyx5nka6hwx9.streamlit.app/

📂 **GitHub Repository:** https://github.com/areeshabatool1416/Sentiment-Analysis-Internship-Feedback/tree/main

## Application Preview

### Home Screen

![Home](images/home.png)

### Positive Prediction

![Positive](images/positive.png)

### Negative Prediction

![Negative](images/negative.png)

##  Project Overview

Understanding intern feedback is essential for improving internship programs and enhancing the overall learning experience.

This project uses Machine Learning and Natural Language Processing (NLP) techniques to analyze textual internship feedback and predict its sentiment. Reviews are cleaned, transformed into numerical features using TF-IDF Vectorization, and classified with a Logistic Regression model. The final model is deployed through an interactive Streamlit web application for real-time predictions.

##  Problem Statement

Organizations receive large amounts of textual feedback from interns. Manually reviewing every response is time-consuming and inconsistent.

This project automates the sentiment analysis process by classifying internship feedback, enabling organizations to quickly identify positive experiences.

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- NLTK
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Joblib
- Streamlit

##  Machine Learning Workflow

```
Employee Reviews Dataset
          │
          ▼
Exploratory Data Analysis (EDA)
          │
          ▼
Data Cleaning
          │
          ▼
Text Preprocessing
(Lowercase, Tokenization, Stopword Removal, Lemmatization)
          │
          ▼
TF-IDF Vectorization
          │
          ▼
Logistic Regression
          │
          ▼
Model Evaluation
          │
          ▼
Streamlit Deployment
```

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Model | Logistic Regression |
| Vectorizer | TF-IDF |
| Accuracy | 73.15% |
| Dataset Size | 67,529 Reviews |

##  Project Structure

```
Sentiment-Analysis-Internship-Feedback/
│
├── app/
│   └── app.py
│
├── data/
│   └── employee_reviews.csv
│
├── images/
│   ├── home.png
│   ├── positive.png
│   └── negative.png
│
├── models/
│   ├── logistic_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── notebooks/
│   └── Sentiment_Analysis.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
```

##  Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_LINK
```

Navigate into the project:

```bash
cd Sentiment-Analysis-Internship-Feedback
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app/app.py
```

## Future Improvements

- Improve sentiment classification performance.
- Experiment with transformer-based models such as BERT.
- Add confidence scores for predictions.
- Enhance the user interface with additional analytics.
- Support multilingual feedback analysis.

##  About the Author

**Areesha Batool**

Computer Science Student passionate about Artificial Intelligence, Machine Learning, and Data Science. I enjoy building end-to-end ML solutions that solve real-world problems and continuously expanding my technical skills through hands-on projects.

 Feel free to connect with me on LinkedIn!
https://www.linkedin.com/in/areesha-batool-667651262/
