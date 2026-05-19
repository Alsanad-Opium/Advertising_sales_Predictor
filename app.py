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
    feature_input = data.get('features')
    
    
    features = ['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)']
    
    df_pred = pd.DataFrame(feature_input,columns=features)
    pred = model.predict(df_pred)
    
    
    return jsonify({'prediction' : round(float(pred[0]), 2)})
    


@app.route('/predict_form', methods=['POST'])
def predict_form():
    try:
        tv = request.form.get('tv')
        radio = request.form.get('radio')
        newspaper = request.form.get('newspaper')

        
        features = {
            'TV Ad Budget ($)': float(tv) if tv else np.nan,
            'Radio Ad Budget ($)': float(radio) if radio else np.nan,
            'Newspaper Ad Budget ($)': float(newspaper) if newspaper else np.nan
        }

        df_feat = pd.DataFrame([features])

        pred = model.predict(df_feat)
        value = pred.item()
        sales = pred.item()
        
        
        #  ROI Calculation
        total_budget = float(tv) + float(radio) + float(newspaper)
        roi = sales / total_budget if total_budget > 0 else 0
        
        # Insight Logic
        if roi > 0.15:
            insight = "High return. Scaling budget may increase revenue."
        elif roi > 0.08:
            insight = "Moderate return. Consider optimizing channel allocation."
        else:
            insight = "Low return. Re-evaluate marketing spend."

        return render_template(
            'index.html',
            prediction_text=f"${sales:.2f}",
            roi_text=f"{roi:.2f}",
            insight_text=insight
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text="Error",
            roi_text="",
            insight_text=str(e)
        )
    
    
if __name__ == '__main__':
    app.run(debug = True)