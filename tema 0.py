#1
#Diferencia entre un ciclo definido e indefinido:

#Un ciclo definido tiene un número fijo de iteraciones determinado antes de su ejecución, como los ciclos for.
#Un ciclo indefinido continúa ejecutándose hasta que se cumple una condición, como los ciclos while.
#2)
#A
def cargar_temperaturas():
    temperaturas = []  # Lista vacía donde se almacenarán las temperaturas
    i = 0  # Contador que indica el índice del día
    while i < 30:  # Bucle para procesar 30 días
        try:  # Bloque para manejar errores de entrada
            temp = float(input(f"Ingrese la temperatura para el día {i+1}: "))  # Entrada del usuario
            if -5 <= temp <= 45:  # Verifica si la temperatura está en el rango válido
                temperaturas.append(temp)  # Agrega la temperatura a la lista
                i += 1  # Incrementa el contador si la entrada es válida
            else:
                print("Temperatura fuera de rango (-5 a 45). Intente nuevamente.")  # Mensaje de error
        except ValueError:  # Captura errores si la entrada no es numérica
            print("Entrada inválida. Debe ingresar un número.")  # Mensaje de error
    return temperaturas  # Devuelve la lista de temperaturas



#B

def promedio_y_maxima(temperaturas):
    suma = 0  # Inicializa una variable para acumular la suma de las temperaturas
    max_temp = temperaturas[0]  # Asume que la primera temperatura es la mayor
    max_dia = 0  # El índice del día con la temperatura máxima, inicialmente el primer día
    for i, temp in enumerate(temperaturas):  # Recorre la lista con índices y valores
        suma += temp  # Suma cada temperatura al acumulador
        if temp > max_temp:  # Verifica si la temperatura actual es mayor que la máxima registrada
            max_temp = temp  # Actualiza la temperatura máxima
            max_dia = i  # Actualiza el índice del día con la temperatura máxima
    promedio = suma / len(temperaturas)  # Calcula el promedio dividiendo la suma por el número de días
    return promedio, max_dia  # Devuelve el promedio y el índice del día con la temperatura máxima

#C

def dias_sobre_promedio(temperaturas):
    promedio, _ = promedio_y_maxima(temperaturas)  # Llama a la función anterior para obtener el promedio
    print(f"Temperatura promedio: {promedio:.2f}")  # Muestra el promedio con dos decimales
    print("Días con temperatura mayor al promedio:")
    for i, temp in enumerate(temperaturas):  # Recorre la lista con índices y valores
        if temp > promedio:  # Verifica si la temperatura actual es mayor al promedio
            print(f"Día {i+1}: {temp}°C")  # Muestra el índice (ajustado) y la temperatura


#programa principal
def main():
    temperaturas = cargar_temperaturas()  # Llama a la función para cargar temperaturas
    promedio, max_dia = promedio_y_maxima(temperaturas)  # Calcula el promedio y el día de la máxima temperatura
    print(f"El promedio de las temperaturas es: {promedio:.2f}°C")  # Muestra el promedio
    print(f"La temperatura más alta fue el día {max_dia+1}")  # Muestra el día con la temperatura más alta
    dias_sobre_promedio(temperaturas)  # Llama a la función para mostrar los días con temperaturas mayores al promedio




#3


def contar_a(cadena):
    contador = 0  # Inicializa un contador en 0 para rastrear las apariciones de la letra 'a'
    for char in cadena:  # Itera sobre cada carácter de la cadena
        if char.lower() == 'a':  # Convierte el carácter a minúsculas y verifica si es 'a'
            contador += 1  # Incrementa el contador si la condición es verdadera
    return contador  # Devuelve el número total de apariciones de 'a'




#4
def prueba_contar_a():
    casos = [
        ("Programación", 2),  # Caso 1: Debe devolver 2
        ("Abracadabra", 5),  # Caso 2: Debe devolver 5
        ("Python", 0)  # Caso 3: Debe devolver 0
    ]
    for i, (entrada, esperado) in enumerate(casos):  # Itera sobre los casos de prueba
        resultado = contar_a(entrada)  # Llama a contar_a para obtener el resultado
        assert resultado == esperado, f"Error en caso {i+1}: esperado {esperado}, obtenido {resultado}"  # Verifica que el resultado sea el esperado
    print("Todos los casos de prueba pasaron.")  # Imprime un mensaje si todas las pruebas pasan

