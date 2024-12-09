from transformers import pipeline

sentiment_analyzer = pipeline(
    "sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


yoga_routines = {
    "positive": [
        "Sun Salutations (Surya Namaskar)",
        "Backbends (e.g., Cobra Pose)",
        "Warrior Poses"
    ],
    "neutral": [
        "Seated Forward Bend (Paschimottanasana)",
        "Cat-Cow Stretch (Marjaryasana-Bitilasana)",
        "Tree Pose (Vrikshasana)"
    ],
    "negative": [
        "Child's Pose (Balasana)",
        "Legs-Up-The-Wall Pose (Viparita Karani)",
        "Corpse Pose (Savasana)"
    ]
}


def recommend_yoga_routine(user_text):
    sentiment = sentiment_analyzer(user_text)[0]
    label = sentiment["label"].lower()

    if "positive" in label:
        return yoga_routines["positive"]
    elif "negative" in label:
        return yoga_routines["negative"]
    else:
        return yoga_routines["neutral"]


if __name__ == "__main__":
    user_input = input("How are you feeling today? ")
    recommended_routines = recommend_yoga_routine(user_input)

    print("\nBased on your mood, here are some yoga routines for you:")
    print(", ".join(recommended_routines))
