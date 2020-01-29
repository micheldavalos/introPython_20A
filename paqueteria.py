class Paqueteria:
    def __init__(self):
        self.paquetes = []

    def agregar(self, paquete):
        self.paquetes.append(paquete)

    def mostrar(self):
        for p in self.paquetes:
            print('id:', p.id)
            print('origen:', p.origen)
            print('destino:', p.destino)
            print('peso:', p.peso)