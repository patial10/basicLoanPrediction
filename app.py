import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

# from sklearn.external import joblib
# try
import joblib

app = Flask(__name__)
model=pickle.load(open("savedFile.pkl","rb"))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/hello')
def hello():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

#     output = round(prediction[0], 2)
    if prediction == 'N':
        prediction="This Person is not able to take the loan on the basis of his/her informaton"
    else:
        prediction="This person is able to take the loan on the basis of his/her informaton"
        
    return render_template('home.html', prediction_text=' {} '.format(prediction))

if __name__ == "__main__":
    app.run(debug=True)
