import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.datasets import load_iris
iris_dataset = load_iris()

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    prediction = iris_dataset['target_names'][prediction]
    return render_template('index.html', prediction=prediction, long_petale=final_features[0][0], larg_petale=final_features[0][1], long_sepale=final_features[0][2], larg_sepale=final_features[0][3])

if __name__ == "__main__":
    app.run(debug=False)