import signal
from database import Database

import random
import time
import sys

db = Database()

class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True

# Se generaran valores random de Temperatura, Humedad, PA, Vel Viento cada frecuenciaGeneracion [segundos].

frecuenciaGeneracion = 1

#desde aca es lo nuevo
def main():
    killer = GracefulKiller()
    while(True):
        temp = random.randint (0,50)
        hum = random.randint (0,100) # porcentaje
        pa = random.randint(0,200) # hPa
        viento = random.randint (0,200) # km/h
        db.new_samples(temp,hum,pa,viento)
        time.sleep(frecuenciaGeneracion)
        if killer.kill_now:
            break

if __name__ == '__main__':
    main()