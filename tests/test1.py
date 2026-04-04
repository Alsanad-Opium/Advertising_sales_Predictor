# This is the samplel tes to check whether the models i loaded perfectly or not nad is able to make predictions or not 

import numpy as np
import pickle as pk


model = pk.load(open('..\model\Advertising_model_sales_v1.pkl','rb'))

import pandas as pd

sample_input = pd.DataFrame([[230.1, 37.8, 69.2]],
                            columns=['TV Ad Budget ($)', 'Radio Ad Budget ($)', 'Newspaper Ad Budget ($)'])

pred = model.predict(sample_input)

print(pred)