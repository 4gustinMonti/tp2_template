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
    
    def new_samples(self, temperatura, humedad, h_pascales, viento):
        """Generate samples of temperature, humidity, pressure and windspeed in the database.
    
        Returns:
            nothing
        """
        session = self.get_session()
        samples = Samples(temperature=temperatura, humidity=humedad, pressure=h_pascales, windspeed=viento)
        session.add(samples)
        session.commit()
        session.close()

    def get_samples(self):
        """Get samples of temperature, humidity, pressure and windspeed from the database.
    
        Returns:
            temp, hum, pres , viento objects with 'actual' and 'promedio' attributes
        """
        session = self.get_session()
        #obtengo las ultimas 10 muestras
        ten_samples = session.query(Samples).order_by(desc(Samples.id)).limit(10)
        session.close()
        return ten_samples
