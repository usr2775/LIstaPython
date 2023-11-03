def consultar(cocheLista, marca_consultar):
    coches_encontrados = [coche for coche in cocheLista if coche['marca'].lower() == marca_consultar.lower()]
    if coches_encontrados:
        print("Coches con la marca {}:".format(marca_consultar))
        for coche in coches_encontrados:
            print("Marca: {}, Modelo: {}, Precio: ${:.2f}".format(coche["marca"], coche["modelo"], coche["precio"]))
    else:
        print("No se encontraron coches con la marca {}".format(marca_consultar))
