## How to deploy ML Model with Flask
This is a demo project to elaborate how Machine Learn Models are deployed on production using Flask API

### Prerequisites
You must have Scikit Learn, Numpy, Pandas and Flask installed.

### Project Structure
This project has 3 parts :
1. model.py - This contains code for our Machine Learning model to predict iris category based on training data from Scikit Learn Data set.
2. app.py - This contains Flask APIs that receives iris description values through GUI or API calls, computes the precited value based on our model and returns it.
3. templates - This folder contains the HTML template to allow user to enter iris description values and displays the predicted iris category.

### Running the project
1. Ensure that you are in the project home directory. Create the machine learning model by running below command -
```
python model.py
```
This would create a serialized version of our model into a file model.pkl

2. Run app.py using below command to start Flask API
```
python app.py
```
By default, flask will run on port 5000.

3. Navigate to URL http://localhost:5000

Enter valid numerical values in all 4 input text and hit Predict.
