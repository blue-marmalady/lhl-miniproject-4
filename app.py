#import the required plugins
# building an API that hosts a model. 
from flask import Flask, request, jsonify
from flask_restful import Api, Resource 
import pickle
#api turns your app into an API, and resource sends
#things in and out

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import pandas as pd
import numpy as np

from sklearn.svm import LinearSVC

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# create Flask object
app = Flask(__name__)

# Create api from application
api = Api(app) 

# load the model
model = pickle.load(open('model.sav', 'rb'))

# read the request
class Predict(Resource):

    def post(self):
        json_data = request.get_json()

        #For one observation, transposing the data, so index is a column.
        #df = pd.DataFrame(json_data.values(), index = json_data.keys()).transpose


        #Recieving multiple observations
        df = pd.DataFrame(json_data)

# return the prediction. 
        result = model.predict(df)
        return result.tolist()

# assign endpoints
api.add_resource(Predict, '/predict')

# run main function
if __name__ == '__main__':
    app.run(port=5000, debug=True)