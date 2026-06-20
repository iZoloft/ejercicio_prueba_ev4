lista_envios = []

def mostrar_menu():
    print("========== MENÚ DE LOGÍSTICA ==========")
    print("1. Registrar nuevo envío")
    print("2. Buscar envío por código")
    print("3. Eliminar envío cancelado")
    print("4. Actualizar estado de despachos")
    print("5. Mostrar todos los envíos")
    print("6. Salir del sistema")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: \n"))
            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Opción no válida, debe ser entre 1 y 6")
        except:
            print("Valor debe ser numérico")

def _validar_peso(numero):
    if numero > 0:
        return True
    return False

def _validar_distancia(numero):
    if numero > 0:
        return True
    return False

def _validar_string(codigo):
    if len(codigo) > 0:
        return True
    return False

def _validar_lista(lista_envios):
    if len(lista_envios) > 0:
        return True
    return False

def traducir_estado(estado_booleano):
    if estado_booleano == True:
        return "En Ruta"
    else:
        return "En Bodega"

def registrar_envio(lista_envios):
    while True:
        codigo = input("Ingrese código de seguimiento del paquete: \n").strip()
        if _validar_string(codigo):
            break
        else:
            print("Código no debe venir vacio")
    while True:
        peso = float(input("Ingrese peso del paquete en kilogramos: \n"))
        if _validar_peso(peso):
            break
        else:
            print("Peso debe ser mayor a 0")
    while True:
        distancia = int(input("Ingrese distancia en kilometros del destino: \n"))
        if _validar_distancia(distancia):
            break
        else:
            print("Distancia debe ser mayor a 0")
    paquete={
        "codigo" : codigo,
        "peso" : peso,
        "distancia" : distancia,
        "despachado" : False
    }
    lista_envios.append(paquete)
    print("Paquete ingresado al sistema")

def buscar_envio(lista_envios, codigo):
    for e in range(len(lista_envios)):
        if lista_envios[e]["codigo"] == codigo:
            return e
    return -1

def actualizar_estado(lista_envios):
    if _validar_lista(lista_envios) == False:
        print("No hay envios")
        return
    for e in lista_envios:
        if e["distancia"] <= 50:
            e["despachado"] = True
        else:
            e["despachado"] = False
    print("Disponibilidad Actualizada")

def mostrar_envios(lista_envios):
    if _validar_lista(lista_envios) == False:
        print("No hay envios")
        return
    actualizar_estado(lista_envios)
    print("=== REGISTRO DE ENVÍOS ===")
    for e in lista_envios:
        print(f"Código: {e["codigo"]}")
        print(f"Peso: {e["peso"]} kg")
        print(f"Distancia: {e["distancia"]} km")
        estado_texto = traducir_estado(e['despachado'])
        print(f"Estado: {estado_texto}")
