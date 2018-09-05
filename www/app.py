# Imports
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
from process import Process
from database import Database
import os

app = Flask(__name__)
db = Database()
pro = Process()

@app.route('/config')
def leo_config():
    
    return render_template('config.html')
@app.route('/config', methods = [ 'POST'])
def escribo_config():
    data = 10
    return render_template('index.html',data = data)

@app.route('/', methods = ['GET'])
def start_sampling():
     # If there is a process running, return to index()
    if not pro.is_running():
        pro.start_process()
    return render_template('index.html')

@app.route('/samples', methods = ['GET'])
def get_samples():
    #traigo las 10 ultimas muestras de cada sensor
    ten_samples = db.get_samples()
    temp_actual = 0
    temp_promedio = 0.0
    hum_actual = 0
    hum_promedio = 0.0
    pres_actual = 0
    pres_promedio = 0.0
    viento_actual = 0
    viento_promedio = 0.0
    #muestra actual de cada sensor
    temp_actual = ten_samples[-1].temperature
    hum_actual = ten_samples[-1].humidity
    pres_actual = ten_samples[-1].pressure
    viento_actual = ten_samples[-1].windspeed
    #calculo el promedio de esas 10 muestras
    for sample in ten_samples:
        temp_promedio += sample.temperature
        hum_promedio += sample.humidity
        pres_promedio += sample.pressure
        viento_promedio += sample.windspeed
    temp_promedio /= 10
    hum_promedio /= 10
    pres_promedio /= 10
    viento_promedio /= 10
    return jsonify (temp_actual = temp_actual,
                    hum_actual = hum_actual,
                    pres_actual = pres_actual,
                    viento_actual = viento_actual,
                    temp_promedio = temp_promedio,
                    hum_promedio = hum_promedio,
                    pres_promedio = pres_promedio,
                    viento_promedio = viento_promedio)

@app.route('/shut-down', methods = ['GET'])
def shut_down():
    data = pro.stop_process()
    return jsonify({"status": data})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

