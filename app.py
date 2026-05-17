import pickle 
from flask import Flask,request,jsonify,render_template
import numpy as np 
import pandas as pd

model = pickle.load(open('model/Advertising_model_sales_v1.pkl','rb'))

EXPECTED_FEATURES = 3
app = Flask(__name__)

@app.route('/')

def home():
    return render_template('index.html')
    

    
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "running"})
    
    
@app.route('/predict_form', methods = ['POST'])

def predict_form():
    tv = request.form.get('f1')
    radio = request.form.get('f2')
    newspaper = request.form.get('f3')
    
    features = [[float(tv), float(radio), float(newspaper)]]
    
    df_feat = pd.DataFrame(features, columns = ['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']) 
    
    pred = model.predict (df_feat)
    value = pred[0].item() # this covert the numpy floast valeu into regular python float value 
    
    
    return render_template('index.html', prediction_text = f'Predicted Sales: {round(value)}')
    
if __name__ == '__main__':
    app.run(debug = True)