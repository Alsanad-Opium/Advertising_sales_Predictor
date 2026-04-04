import pickle 
from flask import Flask,request,jsonify
import numpy as np 
import pandas as pd

model = pickle.load(open('model/Advertising_model_sales_v1.pkl','rb'))

EXPECTED_FEATURES = 3
app = Flask(__name__)

@app.route('/')

def home():
    return " First ml and flask api bitch"
    
    
@app.route('/predict', methods = ['POST'])

def predict():

    data  = request.get_json()
    
     # 🔹 Check if data exists
    if not data:
            return jsonify({"error": "No input data provided"}), 400

        # 🔹 Check key
    if 'features' not in data:
            return jsonify({"error": "'features' key missing"}), 400
        
    features = data['features'] 
    
    # 🔹 Check type
    if not isinstance(features, list):
            return jsonify({"error": "Features must be a list"}), 400

        # 🔹 Check length
    if len(features) != EXPECTED_FEATURES:
            return jsonify({
                "error": f"Expected {EXPECTED_FEATURES} features"
            }), 400
     
      
    df_feat = pd.DataFrame(features, columns = ['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']) 
    
    pred = model.predict (df_feat)
    return jsonify({
        "status": "success",
        'prediction': pred.tolist()
    })
    
    
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})
    
    
if __name__ == '__main__':
    app.run(debug = True)