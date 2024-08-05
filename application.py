from flask import Flask,request,jsonify,render_template
import pickle
import os
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline

application = Flask(__name__)
app = application

#  Import our pipeline in the pickle format

model_path = os.path.join('model', 'forest_fire_final_model.pkl')

with open(model_path, 'rb') as file:
    loaded_pipeline = pickle.load(file)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods = ['GET','POST'])
def predict_datapoint():
    if request.method == "POST":
        Temperature=float(request.form.get('Temperature'))
        RH = float(request.form.get('RH'))
        Ws = float(request.form.get('Ws'))
        Rain = float(request.form.get('Rain'))
        FFMC = float(request.form.get('FFMC'))
        DMC = float(request.form.get('DMC'))
        DC = float(request.form.get('DC'))
        ISI = float(request.form.get('ISI'))
        BUI = float(request.form.get('BUI'))
        Classes = request.form.get('Classes')
        Region = request.form.get('Region')

        result=loaded_pipeline.predict([[Temperature,RH,Ws,Rain,FFMC,DMC,DC,ISI,BUI,Classes,Region]])
        return render_template('home.html',result=result[0])
    
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run()
