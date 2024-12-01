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


# Interaccion con el tablero
def click_tablero(coordenadas_click, tamaño_tablero, ancho_casillero, ANCHO_PANTALLA, ALTO_PANTALLA, barcos_casilleros, matriz, puntajes, usuario, barcos_averiados, ventana, puntaje_actual,  x_puntajes, y_puntajes, color_barco_tocado, color_agua, partes_barco_coordenadas):
    
    # !!!
    # VER DE TRAER LA LISTA DE RECTS sola y no generar una cada vez que hace click en el tablero
    lista_rects_valores = dibuja_rects(tamaño_tablero, ancho_casillero, ventana, posicion_x=ANCHO_PANTALLA/5, posicion_y=ALTO_PANTALLA/7)
    # !!!
    #     

    for i in range(len(lista_rects_valores)): # cambiar al for
        rect_seleccionado = lista_rects_valores[i]
        if rect_seleccionado.collidepoint(coordenadas_click):
        # veo si hay un barco en ese casillero y su valor
            casillero_tocado = barcos_casilleros[i] # Una parte del barco (un casillero)
            barco_valor = barcos_casilleros[i]['valor']
            print(f'casillero_tocado >> {casillero_tocado}')
            
            """ if barco_id != 0:
                barcos_averiados[barco_id] += 1 # suma una parte averiada al barco """

            # Verificamos si el barco está hundido
            """ resultado = obtener_partes_barco(barco_id, barcos_casilleros, barcos_averiados)
            barco_hundido = resultado[0]
            cant_partes_hundidas = resultado[1]
            if barco_hundido: # si esta hundido
                puntaje_hundido = 0
                print(f"El barco {barco_id} está hundido!")
                puntaje_hundido += cant_partes_hundidas * 10  # Suma 10 puntos por cada parte tocada
                actualizar_puntaje(usuario, puntajes, puntaje_hundido)
                print(f"Puntaje aumentado a {puntaje}")
            else:
                print(f"El barco {barco_id} No esta hundido") """
            
            if barco_valor != 0:  # Si hay un barco
                if barco_valor == 9: # Si ya estaba tocado/averiado
                    print(f' Barco averiado! en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y}')
                else:
                    print(f' Tocaste un barco en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y} ')
                    print(f' El barco es: {casillero_tocado} ')
                    barcos_casilleros[i]['valor'] = 9 # uso 9 para barcos tocados/heridos
                    # Modifica la matriz de barcos
                    matriz_modificada = modifica_matriz_disparos(matriz, casillero_tocado)
                    
                    # MODIFICAR EL COLOR AL RECT que contiene el texto
                    pygame.draw.rect(ventana, color_barco_tocado, rect_seleccionado)  

                    # MODIFICA EL PUNTAJE DEL USUARIO
                    nuevo_puntaje = 5
                    actualizar_puntaje(usuario, puntajes, nuevo_puntaje)
                    
            else:
                pygame.draw.rect(ventana, color_agua, rect_seleccionado)  # Redibujar el rectángulo con el nuevo color
                print(f' Agua en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y}')
                # MODIFICA EL PUNTAJE DEL USUARIO - 1
                nuevo_puntaje = -1
                actualizar_puntaje(usuario, puntajes, nuevo_puntaje)

            # Actualiza el marcador de los puntajes
            #actualiza_marcador(puntajes)
            actualiza_marcador(puntajes, ventana, puntaje_actual, x_puntajes, y_puntajes)
            pygame.display.update(rect_seleccionado)  # Solo actualiza el área del clic

            break  # Salir si ya toco un casillero 

    return puntajes

def dibuja_rects(tamaño_tablero, ancho_casillero, ventana, posicion_x, posicion_y): # Dibujo el tablero con sus rectangulos sin valores, para poder machear el click del usuario en estos

    #lista_rects = [] # lista de rectangulos
    rectangulos = []
    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            
            x_rect = posicion_x + columna * ancho_casillero
            y_rect = posicion_y + fila * ancho_casillero
            rect_tablero = pygame.Rect(x_rect, y_rect, ancho_casillero, ancho_casillero)
            rectangulo_tablero = pygame.draw.rect(ventana, fondo_color_tablero, rect_tablero, 1)  # Dibuja las líneas del tablero
            rectangulos.append(rectangulo_tablero)
            
            #lista_rects.append(rect_tablero) # lista de rectangulos
    return rectangulos


""" 
Si estás trabajando con música de fondo, usa mixer.music, ya que está optimizado para manejar archivos de mayor tamaño. Por otro lado, mixer.Sound es mejor para efectos cortos y repetitivos.
 """