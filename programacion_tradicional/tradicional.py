
def registrar_mascota():
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie: ")
    edad = input("Ingrese la edad: ")
    return nombre, especie, edad

def mostrar_mascota(nombre, especie, edad):
    print("\nINFORMACIÓN DE LA MASCOTA")
    print(f"Nombre : {nombre}")
    print(f"Especie  : {especie}")
    print(f"Edad   : {edad}")

nombre, especie, edad = registrar_mascota()
mostrar_mascota(nombre, especie, edad)