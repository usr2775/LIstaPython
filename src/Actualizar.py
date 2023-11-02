def actualizar(cocheLista, marca):
    for coche in cocheLista:
        if coche['marca'].lower() == marca.lower():
            marca_nueva = input('Nueva marca: ')
            modelo_nuevo = input('Nuevo modelo: ')
            precio_nuevo = float(input('Nuevo precio: '))
            coche['marca'] = marca_nueva
            coche['modelo'] = modelo_nuevo
            coche['precio'] = round(precio_nuevo, 2)
    return cocheLista
