def verListado(cocheLista):
    if not cocheLista:
        print("No hay ningu auto en la lista")
    else:
        print("Listado de autos:")
        for i, auto in enumerate(cocheLista, start=1):
            print(f"Auto {i}:")
            print(f"Marca: {auto['marca']}")
            print(f"Modelo: {auto['modelo']}")
            print(f"Precio: ${auto['precio']:.2f}")

def ordenarLista(cocheLista, criterio):
    if criterio == "marca":
        cocheLista.sort(key=lambda auto: auto['marca'])
    elif criterio == "modelo":
        cocheLista.sort(key=lambda auto: auto['modelo'])
    elif criterio == "precio":
        cocheLista.sort(key=lambda auto: auto['precio'])
    else:
        print("Criterio de orden no válido. Ordenando por marca por defecto.")
        cocheLista.sort(key=lambda auto: auto['marca'])

from src.Ingreso import multiples_ingresos
from src.Ingreso import verListado

cocheLista = [] 
multiples_ingresos(cocheLista)  
criterio = input("¿Cómo deseas ordenar la lista (marca/modelo/precio)? ").lower()

ordenarLista(cocheLista, criterio)

verListado(cocheLista)
