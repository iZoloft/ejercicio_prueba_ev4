# #### Resolver:

# Desarrolla un programa en Python que implemente un **Sistema de Gestión de Envíos y Logística**, donde todo el comportamiento se organice mediante funciones bien definidas y separadas en módulos.

# #### 1. Datos que debe manejar el sistema

# El sistema trabaja con una colección de envíos (paquetes). Esta colección es una lista que comienza vacía y se va llenando a medida que se agregan registros. Cada envío es un diccionario con los siguientes campos y restricciones:

# | Campo | Qué representa | Restricciones de validación |
# | --- | --- | --- |
# | `"codigo"` | Código de seguimiento del paquete | No vacío ni solo espacios en blanco. |
# | `"peso"` | Peso del paquete en kilogramos | Número decimal (float) mayor que 0. |
# | `"distancia"` | Distancia al destino en kilómetros | Número entero (int) mayor que 0. |
# | `"despachado"` | ¿El paquete ya salió a ruta? | `False` al registrar. No se valida ni se pide al usuario. Su valor cambia a `True` al ejecutar la Opción 4, dependiendo de la distancia. |

# #### 2. Lo que debe hacer el sistema

# El sistema se controla desde un menú interactivo. Debes crear una función para imprimir el menú y otra para leer/validar la opción ingresada (entre 1 y 6).

# **========== MENÚ DE LOGÍSTICA ==========**

# 1. Registrar nuevo envío
# 2. Buscar envío por código
# 3. Eliminar envío cancelado
# 4. Actualizar estado de despachos
# 5. Mostrar todos los envíos
# 6. Salir del sistema
# **=======================================**

# **Opción 1 - Registrar nuevo envío:**
# El sistema solicita al usuario el código, el peso y la distancia. Debes usar funciones de validación independientes para cada dato (estas funciones solo retornan `True` o `False`). Los mensajes de error se muestran en la función principal, no dentro del validador. Si todo es válido, se crea el diccionario y se agrega a la lista global.

# **Opción 2 - Buscar envío por código:**
# El sistema pide el código a buscar. **Regla estricta:** Debes crear una función que reciba la lista de envíos y el código (en ese orden exacto) como parámetros. La función retorna la posición numérica en la lista o `-1` si no existe. El `main.py` decide qué imprimir: si lo encuentra, muestra todos sus datos; si no, arroja un mensaje de error.

# **Opción 3 - Eliminar envío cancelado:**
# El sistema pide el código del paquete a eliminar. Reutiliza la función de búsqueda de la Opción 2. Si la función retorna una posición válida, elimina el registro usando esa posición exacta. Si retorna `-1`, muestra el mensaje: *"El envío con código 'X' no se encuentra registrado"*.

# **Opción 4 - Actualizar estado de despachos:**
# El sistema recorre la lista completa. La regla de negocio es: todos los envíos que tengan una **distancia menor o igual a 50 km** deben cambiar su estado `"despachado"` a `True` (envío exprés). Los que tengan más de 50 km se mantienen en `False`. Esto debe hacerse en una función que reciba la lista como parámetro.

# **Opción 5 - Mostrar todos los envíos:**
# El sistema primero llama a la función de la Opción 4 para actualizar los estados. Luego, recorre la lista y muestra los paquetes con el siguiente formato. *(Pista: Recuerda tu validador de listas para evitar que intente mostrar cosas si la lista está vacía).*

# === REGISTRO DE ENVÍOS ===
# Código: PKT-001
# Peso: 2.5 kg
# Distancia: 15 km
# Estado: EN RUTA
# ********************************
# Código: PKT-002
# Peso: 14.0 kg
# Distancia: 400 km
# Estado: EN BODEGA
# ********************************
# **Opción 6 - Salir:**
# El programa rompe el ciclo de forma limpia y despide al usuario con un mensaje amigable.

from functions import *

while True:
    mostrar_menu()
    opcion = leer_opcion()
    if opcion == 1:
        registrar_envio(lista_envios)
    elif opcion == 2:
        codigo = input("Ingrese código de envío a buscar: \n").strip()
        posicion = buscar_envio(lista_envios, codigo)
        if posicion != -1:
            print(f"Envío encontrado en la posición {posicion}")
            print(f"Código: {lista_envios[posicion]["codigo"]}")
            print(f"Peso: {lista_envios[posicion]["peso"]} kg")
            print(f"Distancia: {lista_envios[posicion]["distancia"]} km")
            estado_texto = traducir_estado(lista_envios[posicion]['despachado'])
            print(f"Estado: {estado_texto}")
        else:
            print("Envío no se encuentra registrado")
    elif opcion ==  3:
        codigo = input("Ingrese código de envío a buscar: \n").strip()
        posicion = buscar_envio(lista_envios, codigo)
        if posicion != -1:
            lista_envios.pop(posicion)
            print("Envío eliminado")
        else:
            print(f"Envío {codigo} no se ha encontrado")
    elif opcion == 4:
        actualizar_estado(lista_envios)
    elif opcion == 5:
        mostrar_envios(lista_envios)
    else:
        print("Gracias por usar nuestra app :D")
        break