from flask import Flask, request, render_template
from flask import jsonify
import config
from utils import obesity_prediction

import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Age = eval(request.form['Age'])
    Gender = request.form['Gender']
    Height = eval(request.form['Height'])
    Weight = eval(request.form['Weight'])
    BMI = eval(request.form['BMI'])
    PhysicalActivityLevel = eval(request.form['PhysicalActivityLevel'])

    prediction = obesity_prediction(Age, Gender, Height, Weight, BMI, PhysicalActivityLevel)
    # Make the prediction
    class_mapping = {1: 'Normal weight', 2: 'Overweight', 3: 'Obese', 0: 'Underweight'}
    predicted_class = class_mapping.get(prediction[0], 'Unknown')
  
    return render_template('index2.html', prediction=predicted_class)     


if __name__ == '__main__':
      app.run(host='0.0.0.0',port=8080,debug=False)

