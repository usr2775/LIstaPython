from src.Ingreso import multiples_ingresos, verListado
from src.Eliminar import eliminar
from src.Actualizar import actualizar
from src.Consultar import consultar

cocheLista = []

while True:
    print("1. Ingresar coche")
    print("2. Ver listado de coches")
    print("3. Eliminar coche por marca")
    print("4. Actualizar coche por marca")
    print("5. Consultar coche por marca") 
    print("6. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cocheLista = multiples_ingresos(cocheLista)
    elif opcion == "2":
        verListado(cocheLista)
    elif opcion == "3":
        marca = input("Introduce la marca del coche a eliminar: ")
        cocheLista = eliminar(cocheLista, marca)
    elif opcion == "4":
        marca = input("Introduce la marca del coche a actualizar: ")
        cocheLista = actualizar(cocheLista, marca)
    elif opcion == "5":
        marca_consultar = input("Introdue la marca del coche a consultar: ")
        consultar(cocheLista, marca_consultar)  
    elif opcion == "6":
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
