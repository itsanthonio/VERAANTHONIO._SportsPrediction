from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

# Load the model
model = pickle.load(open('C:\\Users\\user\\Ensemble.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from POST request
    features = [float(x) for x in request.form.values()]

    # Convert features to array and make prediction
    input_features = np.array(features).reshape(1, -1)
    prediction = model.predict(input_features)

    # Format the prediction as needed
    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Predicted Rating: {}'.format(output))

if __name__ == '__main__':
    app.run(debug=True)