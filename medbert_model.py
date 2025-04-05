import torch
from transformers import BertTokenizer, BertModel

def load_model():
    model = torch.load("model_files/medbert_model.pt", map_location=torch.device('cpu'))
    model.eval()
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    return model, tokenizer

def preprocess_input(data):
    text = f"BP: {data['physical']['bloodPressure']}, Sugar: {data['physical']['sugar']}, HeartRate: {data['physical']['heartRate']}, Depression: {data['mental']['currentDepression']}, Anxiety: {data['mental']['anxiety']}"
    return text

def predict_health(model, tokenizer, user_data):
    text = preprocess_input(user_data)
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model(**inputs)
    score = torch.sigmoid(outputs.last_hidden_state.mean()).item() * 100

    condition = "Excellent" if score >= 85 else "Good" if score >= 70 else "Moderate" if score >= 50 else "Poor"
    challenge = {
        "name": "41-Day Challenge",
        "goals": ["Build mental clarity", "Enhance physical fitness", "Practice discipline"],
        "tasks": ["Meditate 10 mins", "Read 5 pages", "Gratitude journaling", "Workout 15 mins"]
    }

    return round(score, 2), condition, challenge
