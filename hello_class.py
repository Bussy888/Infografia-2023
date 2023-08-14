class Carro:

    def __init__(self, marca, cilindrada, kilometraje):
        self.marca = marca
        self.kilometraje = kilometraje
        self.cilindrada = cilindrada

    def encender(self):
        self._iniciar_motor()
        print("Brummm brummm")

    def _iniciar_motor(self):
        print("iniciando motor")


carro = Carro("subaru", 500, 123435)
carro.encender()
print(f"marca carro1 : {carro.marca}")
carro2 = Carro("ford", 1000, 20000)
print(f"marca carro2 : {carro2.marca}")
