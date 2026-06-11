class Mascota:

    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def mostrar_informacion(self):
        print("INFORMACIÓN DE LA MASCOTA")
        print(f"Nombre : {self.nombre}")
        print(f"Especie  : {self.especie}")
        print(f"Edad   : {self.edad }")

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
           print(f"{self.nombre}'dice: ¡guau guau!")
        elif self.especie.lower() == "loro":
            print(f"{self.nombre} dice ¡hola! ¿quiere cacao?")
        else:
            print(f"{self.nombre} hace un sonido.")