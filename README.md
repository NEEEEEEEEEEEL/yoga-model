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
2. Set up the environment
It's recommended to use a virtual environment. To create and activate a virtual environment, run the following:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3. Install dependencies
Install the required Python libraries using pip:

bash
Copy code
pip install -r requirements.txt
Ensure your requirements.txt includes the following dependencies:

makefile
Copy code
transformers==4.31.0
torch==2.0.0
4. Run the program
After installing the dependencies, you can run the program with:

bash
Copy code
python app.py
The program will prompt you for input and suggest a yoga routine based on your mood.

Code Overview
1. Sentiment Analysis
We use the transformers library from Hugging Face to load a pre-trained sentiment analysis model:

python
Copy code
from transformers import pipeline
sentiment_analyzer = pipeline("sentiment-analysis")
This model classifies input text into three sentiment categories: positive, neutral, or negative.

2. Yoga Routine Mapping
Yoga routines are predefined for each sentiment (positive, neutral, and negative). The system recommends specific poses based on the detected sentiment:

python
Copy code
yoga_routines = {
    "positive": ["Sun Salutations (Surya Namaskar)", "Backbends (e.g., Cobra Pose)", "Warrior Poses"],
    "neutral": ["Seated Forward Bend (Paschimottanasana)", "Cat-Cow Stretch (Marjaryasana-Bitilasana)", "Tree Pose (Vrikshasana)"],
    "negative": ["Child's Pose (Balasana)", "Legs-Up-The-Wall Pose (Viparita Karani)", "Corpse Pose (Savasana)"]
}
3. Recommendation Logic
The function recommend_yoga_routine() analyzes the sentiment of the user's input and maps it to the corresponding yoga routine:

python
Copy code
def recommend_yoga_routine(user_text):
    sentiment = sentiment_analyzer(user_text)[0]
    label = sentiment["label"].lower()

    if "positive" in label:
        return yoga_routines["positive"]
    elif "negative" in label:
        return yoga_routines["negative"]
    else:
        return yoga_routines["neutral"]
Example Usage
Input:
vbnet
Copy code
How are you feeling today?
> I'm feeling really good today!
Output:
sql
Copy code
Based on your mood, here are some yoga routines for you:
Sun Salutations (Surya Namaskar), Backbends (e.g., Cobra Pose), Warrior Poses
Input:
vbnet
Copy code
How are you feeling today?
> I'm feeling stressed and anxious.
Output:
rust
Copy code
Based on your mood, here are some yoga routines for you:
Child's Pose (Balasana), Legs-Up-The-Wall Pose (Viparita Karani), Corpse Pose (Savasana)
Model Information
The system uses a pre-trained sentiment analysis model from Hugging Face, which classifies the input text into one of the following categories:

POSITIVE: The user is in a good mood or feeling happy.
NEGATIVE: The user is feeling sad, stressed, or anxious.
NEUTRAL: The user's input doesn't convey a strong emotional tone.
Next Steps
Expand Yoga Routine Database: Add more yoga poses and routines for different emotional states or even provide dynamic recommendations based on the user's previous feedback.
Improve User Interaction: Implement options where the user can explicitly choose their mood (happy, sad, stressed) instead of typing a description.
Mobile App Integration: Integrate this system into a mobile app for real-time yoga routine recommendations.
User Feedback: Collect feedback from users to refine the yoga routines suggested and improve sentiment analysis accuracy.
License
This project is licensed under the MIT License - see the LICENSE file for details.
