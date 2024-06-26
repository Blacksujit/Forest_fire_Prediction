from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)   

# Load the trained model
with open('./model/model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from POST request
        data = request.get_json(force=True)

        # Extract features
        features = [data['temp'], data['RH'], data['wind']]
        features = np.array(features).reshape(1, -1)

        # Make prediction using loaded model
        prediction = model.predict(features)
        prediction_proba = model.predict_proba(features)[0]

        # Prepare response
        result = {
            'fire': bool(prediction[0]),
            'probability': prediction_proba.tolist(),
            'accuracy': model.score(features, [prediction[0]])
        }

        # Return result
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True , port=560)
