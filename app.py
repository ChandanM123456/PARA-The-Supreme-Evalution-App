from flask import Flask, request, jsonify
from medbert_model import load_model, predict_health

app = Flask(__name__)

model, tokenizer = load_model()

@app.route("/predict-health", methods=["POST"])
def predict():
    data = request.json
    if not data:
        return jsonify({"error": "No data provided"}), 400

    score, condition, challenge = predict_health(model, tokenizer, data)
    return jsonify({
        "score": score,
        "condition": condition,
        "challenge": challenge
    })

if __name__ == "__main__":
    app.run(debug=True)
