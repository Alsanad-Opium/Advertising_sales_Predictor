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
    
    
@app.route('/predict', methods= ['POST'])

def predict():
    data = request.get_json()
    data = data.get('features')
    
    
    features = ['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']
    
    df_pred = pd.DataFrame(data,columns=features)
    pred = model.predict(df_pred)
    
    
    return jsonify({'prediction' : round(float(pred[0]))})
    


@app.route('/predict_form', methods=['POST'])
def predict_form():
    data = {}
    
    # Securely parse values one by one
    for key, val in request.form.items():
        val = val.strip()
        if val == '':
            data[key] = np.nan
        else:
            try:
                # Only accept valid numbers
                data[key] = float(val)
            except ValueError:
                # If someone typed text/letters, treat it as missing data safely
                data[key] = np.nan 
    
    df_feat = pd.DataFrame([data])
    pred = model.predict(df_feat)
    value = pred.item()
    
    return render_template('index.html', prediction_text=f'Predicted Sales: {round(value)}')

    
if __name__ == '__main__':
    app.run(debug = True)