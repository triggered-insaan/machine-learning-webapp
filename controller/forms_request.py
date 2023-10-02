from app import app
from flask import request, jsonify, render_template
from model.user_model import Model
from numpy import array

@app.route('/receive', methods=["POST"])
def receive():
    data=request.form
    input_data=[float(data['CRIM']),float(data['ZN']),float(data['INDUS']),float(data['CHAS']),float(data['NOX']),float(data['RM']),float(data['AGE']),float(data['DIS']),float(data['RAD']),float(data['TAX']),float(data['PTRATIO']),float(data['B']),float(data['LSTAT'])]
    
    # Evaluating the value using Dragon Model
    mdl=Model('model/dragon.model')
    value=mdl.predict(array(input_data))*1000*82
    
    return render_template('result.html',value=value)
