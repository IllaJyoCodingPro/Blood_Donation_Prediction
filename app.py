from flask import Flask, render_template, request, jsonify, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the dataset (assuming it's already loaded and processed as in your code)
dataset = pd.read_excel("data/BDPJ.xlsx")

# Assuming your model and data preprocessing code is defined here

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('Register.html')


@app.route('/accept')
def accept():
    return render_template('accept.html')

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/predict', methods=['POST'])
def predict():
    blood_group = request.json['bloodGroup']
    
    # Filter the dataset for donors matching the specified blood group
    potential_donors = dataset[dataset['Blood group'] == blood_group]
    
    # Count the number of potential donors for the specified blood group
    donor_count = len(potential_donors)

    # Return JSON response with predicted count
    return jsonify({'predictionCount': donor_count})

@app.route('/donate/register')
def donate_register():
    return render_template('createac.html')  # Redirect to the create account page



if __name__ == '__main__':
    app.run(debug=True)
  


    