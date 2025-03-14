import json
import re

class Lexer:
    def __init__(self, rules):  # Corregido: __init__ con doble guion bajo
        self.rules = rules

    def tokenize(self, text):
        tokens = []
        while text:
            for pattern, token_type in self.rules:
                regex = re.compile(pattern)
                match = regex.match(text)
                if match:
                    value = match.group(0)
                    tokens.append((token_type, value))
                    text = text[len(value):]
                    break
            else:
                raise ValueError(f"Invalid text: {text}")
        return tokens

def cargar_niveles():
    with open("niveles.json", "r") as file:
        return json.load(file)

def verificar_palabra(input_text, nivel):
    patron = nivel["patron"]

    # Definir reglas para el lexer
    rules = [(patron, 'WORD')]

    lexer = Lexer(rules)
    try:
        tokens = lexer.tokenize(input_text)
        if any(token_type == 'WORD' for token_type, _ in tokens):
            return True, "✅ ¡Correcto! Palabra válida."
        else:
            return False, "❌ Incorrecto. La palabra no cumple con el patrón."
    except ValueError as e:
        return False, f"❌ Error: {e}"

def jugar_nivel(nivel):
    print(f"\n--- Nivel {nivel['nivel']} ---")
    print(f"Descripción: {nivel['descripcion']}")
    print(f"Patrón: {nivel['patron']}")

    palabras_adivinadas = 0
    while palabras_adivinadas < 6:
        input_text = input(f"Escribe una palabra ({palabras_adivinadas + 1}/6): ")
        correcto, mensaje = verificar_palabra(input_text, nivel)
        print(mensaje)
        if correcto:
            palabras_adivinadas += 1
        else:
            print("Sigue intentando.")

    print("¡Has adivinado 6 palabras! Pasas al siguiente nivel.")
    return True

def main():
    niveles_data = cargar_niveles()
    niveles = niveles_data["niveles"]
    nivel_actual = 0

    while nivel_actual < len(niveles):
        nivel = niveles[nivel_actual]
        if jugar_nivel(nivel):
            nivel_actual += 1
        else:
            print("Sigue intentando.")

    print("\n¡Felicidades! Has completado todos los niveles.")

if __name__ == "__main__":  # Corregido: __name__ y __main__ con doble guion bajo
    main()