import pickle 
from flask import Flask,request,jsonify
import numpy as np 
import pandas as pd

model = pickle.load(open('model/Advertising_model_sales_v1.pkl','rb'))


app = Flask(__name__)

@app.route('/')

def home():
    return " First ml and flask api bitch"
    
    
@app.route('/predict', methods = ['POST'])

def predict():

    data  = request.get_json()
    
    features = data['features'] 
     
      
    df_feat = pd.DataFrame(features, columns = ['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']) 
    
    pred = model.predict (df_feat)
    return jsonify({
        'prediction': pred.tolist()
    })
    
    
    
    
    
if __name__ == '__main__':
    app.run(debug = True)