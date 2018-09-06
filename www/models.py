import datetime
from sqlalchemy import  Table
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Samples(Base):
    __tablename__ = 'samples'
    id=Column(Integer, primary_key=True)
    temperature=Column('temperature', Integer)
    humidity=Column('humidity', Integer)
    pressure=Column('pressure', Integer)
    windspeed=Column('windspeed', Integer)
    
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'  : self.id,
           'temperature': self.temperature,
           'humidity': self.humidity,
           'pressure': self.pressure,
           'windspeed': self.windspeed
       }

    def __init__(self, temperature=None, humidity=None, pressure=None, windspeed=None):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.windspeed = windspeed

    def __repr__(self):
        return '<Samples {}>'.format(self.body)


#class Frequency(Base):
#    __tablename__ = 'frequency'
#    id=Column(Integer, primary_key=True)
#    last_freq=Column('last_freq', Integer)

