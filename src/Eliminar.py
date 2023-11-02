def eliminar(cocheLista, marca):
    cocheLista = [coche for coche in cocheLista if coche['marca'].lower() != marca.lower()]
    return cocheLista
