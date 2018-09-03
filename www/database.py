from models import Samples

from sqlalchemy import create_engine,desc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
from random import randint
import json
import os

class Database(object):
    session = None
    db_user = os.getenv("DB_USER") if os.getenv("DB_USER") != None else "example"
    db_pass = os.getenv("DB_PASS") if os.getenv("DB_PASS") != None else "example"
    db_host = os.getenv("DB_HOST") if os.getenv("DB_HOST") != None else "db"
    db_name = os.getenv("DB_NAME") if os.getenv("DB_NAME") != None else "samples"
    db_port = os.getenv("DB_PORT") if os.getenv("DB_PORT") != None else "3306"
    Base = declarative_base()
    
    def get_session(self):
        """Singleton of db connection

        Returns:
            [db connection] -- [Singleton of db connection]
        """
        if self.session == None:
            connection = 'mysql+mysqlconnector://%s:%s@%s:%s/%s' % (self.db_user,self.db_pass,self.db_host,self.db_port,self.db_name)
            engine = create_engine(connection,echo=True)
            connection = engine.connect()
            Session = sessionmaker(bind=engine)
            self.session = Session()
            self.Base.metadata.create_all(engine)
        return self.session
    
    def start_sampling(self):
        """Generate samples of temperature, humidity, pressure and windspeed in the database.
    
        Returns:
            nothing
        """
        session = self.get_session()
        ten_samples = session.query(Samples).limit(10)
        if len(ten_samples) < 10:
            #primera vez que levanta la DB, simulo que ya estaba muestreando, genero 10 muestras de cada sensor y vuelvo a consultar
            for x in range(10):
                temperatura = randint (0,50)
                humedad = randint (0,100) # porcentaje
                h_pascales = randint(0,200) # hPa
                viento = randint (0,200) # km/h
                samples = Samples(temperature=temperatura, humidity=humedad, pressure=h_pascales, windspeed=viento)
                session.add(samples)
                session.commit()
            ten_samples = session.query(Samples).limit(10)
        session.close()

    def get_samples(self):
        """Get samples of temperature, humidity, pressure and windspeed from the database.
    
        Returns:
            temp, hum, pres , viento objects with 'actual' and 'promedio' attributes
        """
        session = self.get_session()
        temp : {
            "actual": 0,
            "promedio": 0.0,
            }
        hum : {
            "actual": 0,
            "promedio": 0.0,
            }
        pres : {
            "actual": 0,
            "promedio": 0.0,
            }
        viento : {
            "actual": 0,
            "promedio": 0.0,
            }
        #obtengo las ultimas 10 muestras
        total_samples = session.query(Samples).order_by(desc(Samples.id)).limit(10)
        #muestra actual de cada sensor
        temp["actual"] = total_samples[9].temperature
        hum["actual"] = total_samples[9].humidity
        pres["actual"] = total_samples[9].pressure
        viento["actual"] = total_samples[9].windspeed
        #calculo el promedio de esas 10 muestras
        for sample in total_samples:
            temp["promedio"] += sample.temperature
            hum["promedio"] += sample.humidity
            pres["promedio"] += sample.pressure
            viento["promedio"] += sample.windspeed
        temp["promedio"] /= 10
        hum["promedio"] /= 10
        pres["promedio"] /= 10
        viento["promedio"] /= 10
        session.close()
        return temp.serialize(),hum.serialize(), pres.serialize(), viento.serialize()