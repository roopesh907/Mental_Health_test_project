from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
import joblib
from typing import List

app = Flask(__name__)

# Load the trained SVM model
model = joblib.load('svm_mental_health_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract 8 features from the form
        features = [
            int(request.form.get('feature1')),
            int(request.form.get('feature2')),
            int(request.form.get('feature3')),
            int(request.form.get('feature4')),
            int(request.form.get('feature5')),
            int(request.form.get('feature6')),
            int(request.form.get('feature7')),
            int(request.form.get('feature8')),
        ]

        # Convert to numpy array and reshape for prediction
        input_array = np.array(features).reshape(1, -1)

        # Predict using the model
        prediction = model.predict(input_array)[0]

        # Analyze inputs for custom recommendations
        tips = []
        if features[3] >= 2:  # Sleep-related
            tips.append("Try maintaining a regular sleep schedule and avoid screens before bedtime.")
        if features[5] >= 2:  # Loss of interest
            tips.append("Engage in small joyful activities like walking, art, or music.")
        if features[1] >= 2:  # Feeling tired
            tips.append("Take short breaks and do light stretching during your day.")
        if features[6] >= 2:  # Feeling bad about yourself
            tips.append("Practice self-kindness — speak to yourself like you would to a friend.")
        if features[2] >= 2:  # Appetite changes
            tips.append("Try balanced meals and hydrate regularly to support your mood.")
        
        recommendation = "Here are a few tips for you:\n- " + "\n- ".join(tips) if tips else "Keep doing what works for you! ✨"

        # Final result message
        if prediction == 1:
            result_msg = (
                "⚠️ Based on your responses, signs of mental stress were detected. "
                "Consider speaking with someone you trust or a professional. "
                + recommendation
            )
        else:
            result_msg = (
                "✅ You're doing well overall! Your mental health seems stable. "
                + recommendation
            )

        return jsonify({'result': result_msg})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)