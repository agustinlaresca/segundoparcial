#1
#Consigna 1:
#Características del tipo de dato string:

#Un string es una secuencia de caracteres.
#Es inmutable (no se puede modificar después de su creación).
#Puede incluir caracteres alfanuméricos, espacios y símbolos.
#Permite el acceso a caracteres individuales mediante índices.
#2
#a
def cargar_seguidores():
    seguidores = []  # Lista vacía para almacenar los seguidores
    i = 0  # Contador para el número de usuarios
    while i < 200:  # Procesar seguidores de 200 usuarios
        try:  # Manejar errores en la entrada
            cantidad = int(input(f"Ingrese la cantidad de seguidores del usuario {i+1}: "))  # Entrada del usuario
            if 100 <= cantidad <= 10000:  # Valida si la cantidad de seguidores está en el rango permitido
                seguidores.append(cantidad)  # Agrega la cantidad a la lista
                i += 1  # Incrementa el contador si la entrada es válida
            else:
                print("La cantidad debe estar entre 100 y 10.000.")  # Mensaje de error
        except ValueError:  # Captura errores si la entrada no es numérica
            print("Entrada inválida. Debe ingresar un número.")  # Mensaje de error
    return seguidores  # Devuelve la lista de seguidores





# Función para cargar seguidores en una lista
def cargar_seguidores():
    """
    Solicita al usuario ingresar la cantidad de seguidores para 200 usuarios,
    validando que estén dentro del rango permitido (100 a 10,000).
    """
    seguidores = []
    i = 0
    while i < 200:  # Procesar seguidores de 200 usuarios
        try:
            cantidad = int(input(f"Ingrese la cantidad de seguidores del usuario {i+1}: "))
            if 100 <= cantidad <= 10000:  # Validar rango permitido
                seguidores.append(cantidad)
                i += 1  # Avanzar solo si la entrada es válida
            else:
                print("La cantidad debe estar entre 100 y 10,000.")
        except ValueError:  # Capturar entradas no numéricas
            print("Entrada inválida. Debe ingresar un número.")
    return seguidores

# b) Función para calcular promedio y usuario con más seguidores
def promedio_y_max_seguidores(seguidores):
    """
    Calcula el promedio de seguidores y encuentra el índice del usuario
    con la mayor cantidad de seguidores.

    Args:
        seguidores (list): Lista de cantidades de seguidores.

    Returns:
        tuple: Promedio de seguidores y el índice del usuario con más seguidores.
    """
    suma = 0
    max_seguidores = seguidores[0]
    max_indice = 0
    for i, seg in enumerate(seguidores):  # Recorrer la lista con índices
        suma += seg  # Sumar cada cantidad de seguidores
        if seg > max_seguidores:  # Buscar el máximo
            max_seguidores = seg
            max_indice = i
    promedio = suma / len(seguidores)  # Calcular el promedio
    return promedio, max_indice

# c) Función para mostrar usuarios con seguidores mayores al promedio
def seguidores_sobre_promedio(seguidores):
    """
    Imprime los usuarios que tienen más seguidores que el promedio.

    Args:
        seguidores (list): Lista de cantidades de seguidores.
    """
    promedio, _ = promedio_y_max_seguidores(seguidores)
    print(f"Promedio de seguidores: {promedio:.2f}")
    print("Usuarios con seguidores mayores al promedio:")
    for i, seg in enumerate(seguidores):
        if seg > promedio:  # Verificar si los seguidores superan el promedio
            print(f"Usuario {i+1}: {seg}")

# Programa principal
def main():
    """
    Programa principal para gestionar seguidores y realizar análisis.
    """
    seguidores = cargar_seguidores()  # Cargar los seguidores
    promedio, max_indice = promedio_y_max_seguidores(seguidores)
    print(f"El promedio de seguidores es: {promedio:.2f}")
    print(f"El usuario con más seguidores es el número {max_indice+1}")
    seguidores_sobre_promedio(seguidores)

# 3) Función para contar la letra 'r' en una cadena
def contar_r(cadena):
    """
    Cuenta el número de apariciones de la letra 'r' en una cadena,
    ignorando mayúsculas y minúsculas.

    Args:
        cadena (str): Cadena de texto en la que se buscará la letra 'r'.

    Returns:
        int: Número de veces que aparece 'r' en la cadena.
    """
    contador = 0
    for char in cadena:  # Recorrer cada carácter de la cadena
        if char.lower() == 'r':  # Verificar si el carácter es 'r'
            contador += 1  # Incrementar el contador
    return contador

# 4) Función de prueba para contar_r
def prueba_contar_r():
    """
    Prueba la función `contar_r` con diferentes casos de prueba.
    """
    casos = [
        ("Programación", 2),  # Caso 1: 2 veces 'r'
        ("Rápido", 1),        # Caso 2: 1 vez 'r'
        ("Correr", 3)         # Caso 3: 3 veces 'r'
    ]
    for i, (entrada, esperado) in enumerate(casos):  # Recorrer casos de prueba
        resultado = contar_r(entrada)  # Llamar a la función para el caso actual
        assert resultado == esperado, f"Error en caso {i+1}: esperado {esperado}, obtenido {resultado}"  # Comprobar resultados
    print("Todos los casos de prueba pasaron.")  # Imprimir mensaje de éxito

# Ejecución del programa
if __name__ == "__main__":
    # Realizar pruebas para la función contar_r
    prueba_contar_r()
    # Ejecutar el programa principal
    main()

