# Importing essential libraries
from flask import Flask, render_template, request
#from flask import jsonify 
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'regressor.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
      if request.method == 'POST':
          PM10 = int(request.form['PM10'])
          Benzene = int(request.form['Benzene'])
          NO = int(request.form['NO'])
          NO2 = int(request.form['NO2'])
          NOx = int(request.form['NOx'])
          data = np.array([[PM10, Benzene, NO, NO2, NOx]])
          my_prediction =regressor.predict(data)
     # return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(my_prediction)
      return render_template('result.html', prediction=my_prediction)
    # return my_prediction()


if __name__ == "__main__":
    app.run(debug=True)