import threading 
import time
import random
from database import Database

bd = Database(database= "bancoiot", collection= "sensores")
bd.resetDatabase()

sensorUm = {
    "nomeSensor": "Temp1",
    "valorSensor": [],
    "unidadeMedida": "C°",
    "sensorAlarmado": False
}
sensorDois = {
    "nomeSensor": "Temp2",
    "valorSensor": [],
    "unidadeMedida": "C°",
    "sensorAlarmado": False
}
sensorTres = {
    "nomeSensor": "Temp3",
    "valorSensor": [],
    "unidadeMedida": "C°",
    "sensorAlarmado": False
}

bd.inserirDocumento(sensorUm)
bd.inserirDocumento(sensorDois)
bd.inserirDocumento(sensorTres)

def sensor1(nome, intervalo):
    normal = True
    while normal:
        temperatura = random.randint(30, 40)
        bd.atualizarTemperatura("Temp1", temperatura)
        print(f"O {nome} esta medindo {temperatura} graus")

        if temperatura > 38:
            normal = False
            print("Atenção! Temperatura muito alta! Verificar Sensor 1!")
            bd.atualizarAlarme("Temp1")

        time.sleep(intervalo)


def sensor2(nome, intervalo):
    normal = True
    while normal:
        temperatura = random.randint(30, 40)
        bd.atualizarTemperatura("Temp2", temperatura)
        print(f"O {nome} esta medindo {temperatura} graus")
        
        if temperatura > 38:
            normal = False
            print("Atenção! Temperatura muito alta! Verificar Sensor 2!")
            bd.atualizarAlarme("Temp2")

        time.sleep(intervalo)

def sensor3(nome, intervalo):
    normal = True
    while normal:
        temperatura = random.randint(30, 40)
        bd.atualizarTemperatura("Temp3", temperatura)
        print(f"O {nome} esta medindo {temperatura} graus")

        if temperatura > 38:
            normal = False
            print("Atenção! Temperatura muito alta! Verificar Sensor 3!")
            bd.atualizarAlarme("Temp3")
        time.sleep(intervalo)

s1 = threading.Thread(target = sensor1, args = ("sensor 1", 2))
s2 = threading.Thread(target = sensor2, args = ("sensor 2", 2))
s3 = threading.Thread(target = sensor3, args = ("sensor 3", 2))

s1.start()
s2.start()
s3.start()

