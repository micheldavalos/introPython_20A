from paqueteria import Paqueteria
from paquete import Paquete

pq = Paqueteria()

while True:
    print("1) Agregar Paquete")
    print("2) Mostrar paquetes")
    print("0) Salir")
    op = input(": ")

    if op == "1":
        p = Paquete()

        p.id = input("id: ")
        p.origen = input('origen: ')
        p.destino = input('destino: ')
        p.peso = float(input('peso: '))

        pq.agregar(p)
    elif op == "2":
        pq.mostrar()
    elif op == "0":
        break