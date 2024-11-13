#1
#Características de una lista:

#Una lista es una estructura de datos en Python que puede almacenar múltiples elementos en un solo objeto.
#Es mutable (sus elementos pueden cambiarse).
#Puede contener diferentes tipos de datos.
#Permite el acceso a elementos mediante índices.
#2
#a
def cargar_calificaciones():
    calificaciones = []  # Lista vacía donde se almacenarán las calificaciones
    i = 0  # Contador para el número de estudiantes
    while i < 30:  # Procesar calificaciones de 30 estudiantes
        try:  # Bloque para manejar entradas incorrectas
            nota = int(input(f"Ingrese la calificación del estudiante {i+1}: "))  # Solicita la calificación
            if 1 <= nota <= 10:  # Verifica si la calificación está en el rango permitido
                calificaciones.append(nota)  # Agrega la calificación a la lista
                i += 1  # Incrementa el contador si la entrada es válida
            else:
                print("La calificación debe estar entre 1 y 10.")  # Mensaje de error
        except ValueError:  # Captura errores si la entrada no es un número entero
            print("Entrada inválida. Debe ingresar un número.")  # Mensaje de error
    return calificaciones  # Devuelve la lista de calificaciones



#b
def promedio_y_maxima(calificaciones):
    suma = 0
    max_nota = calificaciones[0]
    max_indice = 0
    for i, nota in enumerate(calificaciones):
        suma += nota
        if nota > max_nota:
            max_nota = nota
            max_indice = i
    promedio = suma / len(calificaciones)
    return promedio, max_indice


#c
def calificaciones_sobre_promedio(calificaciones):
    promedio, _ = promedio_y_maxima(calificaciones)
    print(f"Promedio del curso: {promedio:.2f}")
    print("Estudiantes con calificaciones mayores al promedio:")
    for i, nota in enumerate(calificaciones):
        if nota > promedio:
            print(f"Estudiante {i+1}: {nota}")

#programa principal
def main():
    calificaciones = cargar_calificaciones()
    promedio, max_indice = promedio_y_maxima(calificaciones)
    print(f"El promedio del curso es: {promedio:.2f}")
    print(f"El estudiante con la calificación más alta es el número {max_indice+1}")
    calificaciones_sobre_promedio(calificaciones)

if __name__ == "__main__":
    main()




#3
def contar_n(cadena):
    contador = 0
    for char in cadena:
        if char.lower() == 'n':
            contador += 1
    return contador




#4
def prueba_contar_n():
    casos = [
        ("Programación", 1),
        ("Python", 1),
        ("Naranja", 2)
    ]
    for i, (entrada, esperado) in enumerate(casos):
        resultado = contar_n(entrada)
        assert resultado == esperado, f"Error en caso {i+1}: esperado {esperado}, obtenido {resultado}"
    print("Todos los casos de prueba pasaron.")
