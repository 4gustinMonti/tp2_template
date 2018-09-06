import os
import signal
import subprocess
from database import Database
from random import randint
from flask import flash
import time


db = Database()

class Process(object):
    # Se generaran valores random de Temperatura, Humedad, PA, Vel Viento cada frecuenciaGeneracion [segundos].
    process = None
    frecuenciaGeneracion = 10
    
    def start_process(self):
        #la primera vez que levanta la pagina cargo la DB con 100 muestras de cada sensor
        for x in range(0, 100):
            temp = randint (0,50)
            hum = randint (0,100) # porcentaje
            pa = randint(0,200) # hPa
            viento = randint (0,200) # km/h
            db.new_samples(temp,hum,pa,viento)

    def create_samples(self):
        while True:
            time.sleep(self.frecuenciaGeneracion)
            temp = randint (0,50)
            hum = randint (0,100) # porcentaje
            pa = randint(0,200) # hPa
            viento = randint (0,200) # km/h
            db.new_samples(temp,hum,pa,viento)
            flash('se han creado nuevas muestras')

    def stop_process(self):
        if self.process != None:
            os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            self.process = None
        return 200
        
    def is_running(self):
        return self.process != None