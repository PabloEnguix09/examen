from ast import If
import random


def choose_secret(filename):
    """Dado un nombre de fichero, esta funciÃ³n devuelve una palabra aleatoria de este fichero transformada a mayÃºsculas.
    Args:
      filename: El nombre del fichero. Ej. "palabras_reduced.txt"
    Returns:
      secret: Palabra elegida aleatoriamente del fichero transformada a mayÃºsculas. Ej. "CREMA"
    """
    f = open(filename, mode="rt", encoding="utf-8")
    lineas = []
    for linea in f.readlines():
        lineas.append(linea[:-1])
    secret = random.choice(lineas)
    f.close()
    return secret
    
def compare_words(word, secret):
    """Dadas dos palabras en mayÃºsculas (word y secret), esta funciÃ³n calcula las posiciones de las letras de word que aparecen en la misma posiciÃ³n en secret, y las posiciones de las letras de word que aparecen en secret pero en una posiciÃ³n distinta.
    Args:
      word: Una palabra. Ej. "CAMPO"
      secret: Una palabra. Ej. "CREMA"
    Returns:
      same_position: Lista de posiciones de word cuyas letras coinciden en la misma posiciÃ³n en secret. En el caso anterior: [0]
      same_letter: Lista de posiciones de word cuyas letras estÃ¡n en secret pero en posiciones distintas. En el caso anterior: [1,2]
    """
    same_position = []
    same_letter = []
    for letraSecret in secret:
        for letraWord in word:
            if letraSecret == letraWord:
                if word.index(letraWord) == secret.index(letraSecret):
                    same_position.append(word.index(letraWord))
                else:
                    same_letter.append(word.index(letraWord))
                break
    return same_position, same_letter


def print_word(word, same_letter_position, same_letter):
    """Dada una palabra, una lista same_position y otra lista same_letter, esta funciÃ³n crearÃ¡ un string donde aparezcan en mayÃºsculas las letras de la palabra que ocupen las posiciones de same_position, en minÃºsculas las letras de la palabra que ocupen las posiciones de same_letter y un guiÃ³n (-) en el resto de posiciones
    Args:
      word: Una palabra. Ej. "CAMPO"
      same_letter_position: Lista de posiciones. Ej. [0]
      same_letter: Lista de posiciones. Ej. [1,2]
    Returns:
      transformed: La palabra aplicando las transformaciones. En el caso anterior: "Cam--"
    """
    transformed = ""
    for letter in word:
        if word.index(letter) in same_letter_position:
            transformed += letter.upper()
        elif word.index(letter) in same_letter:
            transformed += letter.lower()
        else:
            transformed += "-"
    return transformed
    
def choose_secret_advanced(filename):
    """Dado un nombre de fichero, esta funciÃ³n filtra solo las palabras de 5 letras que no tienen acentos (Ã¡,Ã©,Ã­,Ã³,Ãº). De estas palabras, la funciÃ³n devuelve una lista de 15 aleatorias no repetidas y una de estas 15, se selecciona aleatoriamente como palabra secret.
    Args:
      filename: El nombre del fichero. Ej. "palabras_extended.txt"
    Returns:
      selected: Lista de 15 palabras aleatorias no repetidas que tienen 5 letras y no tienen acentos
      secret: Palabra elegida aleatoriamente de la lista de 15 seleccionadas transformada a mayÃºsculas
    """
    f = open(filename, mode="rt", encoding="utf-8")
    lineas = []
    for linea in f.readlines():
        lineas.append(linea)
    f.close()
    listaValidas = []
    selected = []
    for palabra in lineas:
        if len(palabra) == 6 and palabra.__contains__("á") == False and palabra.__contains__("é") == False and palabra.__contains__("í") == False and palabra.__contains__("ó") == False and palabra.__contains__("ú") == False:
            listaValidas.append(palabra[:-1])
    while True:
        palabra = random.choice(listaValidas)
        if palabra not in selected:
            selected.append(palabra)
        if len(selected) == 15:
            break
    secret = random.choice(selected)
    return selected, secret.upper()
 
def check_valid_word(selected):
    """Dada una lista de palabras, esta funciÃ³n pregunta al usuario que introduzca una palabra hasta que introduzca una que estÃ© en la lista. Esta palabra es la que devolverÃ¡ la funciÃ³n.
    Args:
      selected: Lista de palabras.
    Returns:
      word: Palabra introducida por el usuario que estÃ¡ en la lista.
    """
    while True:
        word = input("Introduce una palabra de la lista: ")
        for palabra in selected:
            if word == palabra:
                return word

if __name__ == "__main__":
    selected, secret = choose_secret_advanced("palabras_extended.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    print("Lista de palabras seleccionadas: ", selected)#Debug: esto es para que sepas la lista de la que tienes que decir una palabra
    check_valid_word(selected)
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        print("sPos=", same_position)
        print("sLet=", same_letter)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)
"""
    secret=choose_secret("palabras_reduced.txt")
    print("Palabra a adivinar: "+secret)#Debug: esto es para que sepas la palabra que debes adivinar
    for repeticiones in range(0,6):
        word = input("Introduce una nueva palabra: ")
        same_position, same_letter = compare_words(word, secret)
        print("sPos=", same_position)
        print("sLet=", same_letter)
        resultado=print_word(word, same_position, same_letter)
        print(resultado)
        if word == secret:
            print("HAS GANADO!!")
            exit()
    print("LO SIENTO, NO LA HAS ADIVINIDADO. LA PALABRA ERA "+secret)   

"""