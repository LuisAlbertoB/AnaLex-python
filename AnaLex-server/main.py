# main.py
from tabla_transiciones import tabla, estados_finales

def automata(cadena, nivel):
    estado = 0  # Estado inicial
    estado_final = estados_finales[nivel]  # Estado final para el nivel

    for caracter in cadena:
        # Buscar la transición correspondiente
        transicion = None
        for (estado_actual, rango, nivel_actual), estado_siguiente in tabla.items():
            if estado_actual == estado and nivel_actual == nivel:
                if rango == caracter or (rango == 'a-z' and caracter.islower()) or (rango == 'A-Z' and caracter.isupper()):
                    transicion = estado_siguiente
                    break

        if transicion is not None:
            estado = transicion
        else:
            return False  # Estado de error

    return estado == estado_final  # Verifica si llegó al estado final

# Función para mostrar las instrucciones del nivel
def mostrar_instrucciones(nivel):
    instrucciones = {
        1: "Nivel 1: Palabras de 5 letras que empiezan con 'a'.",
        2: "Nivel 2: Palabras de 7 letras que terminan con 'o'.",
        3: "Nivel 3: Palabras de 6 letras que empiezen con 'll'.",
        4: "Nivel 4: Palabras de 6 letras que contienen 'ción'.",
        5: "Nivel 5: Palabras de 7 letras que empiezan con 'b', luego vocal vocal y terminan con 'a'.",
        6: "Nivel 6: Palabras de 5 que empiezan con 'p', luego una vocal y terminan con 'o'.",
    }
    print(instrucciones[nivel])

# Función principal
def main():
    print("Bienvenido al Juego de Palabras")
    print("Instrucciones generales:")
    print("- Debes ingresar una palabra que cumpla con las reglas del nivel actual.")
    print("- Si la palabra es válida, avanzarás al siguiente nivel.")
    print("- Si la palabra no es válida, tendrás que intentarlo de nuevo.")
    print("- ¡Buena suerte!\n")

    nivel_actual = 1  # Comenzar en el nivel más bajo
    nivel_maximo = 6  # Nivel más alto

    while nivel_actual <= nivel_maximo:
        # Mostrar instrucciones del nivel actual
        mostrar_instrucciones(nivel_actual)

        palabra = input(f"Ingresa una palabra para el Nivel {nivel_actual}: ")

        if automata(palabra, nivel_actual):
            print(f"¡Correcto! '{palabra}' es válida en el Nivel {nivel_actual}.\n")
            nivel_actual += 1  # Avanzar al siguiente nivel
        else:
            print(f"Incorrecto. '{palabra}' no es válida en el Nivel {nivel_actual}. Intenta de nuevo.\n")

    print("¡Felicidades! Has completado todos los niveles. ¡Eres un campeón/ona de las palabras!")

if __name__ == "__main__":
    main()