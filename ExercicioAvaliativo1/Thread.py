import threading # Lib para se trabalhar com Threads
import time # Permite executar uma Thread mais devagar

# Função que sera chamada pela Thread
def sayHello(nome, intervalo):
    while True:
        print(f"{nome} say hello")
        time.sleep(intervalo)

# Abrindo uma Thread 
x = threading.Thread(target = sayHello, args = ('Thread 1', 2))
x.start()