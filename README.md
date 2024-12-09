# Sentiment Analysis-based Yoga Routine Recommendation System

This project provides a yoga routine recommendation system that suggests yoga poses based on the sentiment of user input. By analyzing the sentiment of the user's text (positive, neutral, or negative), the system recommends an appropriate yoga routine to match the user's emotional state. The sentiment analysis is powered by a pre-trained model from the Hugging Face Transformers library.

## Features

- **Sentiment Analysis**: Detects the sentiment (positive, neutral, or negative) from user input.
- **Yoga Routine Recommendation**: Maps the sentiment to a list of yoga poses.
- **Interactive Interface**: Prompts the user to enter their mood and responds with a customized yoga routine.

## How It Works

1. The user inputs a text describing how they feel (e.g., "I'm feeling happy" or "I'm stressed").
2. The system analyzes the sentiment of the input using a pre-trained sentiment analysis model.
3. Based on the sentiment (positive, neutral, or negative), the system recommends a set of yoga poses suited for that mood.

## Installation

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/yoga-sentiment-analysis.git
cd yoga-sentiment-analysis
