# Sentiment Analysis Tool

A simple Python-based tool that analyzes the **sentiment** of text (positive, negative, or neutral) using:

-  **TextBlob** – rule-based sentiment scoring
-  **VADER** – tuned for social media and informal text
-  (Coming Soon) Custom **ML model** with `scikit-learn`

## Features

- Accepts user input or text files
- Detects sentiment polarity, subjectivity (TextBlob)
- Provides VADER sentiment scores (including compound)
- Optional web interface with Flask
- Clean and simple folder structure
- Easy to run and extend

## Setup Instructions

```bash
# Clone or download the repo
cd sentiment-analysis-tool

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # for Windows

# Install dependencies
pip install -r requirements.txt
