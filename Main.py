from src.Ingreso import multiples_ingresos
from src.Ingreso import verListado
from src.Actualizar import actualizar
from src.Eliminar import eliminar


cocheLista = []

while True:
    print("1. Ingresar coche")
    print("2. Ver listado de coches")
    print("3. Eliminar coche por marca")
    print("4. Actualizar coche por marca")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        multiples_ingresos(cocheLista)
    elif opcion == "2":
        verListado(cocheLista)
    elif opcion == "3":
        marca = input("Introduce la marca del coche a eliminar: ")
        cocheLista = eliminar(cocheLista, marca)
    elif opcion == "4":
        marca = input("Introduce la marca del coche a actualizar: ")
        cocheLista = actualizar(cocheLista, marca)
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
