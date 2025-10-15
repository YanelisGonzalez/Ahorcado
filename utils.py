# Declaro todas las variables necesarias para el juego

import random

def jugar_ahorcado(max_errores=6):
    print('🎯 Bienvenido al juego del AHORCADO')

    # Lista de palabras posibles
    lista_palabras = ['python', 'ciencia', 'datos', 'programacion', 'analista']
    palabra_secreta = random.choice(lista_palabras) # De la lista de palabras, escoge una aleatoreamente
    letras_acertadas = [ '_' ] * len(palabra_secreta) # Crea una lista con tantos guiones bajos como letras tenga la palabra secreta
    letras_intentadas = [] # Lista vacía para asegurar que no se repitan las letras
    errores = 0
    max_errores = 6 # Número de errores permitidos, también se puede ajustar la dificultad del juego cambiando este valor

    print('Adivina la palabra secreta. Tienes', max_errores, 'intentos.')
    print(*letras_acertadas) # Muestra los guines bajos separados por espacios

    while errores < max_errores and '_' in letras_acertadas:
        letra = input('Introduce una letra').lower()

        # Validar que se introduzca una letra y no otra cosa
        if len(letra) != 1 or not letra.isalpha():
            print('❌ Por favor, introduzca solo una letra válida')
            continue
        else:
            letras_intentadas.append(letra)

        # Comprobar que la letra está en la palabra secreta
        if letra in palabra_secreta:
            print('✅ ¡Bien hecho! La letra', letra, 'está en la palabra secreta')
            for i, caracter in enumerate(palabra_secreta):
                if caracter == letra:
                    letras_acertadas[i] = letra
        else:
            errores += 1
            print('❌ La letra', letra, 'no está en la palabra secreta. Te quedan', max_errores, 'intentos.')
        print(*letras_acertadas)

    # Fin del juego
    if '_' not in letras_acertadas:
        print('🎉 ¡FELICIDADES! Has adivinado la palabra', palabra_secreta)
    else:
        print(' 💀 FIN DEL JUEGO. Has superado el número máximo de errores.')
        print('La palabra secreta era:', palabra_secreta)