""" import random
import pygame.mixer as mixer

#Musica del juego
def sonido_juego ():
    mixer.init()
    ruta_musica = 'teoria_juegos/Batalla_Naval/archivos_naval/naval_music.mp3'
    sonido = mixer.Sound(ruta_musica)
    sonido.set_volume(0.1)
    #sonido.play()

def inicializar_matriz (filas: int, columnas:int, valor_inicial: any)-> list:
    matriz = []
    for _ in range (filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    
    return matriz

def mostrar_tablero (matriz:list)-> list:    
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print (matriz[i][j], end=' ')
        print('')

def crea_navios_automaticamente():

    navios = [] # lista que contiene listas[dict] >>> navios[[{},{},{},{}], [{},{},{}], [{},{}], [{}]]
    estados_navios = ['nuevo','herido','hundido']

    for _ in range (4):
        navios += [[]]
    
    tipos_navios = ['submarinos', 'destructores', 'cruceros', 'acorazados']
    
    for tipo in tipos_navios:
        match tipo:
            case 'submarinos':
                # crea 4 
                subm = {
                    'nombre': 's1',
                    'tamaño': 1,
                    'daño': int,
                    'vida': int,
                    'estado': estados_navios[0]
                    }
                navios[0] += [subm] * 4
                
            case 'destructores':
                # crea 3
                dest = {
                    'nombre': 'd1',
                    'tamaño': 2,
                    'daño': int, 
                    'vida': int,
                    'estado': estados_navios[0]
                    }
                navios[1] += [dest] * 3

            case 'cruceros':
                # crea 2 
                cruc = {
                'nombre': 'c1',
                'tamaño': 3,
                'daño': int, 
                'vida': int,
                'estado': estados_navios[0]
                }
                navios[2] += [cruc] * 2

            case 'acorazados':
                # crea 1 
                acor = {
                'nombre': 'a1',
                'tamaño': 4,
                'daño': int, 
                'vida': int,
                'estado': estados_navios[0]
                }
                navios[3] += [acor] * 1

    return navios


def mensaje_bienvenida ()-> str:
    mensaje = '\nBienvenido/a al Juego de la Batalla Naval! \n'
    print(mensaje)


def muestra_flota_logica(flota:list):
    print('\n\n')
    for i in range (len(flota)):
        print (flota[i], end=' ')
        print ('\n-----------------------------------------------')


def muestra_flota_x_navio(flota:list):
    print('\n\n')
    for i in range (len(flota)):

        match flota[i][0]['nombre']:
            case 's1':
                print('\n||| Submarinos |||')
            case 'd1':
                print('\n||| Destructores |||')
            case 'c1':
                print('\n||| Cruceros |||')
            case 'a1':
                print('\n||| Acorazados |||')


        for j in range (len(flota[i])):
            print(flota[i][j], end= '\n')
    print('\n')


parametros_juego = {
    'Nivel': 'Facil',
    'Nivel': 'Medio',
    'Nivel': 'Dificil'

}

# Funcion para encontrar un barco dentro de la flota con parametros
def buscar_barco (flota:list, tipo_navio:str, nro_navio:int):
    nro_navio = nro_navio-1

    match tipo_navio:
        case 'submarino':
            barco_buscado = flota[0][nro_navio]
        case 'destructor':
            barco_buscado = flota[1][nro_navio]
        case 'crucero':
            barco_buscado = flota[2][nro_navio]
        case 'acorazado':
            barco_buscado = flota[3][nro_navio]

    return barco_buscado

def comienza_juego(flota:list, inicializar_matriz:callable, nivel:str):
    match nivel:
        case 'Facil':
            matriz = inicializar_matriz(10,10,0)
        case 'Medio':
            matriz =  inicializar_matriz(20,20,0) 
        case 'Dificil':
            matriz =  inicializar_matriz(40,40,0) 
    return matriz

def generar_pos_aleatoria (filas:int, columnas:int)-> tuple:
    pos_fila = random.randint(0,filas-1)
    pos_columna = random.randint(0,columnas-1)
    
    posicion = (pos_fila, pos_columna)
    return posicion

def validar_ubicacion(barco, posicion, matriz)-> bool:
    # se puede en la ubicacion dada, colocar el barco dado?
    pos_f = posicion[0]
    pos_c = posicion[1]
    # ademas de que sea 0 (libre) ver si hay espacio hacia la derecha para ubicarlo
        # recorro el resto de la fila buscando si hay espacio libre para el largo de ese barco
    # la posicion buscada esta disponible?
    posicion_libre = False
    if matriz[pos_c][pos_f] == 0:
        posicion_libre = True
    else:
        posicion_libre = False

    # hay espacio a la derecha de la fila suficiente?
    espacio_fila = False

    # si ambos son True entonces ubicar el barco es posible (True)
    if posicion_libre == True and espacio_fila == True:
        ubicacion = True
    else:
        ubicacion = False

    return ubicacion

def ubicar_barcos_aleatoriamente(flota:list, matriz:list, filas:int, columnas:int):
    cont_lleno = 0
    cont_libre = 0
    for i in range (len(flota)): # tipos de barcos
        for j in range (len(flota[i])): # barcos por tipo
            # tomo un barco y su tamaño
            barco = flota[i][j]
            largo_barco = flota[i][j]['tamaño']

            # una vez que tengo un barco de la flota, lo ubico aleatoriamente en la matriz
            # necesito *generar una posicion(fila, columna) random y *validar si se puede ubicar ahi.           
            # ubico el barco en la posicion generada
            match largo_barco:
                case 1:
                    casillero_libre = False
                    while casillero_libre == False:
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]

                        if matriz[pos_fila][pos_columna] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 1 # ubico el barco
                        else:
                            cont_lleno += 1
                    
                case 2:
                    casillero_libre = False
                    while casillero_libre == False:
                    
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]
                        while pos_columna == 9:
                            posicion = generar_pos_aleatoria(filas, columnas)
                            pos_fila = posicion[0]
                            pos_columna = posicion[1]

                        if matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 2 
                            matriz[pos_fila][pos_columna+1] = 2 
                        else:
                            cont_lleno += 1
             
                case 3:
                    casillero_libre = False
                    while casillero_libre == False:
                    
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]
                        while pos_columna == 8 or pos_columna == 9:
                            posicion = generar_pos_aleatoria(filas, columnas)
                            pos_fila = posicion[0]
                            pos_columna = posicion[1]
                        
                        if matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0 and matriz[pos_fila][pos_columna+2] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 3 
                            matriz[pos_fila][pos_columna+1] = 3 
                            matriz[pos_fila][pos_columna+2] = 3
                        else:
                            cont_lleno += 1
                case 4:
                    casillero_libre = False
                    while casillero_libre == False:
                    
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]
                        while pos_columna == 7 or pos_columna == 8 or pos_columna == 9:
                            posicion = generar_pos_aleatoria(filas, columnas)
                            pos_fila = posicion[0]
                            pos_columna = posicion[1]
                        
                        if matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0 and matriz[pos_fila][pos_columna+2] == 0 and matriz[pos_fila][pos_columna+3] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 4 
                            matriz[pos_fila][pos_columna+1] = 4 
                            matriz[pos_fila][pos_columna+2] = 4
                            matriz[pos_fila][pos_columna+3] = 4
                        else:
                            cont_lleno += 1
    return matriz    
            
def a_jugar ():
        
    # Cuando comienza el juego: crea la flota, la matriz vacia, y finalmente ubica los barcos aleatoriamente
    print('\n Comienza el juego!  \n')
    flota = crea_navios_automaticamente()
    matriz_comienzo = comienza_juego(flota, inicializar_matriz, 'Facil')
    mostrar_tablero(matriz_comienzo)
    print('\nUbico barcos')
    matriz_barcos = ubicar_barcos_aleatoriamente(flota, matriz_comienzo, 10, 10)
    mostrar_tablero(matriz_comienzo)
    return matriz_barcos






# Configuraciones para cada estado_pantalla

def saliendo(nick:str)-> str:
    mensaje = f'\n**********\nSaliendo del juego! hasta la proxima {nick}...\n**********\n'
    print(mensaje)
    return mensaje


 """


""" barco_rect = {}
barco_rect['x':rect_tablero.x]
barco_rect['y':rect_tablero.y]
barco_rect['valor':barco_valor]
barco_rect['id':id_barco]
barco_rect['fila':fila]
barco_rect['columna':columna] 
"""
                
### funcion original
""" def ubicar_barcos_aleatoriamente(flota:list, matriz:list, filas:int, columnas:int):
    cont_lleno = 0
    cont_libre = 0
    for i in range (len(flota)): # tipos de barcos
        for j in range (len(flota[i])): # barcos por tipo
            # tomo un barco y su tamaño
            barco = flota[i][j]
            largo_barco = flota[i][j]['tamaño']

            # una vez que tengo un barco de la flota, lo ubico aleatoriamente en la matriz
            # necesito *generar una posicion(fila, columna) random y *validar si se puede ubicar ahi.           
            # ubico el barco en la posicion generada
            match largo_barco:
                case 1:
                    casillero_libre = False
                    while casillero_libre == False:
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]

                        if matriz[pos_fila][pos_columna] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 1 # ubico el barco
                        else:
                            cont_lleno += 1
                    
                case 2:
                    casillero_libre = False
                    while casillero_libre == False:
                    
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]
                        while pos_columna == 9:
                            posicion = generar_pos_aleatoria(filas, columnas)
                            pos_fila = posicion[0]
                            pos_columna = posicion[1]

                        if matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 2 
                            matriz[pos_fila][pos_columna+1] = 2 
                        else:
                            cont_lleno += 1
             
                case 3:
                    casillero_libre = False
                    while casillero_libre == False:
                    
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]
                        while pos_columna == 8 or pos_columna == 9:
                            posicion = generar_pos_aleatoria(filas, columnas)
                            pos_fila = posicion[0]
                            pos_columna = posicion[1]
                        
                        if matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0 and matriz[pos_fila][pos_columna+2] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 3 
                            matriz[pos_fila][pos_columna+1] = 3 
                            matriz[pos_fila][pos_columna+2] = 3
                        else:
                            cont_lleno += 1
                case 4:
                    casillero_libre = False
                    while casillero_libre == False:
                    
                        posicion = generar_pos_aleatoria(filas, columnas)
                        pos_fila = posicion[0]
                        pos_columna = posicion[1]
                        while pos_columna == 7 or pos_columna == 8 or pos_columna == 9:
                            posicion = generar_pos_aleatoria(filas, columnas)
                            pos_fila = posicion[0]
                            pos_columna = posicion[1]
                        
                        if matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0 and matriz[pos_fila][pos_columna+2] == 0 and matriz[pos_fila][pos_columna+3] == 0:
                            cont_libre += 1 
                            casillero_libre = True # Si el casillero esta vacio
                            matriz[pos_fila][pos_columna] = 4 
                            matriz[pos_fila][pos_columna+1] = 4 
                            matriz[pos_fila][pos_columna+2] = 4
                            matriz[pos_fila][pos_columna+3] = 4
                            
                        else:
                            cont_lleno += 1
    return matriz    

 """



""" 
lista_posiciones_barcos = []
posicion_parte_barco = (pos_fila, pos_columna)
parte_del_barco = (1, 4) # parte 1 de 4 totales
# necesito generar un id para cada barco (pero un barco puede tener el mismo id para varias partes del mismo barco.)
barco_datos = {'id_barco':id_barco, 'coordenadas':posicion_parte_barco, 'partes_del_barco':parte_del_barco}
lista_posiciones_barcos.append(barco_datos)
 """

####### LABURAR SOBRE ESTE CODIGO >>>> 

""" 
import random  # Necesario para generar IDs si no lo tienes definido

def ubicar_barcos_aleatoriamente_MODIFICADA(flota: list, matriz: list, filas: int, columnas: int):
    cont_lleno = 0
    cont_libre = 0
    lista_posiciones_barcos = []  # Lista para almacenar los datos de los barcos
    id_barco = 1  # ID inicial para los barcos

    for i in range(len(flota)):  # tipos de barcos
        for j in range(len(flota[i])):  # barcos por tipo
            # Tomo un barco y su tamaño
            barco = flota[i][j]
            largo_barco = flota[i][j]['tamaño']

            # Ubico el barco en la matriz
            casillero_libre = False
            while not casillero_libre:
                posicion = generar_pos_aleatoria(filas, columnas)
                pos_fila, pos_columna = posicion

                # Validar espacios según el tamaño del barco
                if largo_barco == 1:
                    if matriz[pos_fila][pos_columna] == 0:
                        casillero_libre = True
                        matriz[pos_fila][pos_columna] = largo_barco
                        lista_posiciones_barcos.append({
                            'id_barco': id_barco,
                            'coordenadas': (pos_fila, pos_columna),
                            'partes_del_barco': (1, 1)  # Parte 1 de 1
                        })
                elif largo_barco == 2:
                    if pos_columna < columnas - 1 and matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna + 1] == 0:
                        casillero_libre = True
                        for parte in range(largo_barco):
                            matriz[pos_fila][pos_columna + parte] = largo_barco
                            lista_posiciones_barcos.append({
                                'id_barco': id_barco,
                                'coordenadas': (pos_fila, pos_columna + parte),
                                'partes_del_barco': (parte + 1, largo_barco)
                            })
                elif largo_barco == 3:
                    if pos_columna < columnas - 2 and all(matriz[pos_fila][pos_columna + k] == 0 for k in range(largo_barco)):
                        casillero_libre = True
                        for parte in range(largo_barco):
                            matriz[pos_fila][pos_columna + parte] = largo_barco
                            lista_posiciones_barcos.append({
                                'id_barco': id_barco,
                                'coordenadas': (pos_fila, pos_columna + parte),
                                'partes_del_barco': (parte + 1, largo_barco)
                            })
                elif largo_barco == 4:
                    if pos_columna < columnas - 3 and all(matriz[pos_fila][pos_columna + k] == 0 for k in range(largo_barco)):
                        casillero_libre = True
                        for parte in range(largo_barco):
                            matriz[pos_fila][pos_columna + parte] = largo_barco
                            lista_posiciones_barcos.append({
                                'id_barco': id_barco,
                                'coordenadas': (pos_fila, pos_columna + parte),
                                'partes_del_barco': (parte + 1, largo_barco)
                            })
            id_barco += 1  # Incremento el ID para el siguiente barco
    return matriz, lista_posiciones_barcos
 """



""" partes_barcos = ['popa', 'proa', 'estribor', 'babor']
for i in range (len(partes_barcos)):
    cada_parte = partes_barcos[i]
    print(f'{i} -- {cada_parte}')
print(len(partes_barcos))
 """
 
""" largo_barco = 4
for parte in range(largo_barco):
    print(parte) """

print(len(range(10)))