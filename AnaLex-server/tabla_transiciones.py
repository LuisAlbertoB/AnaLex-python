tabla = {
    # Nivel 1: Palabras de 5 letras que empiezan con 'a'
    (0, 'a', 1): 1,
    (0, 'A', 1): 1,
    (1, 'a-z', 1): 2,
    (2, 'a-z', 1): 3,
    (3, 'a-z', 1): 4,
    (4, 'a-z', 1): 5,
    # Ej. Palabra: Abeja/abeja.

    # Nivel 2: Palabras de 7 letras que terminan con 'o'
    (0, 'a-z', 2): 1,
    (0, 'A-Z', 2): 1,
    (1, 'a-z', 2): 2,
    (2, 'a-z', 2): 3,
    (3, 'a-z', 2): 4,
    (4, 'a-z', 2): 5,
    (5, 'a-z', 2): 6,
    (6, 'o', 2): 7,
    # Ej. Palabra: Carroño/carroño.

    # Nivel 3: Palabras de 6 letras que empiezen con 'll'
    (0, 'l', 3): 1,
    (0, 'L', 3): 1,
    (1, 'l', 3): 2,
    (2, 'a-z', 3): 3,
    (3, 'a-z', 3): 4,
    (4, 'a-z', 3): 5,
    (5, 'a-z', 3): 6,
    # Ej. Palabra: Llamar/llamar.


    # Nivel 4: Palabras de 6 letras que terminan en 'ción'
    (0, 'a-z', 4): 1,
    (0, 'A-Z', 4): 1,
    (1, 'a-z', 4): 2,
    (2, 'c', 4): 3,
    (3, 'i', 4): 4,
    (4, 'o', 4): 5,
    (4, 'ó', 4): 5,
    (5, 'n', 4): 6,
    # Ej. Palabra: Accion/Acción/accion/acción.

    # Nivel 5: Palabras de 7 letras que empiezan con 'b', vocal y terminan con 'a'
    (0, 'b', 5): 1,
    (0, 'B', 5): 1,
    (1, 'a', 5): 2,
    (1, 'e', 5): 2,
    (1, 'i', 5): 2,
    (1, 'o', 5): 2,
    (1, 'u', 5): 2,
    (2, 'a-z', 5): 3,
    (2, 'a-z', 5): 3,
    (3, 'a-z', 5): 4,
    (4, 'a-z', 5): 5,
    (5, 'a-z', 5): 6,
    (6, 'a-z', 5): 7,
    # Ej. Palabra: Batalla/batalla.

    # Nivel 6: Palabras de 5 letras que empiezan con 'p', vocal y terminan con 'o'
    (0, 'p', 6): 1,
    (0, 'P', 6): 1,
    (1, 'a', 6): 2,
    (1, 'e', 6): 2,
    (1, 'i', 6): 2,
    (1, 'o', 6): 2,
    (1, 'u', 6): 2,
    (2, 'a-z', 6): 3,
    (3, 'a-z', 6): 4,
    (4, 'o', 6): 5,
    # Ej. Palabra: Pablo/pablo.
}

# Estados finales para cada nivel
estados_finales = {
    1: 5,
    2: 7,
    3: 6,
    4: 6,
    5: 7,
    6: 5,
}