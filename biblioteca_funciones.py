import random
import pygame.mixer as mixer
import pygame
from colores_naval import *

#pygame.init()

#Musica del juego
def sonido_juego ():
    mixer.init()
    ruta_musica = 'teoria_juegos/Batalla_Naval/archivos_naval/naval_music.mp3'
    sonido = mixer.Sound(ruta_musica)
    sonido.set_volume(0.4)
    #sonido.play()

# Inicializa matriz
def inicializar_matriz (filas: int, columnas:int, valor_inicial: any):
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


def menu_juego(ventana, imagen_barcos, nivel, jugar, puntajes_historicos, salir, color_boton_nivel, color_boton_jugar, color_boton_puntaje, color_boton_salir, y_boton, x_boton):
    ventana.blit(imagen_barcos, (0,0)) # Imagen de Fondo
    imagen_barcos.set_alpha(255)
    botones_menu_activos(nivel, jugar, puntajes_historicos, salir, x_boton)
    pygame.draw.rect(ventana, color_boton_nivel, nivel) # con el objeto nivel, dibuja el rectangulo
    pygame.draw.rect(ventana, color_boton_jugar, jugar)
    pygame.draw.rect(ventana, color_boton_puntaje, puntajes_historicos)
    pygame.draw.rect(ventana, color_boton_salir, salir)
    
    txt_nivel = fuente_botones.render('Nivel', False, color_letra_botones)
    ventana.blit(txt_nivel, (150, y_boton + 10))
    txt_jugar = fuente_botones.render('Jugar', False, color_letra_botones)
    ventana.blit(txt_jugar, (300, y_boton + 10))
    txt_puntajes = fuente_botones.render('Ver Puntajes', False, color_letra_botones)
    ventana.blit(txt_puntajes, (420, y_boton + 10))
    txt_salir = fuente_botones.render('Salir', False, color_letra_botones)
    ventana.blit(txt_salir, (600, y_boton + 10))
    
    # Ingrese su usuario, lo guarda y empieza el juego
    usuario = 'Mauro'
    return usuario


def dibujar_botones_juego(ventana:pygame.Surface, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha):
    # Botones a la derecha del tablero    
    pygame.draw.rect(ventana, color_boton_salir, salir_jugando)
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    pygame.draw.rect(ventana, color_boton_salir, reiniciar_jugando)
    pygame.draw.rect(ventana, color_boton_salir, volver_menu)

    txt_puntaje_actual = fuente_puntaje_actual.render('0000', False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actual, (x_puntajes + 35, y_puntajes + 15))
    txt_salir_jugando = fuente_botones.render('Salir', False, color_letra_botones)
    ventana.blit(txt_salir_jugando, (x_boton_derecha + 35, y_boton_derecha+10))
    txt_reiniciar_jugando = fuente_botones.render('Reiniciar', False, color_letra_botones)
    ventana.blit(txt_reiniciar_jugando, (x_boton_derecha + 22, y_boton_derecha + 110))
    txt_volver_menu = fuente_botones.render('Volver', False, color_letra_botones)
    ventana.blit(txt_volver_menu, (x_boton_derecha + 30, y_boton_derecha + 210))

# Botones del menu inactivos
def botones_menu_inactivos(nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA):
    # LOS SACO DE LA PANTALLA
    nivel.x = ANCHO_PANTALLA-1000
    jugar.x = ANCHO_PANTALLA-1000
    puntajes_historicos.x = ANCHO_PANTALLA-1000
    salir.x = ANCHO_PANTALLA-1000

def botones_menu_activos (nivel, jugar, puntajes_historicos, salir, x_boton):
    # vuelven a su posicion original activos.
    nivel.x = x_boton
    jugar.x = x_boton + 150
    puntajes_historicos.x = x_boton + 300
    salir.x = x_boton + 450


def jugando (tamaño_tablero, ancho_casillero, ventana, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, ALTO_PANTALLA, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha):
    ventana.fill(fondo_ventana) # detras de la imagen fondo negro
    ventana.blit(imagen_fondo_oceano, (0,0)) # imagen fondo del tablero 
    botones_menu_inactivos(nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA) # Desactiva los botones del menu al comenzar el juego
    dibujar_botones_juego(ventana, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha)
    matriz_barcos_ubicados = a_jugar() # Se genera la logica del juego.
    retorno_lista_rects = dibuja_tablero(tamaño_tablero, ancho_casillero, ventana, posicion_x=ANCHO_PANTALLA/5, posicion_y=ALTO_PANTALLA/7, matriz_barcos= matriz_barcos_ubicados) # Se prepara el tablero
    lista_rects_generados = retorno_lista_rects[0] 
    barcos_xy_valor = retorno_lista_rects[1]
    barcos_averiados = retorno_lista_rects[2]
    
    datos_retorno = [matriz_barcos_ubicados, lista_rects_generados, barcos_xy_valor, barcos_averiados]
    return datos_retorno

def dibuja_tablero(tamaño_tablero, ancho_casillero, ventana, posicion_x, posicion_y, matriz_barcos): # dibuja el tablero completo con valores

    lista_barcos_dicc = [] # lista de diccionarios
    lista_rects = [] # lista de rectangulos
    rectangulos = []
    barcos_averiados = {} # {'1':0, '2':0}

    id_barco = 1
    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            x_rect = posicion_x + columna * ancho_casillero
            y_rect = posicion_y + fila * ancho_casillero
            rect_tablero = pygame.Rect(x_rect, y_rect, ancho_casillero, ancho_casillero)
            
            rectangulo_tablero = pygame.draw.rect(ventana, fondo_color_tablero, rect_tablero, 1)  # Dibuja las líneas del tablero
            rectangulos.append(rectangulo_tablero)
            lista_rects.append(rect_tablero) # lista de rectangulos

            # Crea un diccionario de cada barco con sus datos y asigna su valor de la matriz creada
            barco_valor = matriz_barcos[fila][columna]
            #if barco_valor != 0: # si hay un barco
            barco_rect = {'x':rect_tablero.x, 'y':rect_tablero.y, 'valor':barco_valor, 'id':id_barco, 'fila':fila, 'columna':columna}
            lista_barcos_dicc.append(barco_rect) # lista de diccionarios
            id_barco += 1
                
            """ if id_barco not in barcos_averiados:
                    barcos_averiados[id_barco] = 0 # Inicializa partes averiadas del barco
                 """
            
            
    retorno = [lista_rects, lista_barcos_dicc, barcos_averiados] 

    return retorno

def dibuja_rects(tamaño_tablero, ancho_casillero, ventana, posicion_x, posicion_y): # Dibujo el tablero con sus rectangulos sin valores, para poder machear el click del usuario en estos

    rectangulos = []
    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            
            x_rect = posicion_x + columna * ancho_casillero
            y_rect = posicion_y + fila * ancho_casillero
            rect_tablero = pygame.Rect(x_rect, y_rect, ancho_casillero, ancho_casillero)
            rectangulo_tablero = pygame.draw.rect(ventana, fondo_color_tablero, rect_tablero, 1)  # Dibuja las líneas del tablero
            rectangulos.append(rectangulo_tablero)
    return rectangulos

        
# PUNTAJES
def puntaje(usuario)-> list[dict]:
    puntajes = []
    puntaje_usuario = {'usuario': usuario, 'ultimo_puntaje': int, 'mejor_puntaje_historico': int, 'puntaje_actual': 0}
    puntajes.append(puntaje_usuario)
    
    return puntajes


def actualizar_puntaje(usuario, puntajes, nuevo_puntaje) -> list[dict]:
    # Buscamos al usuario en la lista de puntajes
    for puntaje in puntajes:
        if puntaje['usuario'] == usuario:
            # Actualizamos el puntaje actual
            puntaje['puntaje_actual'] += nuevo_puntaje
    nuevo_marcador = puntaje['puntaje_actual']
    return nuevo_marcador

def actualiza_marcador(puntajes, ventana, puntaje_actual, x_puntajes, y_puntajes):
    actualizado = puntajes[0]['puntaje_actual']
    actualizado_str = str(puntajes[0]['puntaje_actual']) 
    
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    txt_puntaje_actualizado = fuente_puntaje_actual.render(actualizado_str, False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actualizado, (x_puntajes + 50, y_puntajes + 10))
    return actualizado

# MODIFICA LA MATRIZ AL TOCAR UN BARCO
def modifica_matriz_disparos(matriz, barco)-> list:
    fila = barco['fila']
    columna = barco['columna']
    matriz[fila][columna] = 9 # valor para barco averiado
    return matriz


# Interaccion con el tablero
def click_tablero(coordenadas_click, tamaño_tablero, ancho_casillero, ANCHO_PANTALLA, ALTO_PANTALLA, barcos_casilleros, matriz, puntajes, usuario, barcos_averiados, ventana, puntaje_actual,  x_puntajes, y_puntajes, color_barco_tocado, color_agua):
    lista_rects_valores = dibuja_rects(tamaño_tablero, ancho_casillero, ventana, posicion_x=ANCHO_PANTALLA/5, posicion_y=ALTO_PANTALLA/7)
    
    for i in range(len(lista_rects_valores)): # cambiar al for
        rect_seleccionado = lista_rects_valores[i]
        if rect_seleccionado.collidepoint(coordenadas_click):
        # veo si hay un barco en ese casillero y su valor
            un_barco_tocado = barcos_casilleros[i] # Una parte del barco (un casillero)
            barco_valor = barcos_casilleros[i]['valor']
            #barco_id = barcos_casilleros[i]['id']
            
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
                    print(f' El barco es: {un_barco_tocado} ')
                    barcos_casilleros[i]['valor'] = 9 # uso 9 para barcos tocados/heridos
                    # Modifica la matriz de barcos
                    matriz_modificada = modifica_matriz_disparos(matriz, un_barco_tocado)
                    
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
            break  # Salir si ya toco un casillero 

    return puntajes


# VERIFICAR SI EL BARCO ESTA HUNDIDO PARA EL PUNTAJE
def obtener_partes_barco(id_barco, barcos_averiados, barcos_casilleros):

    partes_averiadas = [] # [{}, {}, {}] va a tener partes(barco{}-casilleros) averiadas
    for barco in barcos_casilleros:
        if barco['id'] == id_barco:
            partes_averiadas.append(barco)  # Añadimos la parte del barco a la lista

    # Cuantas partes del barco han sido tocadas
    partes_tocadas = 0 
    if id_barco in barcos_averiados:
        if barcos_averiados[id_barco] != 0:
            partes_tocadas = barcos_averiados[id_barco]
        else:
            partes_tocadas = 0

    # Si el numero de partes tocadas es igual al numero total de partes del barco
    hundido = False
    if partes_tocadas == len(partes_averiadas):
        hundido = True  # hundido
    else:
        hundido = False  # no está hundido    
    retorno = [hundido, partes_tocadas]
    return retorno


########################################################
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
    matriz_comienzo = comienza_juego(flota, inicializar_matriz, 'Facil') # Inicializa segun el nivel
    matriz_barcos = ubicar_barcos_aleatoriamente(flota, matriz_comienzo, 10, 10) # Barcos ubicados
    #mostrar_tablero(matriz_barcos) # Matriz cargada
    return matriz_barcos



def saliendo(nick:str)-> str:
    mensaje = f'\n**********\nSaliendo del juego! hasta la proxima {nick}...\n**********\n'
    print(mensaje)
    return mensaje


