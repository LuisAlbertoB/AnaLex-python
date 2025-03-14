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

# Función principal
def main():
    print("Bienvenido al Juego de Palabras")
    nivel = int(input("Selecciona un nivel (1-6): "))
    palabra = input("Ingresa una palabra: ")

    if nivel < 1 or nivel > 6:
        print("Nivel no válido.")
        return

    if automata(palabra, nivel):
        print(f"'{palabra}' es válida en el Nivel {nivel}.")
    else:
        print(f"'{palabra}' no es válida en el Nivel {nivel}.")

if __name__ == "__main__":
    main()