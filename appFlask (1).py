import pandas as pandas
import numpy as np
import sklearn
import joblib
from flask import Flask,render_template,request 
app=Flask(__name__)
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/prediccion',methods=['GET','POST'])
def predict():
  if request.method =='POST':
    try:
      var_1=float(request.form["var_1"])
      var_2=float(request.form["var_2"])

      pred_args=[var_1,var_2]
      pred_arr=np.array(pred_args)
      preds=pred_arr.reshape(1,-1)
      modelo=open("./modelo.pkl","rb")
      modelo_class=joblib.load(modelo)
      prediccion_modelo=modelo_class.predict(preds)
      prediccion_modelo=round(float(prediccion_modelo),2)
      if prediccion_modelo == 1.0:
        prediccion_modelo = "Apreuba"
      else:
        prediccion_modelo = "No aprueba"
    except ValueError:
      return "porfavor entra nombre validos"
    return render_template('prediccion.html',prediccion=prediccion_modelo)
  
    if ___name___=='___main___':
        app.run(debug=True)