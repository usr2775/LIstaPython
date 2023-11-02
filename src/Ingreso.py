cocheLista = []

def ingreso(cocheLista):
    marca = input('Cual es la marca: ')
    modelo = input('Cual es el modelo: ')
    precio = input('Cual es el precio: ')
    precio = float(precio)
    vehiculo = {
        "marca": marca,
        "modelo": modelo,
        "precio": round(precio, 2)
    }
    cocheLista.append(vehiculo)
    return cocheLista

def verListado(cocheLista):
    print(cocheLista)

def multiples_ingresos(cocheLista):
    salida = True
    while salida:
        cocheLista = ingreso(cocheLista)
        que_hago = input('Quieres salir s/n')
        if que_hago == 's' or que_hago == 'S' or que_hago == 'Y' or que_hago == 'y':
            salida = False
        else:
            verListado(cocheLista)
    return cocheLista