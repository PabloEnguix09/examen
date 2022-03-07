import random

def encontrar_menores(diccionario,letra):
    """Dado un diccionario de palabras, y una letra, esta funciÃ³n devuelve la lista de palabras que empiezan por una letra que alfabÃ©ticamente estÃ¡ antes que la indicada.
    Args:
      diccionario
      letra
    Returns:
      resultado: ej. ['AUNQUE','ABINAR']
    """
    resultado=[]
    for clave in diccionario:
        for palabra in diccionario[clave]:
            if palabra[0] < letra:
                resultado.append(palabra)
    return resultado
    #El problema aquí era que cuando encontraba una palabra válida declaraba la lista de resultados y ponía solo la última
    #La solución fue declarar la lista de resultados al principio de la función

def add_client(clients_list,nif,name,address,phone,email):
    """Dado un diccionario de clientes y datos de un nuevo cliente, esta funciÃ³n inserta estos datos como un nuevo cliente.
    Args:
      diccionario
      nif
      name 
      address
      phone
      email
    """
    clients_list[nif] = {
        'name': name,
        'address': address,
        'phone': phone,
        'email': email
    }
    #El problema aquí era que hacía un diccionario dentro del diccionario, y ese no es el formato adecuado en esta lista
    #La solución fue borrar la key de nif y dejar solamente los valores que habían dentro de ella

def repartir_cartas(cartas_iniciales,repeticiones):
    """Dada una baraja de cartas iniciales y un nÃºmero de repeticiones, esta funciÃ³n selecciona 5 cartas aleatorias de esta baraja y las mete en un diccionario llamado combinaciones. El proceso se repite tantas veces como repeticiones se indiquen.
    Args:
      cartas_iniciales
      repeticiones
    Returns:
      combinaciones: ej. {'repeticion1': ['contable', 'alguacil', 'asesino', 'cardenal', 'obispo']}
    """    
    combinaciones={}
    for i in range(1,repeticiones+1):
        cartas_aleatorias = cartas_iniciales 
        combinaciones["repeticion"+str(i)]=[]
        for j in range(0,5):
            carta=random.choice(cartas_aleatorias)
            combinaciones["repeticion"+str(i)].append(carta)
    return combinaciones
    #El problema aquí era que borraba la carta que elegía de las combinaciones, por lo que al habe más de 2 combinaciones de 5 cartas en una baraja de 10 cartas, te quedabas sin cartas
    #La solución fue hacer que no borrara la carta que escogía