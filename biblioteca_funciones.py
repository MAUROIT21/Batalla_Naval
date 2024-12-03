import random
import json
import pygame.mixer as mixer
import pygame
from colores_naval import *

#pygame.init()

#Musica del juego
def sonido_juego ():
    """
    Configura y reproduce la musica del juego. La reproduce infinitamente con el parametro loops=-1
    """
    mixer.init()
    ruta_musica = 'teoria_juegos/Batalla_Naval/archivos_naval/naval_music.mp3'
    mixer.music.load(ruta_musica)
    mixer.music.set_volume(0.2)
    mixer.music.play(loops=-1)

# Inicializa matriz
def inicializar_matriz (filas: int, columnas:int, valor_inicial: any):
    """
    Crea una matriz (lista de listas) de dimensiones especificadas, 
    inicializada con un valor determinado.

    Parámetros:
    filas: El número de filas de la matriz.
    columnas: El número de columnas de la matriz.
    valor_inicial: El valor con el que se inicializan todos los elementos de la matriz.

    Retorna: Lista con los valores inicializados"""
    
    matriz = []
    for _ in range (filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    
    return matriz

def mostrar_tablero (matriz:list)-> list:    
    """
    Muestra por pantalla la matriz con sus elementos fila por fila.

    Parámetros:
    matriz (list): Una lista de sublistas

    Retorna:
    list: Retorna la matriz recibida como parámetro sin modificaciones. 
    """
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print (matriz[i][j], end=' ')
        print('')


def saliendo()-> str:
    """
    Muestra un mensaje en la consola saliendo del juego
    """
    mensaje = f'\n**********\nSaliendo del juego! hasta la proxima...\n**********\n'
    print(mensaje)
    return mensaje


def menu_juego(ventana, imagen_barcos, nivel, jugar, puntajes_historicos, salir, color_boton_nivel, color_boton_jugar, color_boton_puntaje, color_boton_salir, y_boton, x_boton, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, txt_usuario_boton, guardar_puntaje, volver_atras):
    """
    Dibuja en la pantalla todos los elementos del Menu, imagenes, botones y ademas desabilita los elementos de otras pantallas y estados del juego
    Parametros: elementos(rectangulos, imagenes, ventana) creados en naval.py y colores, fuentes de colores_naval.py para visualizar los comandos del menu 
    """
    ventana.blit(imagen_barcos, (0,0)) # Imagen de Fondo
    imagen_barcos.set_alpha(255)
    botones_jugando_inactivos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, guardar_puntaje, volver_atras)
    botones_menu_activos(nivel, jugar, puntajes_historicos, salir, x_boton)
    limpia_usuario_texto(ventana, usuario_caja_texto, txt_usuario_boton)
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


def dibujar_botones_juego(ventana, color_boton_salir, color_boton_guardar, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha, usuario_caja_texto, color_usuario_boton, guardar_puntaje, x_guardar, y_guardar):
    """
    Dibuja los Botones a la derecha del tablero de juego 
    Parametros: recibe elementos creados en naval.py y en colores_naval.py para configurar los elementos que dibujara en la pantalla
    """
    pygame.draw.rect(ventana, color_boton_salir, salir_jugando)
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    pygame.draw.rect(ventana, color_boton_salir, reiniciar_jugando)
    pygame.draw.rect(ventana, color_boton_salir, volver_menu)
    pygame.draw.rect(ventana, color_boton_guardar, guardar_puntaje)
    
    txt_puntaje_actual = fuente_puntaje_actual.render('0000', False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actual, (x_puntajes + 35, y_puntajes + 15))
    txt_salir_jugando = fuente_botones.render('Salir', False, color_letra_botones)
    ventana.blit(txt_salir_jugando, (x_boton_derecha + 35, y_boton_derecha+10))
    txt_reiniciar_jugando = fuente_botones.render('Reiniciar', False, color_letra_botones)
    ventana.blit(txt_reiniciar_jugando, (x_boton_derecha + 22, y_boton_derecha + 110))
    txt_volver_menu = fuente_botones.render('Volver', False, color_letra_botones)
    ventana.blit(txt_volver_menu, (x_boton_derecha + 30, y_boton_derecha + 210))
    txt_guardar = fuente_botones.render('Guardar Puntaje', False, color_letra_botones)
    ventana.blit(txt_guardar, (x_guardar + 4, y_guardar + 5))
    

def ingresar_usuario_texto (ventana, usuario_caja_texto, ingreso_texto):
    """
    Dibuja en el cuadro de texto durante el juego el nombre del usuario que se va ingresando
    Parametros: ventana del juego, usuario_caja_texto: rectangulo, ingreso_texto: ingreso por teclado
    """
    pygame.draw.rect(ventana, color_usuario_boton, usuario_caja_texto)
    
    txt_usuario_boton = fuente_botones.render(ingreso_texto, False, color_letra_botones)
    margen_x = 5
    margen_y = (usuario_caja_texto.height - txt_usuario_boton.get_height()) // 2  # Centrado vertical
    texto_x = usuario_caja_texto.x + margen_x
    texto_y = usuario_caja_texto.y + margen_y
    ventana.blit(txt_usuario_boton, (texto_x, texto_y))
    pygame.display.update(usuario_caja_texto)
    return txt_usuario_boton

def limpia_usuario_texto(ventana, usuario_caja_texto, txt_usuario_boton):
    """
    Limpia el texto de la caja de ingreso del usuario
    Parametros: ventana del juego, usuario_caja_texto: rectangulo, txt_usuario_boton: el cuadro de texto
    """
    pygame.draw.rect(ventana, color_casillero_texto, usuario_caja_texto)
    margen_x = 5
    margen_y = (usuario_caja_texto.height - txt_usuario_boton.get_height()) // 2  # Centrado vertical
    texto_x = usuario_caja_texto.x + margen_x
    texto_y = usuario_caja_texto.y + margen_y
    ventana.blit(txt_usuario_boton, (texto_x, texto_y))
    pygame.display.update(usuario_caja_texto)
    return txt_usuario_boton

# Botones del menu inactivos
def botones_menu_inactivos(nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, volver_atras):
    """
    Toma como parametro los elementos de la pantalla que se van a mover para que no esten activos
    """
    nivel.x = ANCHO_PANTALLA-1000
    jugar.x = ANCHO_PANTALLA-1000
    puntajes_historicos.x = ANCHO_PANTALLA-1000
    salir.x = ANCHO_PANTALLA-1000
    volver_atras.x = ANCHO_PANTALLA-1000

def botones_menu_activos (nivel, jugar, puntajes_historicos, salir, x_boton):
    """
    Vuelve a colocar los elementos del menu en su posicion original
    """
    # vuelven a su posicion original activos.
    nivel.x = x_boton
    jugar.x = x_boton + 150
    puntajes_historicos.x = x_boton + 300
    salir.x = x_boton + 450

def botones_jugando_inactivos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, guardar_puntaje, volver_atras):
    """
    Toma como parametro los elementos de la pantalla que se van a mover para que no esten activos
    """    
    salir_jugando.x = ANCHO_PANTALLA+1000
    puntaje_actual.x = ANCHO_PANTALLA+1000
    reiniciar_jugando.x = ANCHO_PANTALLA+1000
    volver_menu.x = ANCHO_PANTALLA+1000
    usuario_caja_texto.x = ANCHO_PANTALLA+1000
    guardar_puntaje.x = ANCHO_PANTALLA+1000
    volver_atras.x = ANCHO_PANTALLA+1000

def botones_jugando_activos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, x_puntajes, x_boton_derecha, guardar_puntaje, x_guardar, y_guardar):
    """
    Vuelve a colocar los elementos del menu en su posicion original
    """    
    salir_jugando.x = x_boton_derecha
    puntaje_actual.x = x_puntajes
    reiniciar_jugando.x = x_boton_derecha
    volver_menu.x = x_boton_derecha
    usuario_caja_texto.x = x_puntajes + 250
    guardar_puntaje.x = x_guardar

def jugando (tamaño_tablero, ancho_casillero, ventana, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, ALTO_PANTALLA, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha, usuario_caja_texto, color_usuario_boton, txt_usuario_boton, color_boton_guardar, guardar_puntaje, x_guardar, y_guardar, volver_atras):
    """
    Cuando inicia el juego, se crea la pantalla, sus elementos y botones, el tablero y se genera lo logica de los barcos posicionandolos en sus respectivos casilleros de manera aleatoria
    """
    
    ventana.fill(fondo_ventana) # detras de la imagen fondo negro
    ventana.blit(imagen_fondo_oceano, (0,0)) # imagen fondo del tablero 
    botones_menu_inactivos(nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, volver_atras) # Desactiva los botones del menu al comenzar el juego
    botones_jugando_activos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, x_puntajes, x_boton_derecha, guardar_puntaje, x_guardar, y_guardar)
    dibujar_botones_juego(ventana, color_boton_salir, color_boton_guardar, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha, usuario_caja_texto, color_usuario_boton, guardar_puntaje, x_guardar, y_guardar)
    limpia_usuario_texto(ventana, usuario_caja_texto, txt_usuario_boton)

    matriz_barcos_posiciones_ubicados = a_jugar() # Se genera la logica del juego.
    matriz_barcos_ubicados = matriz_barcos_posiciones_ubicados[0]
    partes_barco_coordenadas = matriz_barcos_posiciones_ubicados[1]  
    retorno_lista_rects = dibuja_tablero(tamaño_tablero, ancho_casillero, ventana, posicion_x=ANCHO_PANTALLA/5, posicion_y=ALTO_PANTALLA/7, matriz_barcos= matriz_barcos_ubicados, partes_barcos_coordenadas= partes_barco_coordenadas) # Se prepara el tablero
    casilleros_xy_valor = retorno_lista_rects[0]
    barcos_averiados = retorno_lista_rects[1]
    rectangulos = retorno_lista_rects[2]
    
    datos_retorno = [matriz_barcos_ubicados, casilleros_xy_valor, barcos_averiados, partes_barco_coordenadas, rectangulos]
    return datos_retorno

def generar_pos_aleatoria (filas:int, columnas:int)-> tuple:
    """
    Genera la posicion aleatoriamente para filas y columnas para luego posicionar los barcos
    Parametros: toma filas y columnas  como rango para generar
    Devuelve la tupla con las coordenadas
    """
    pos_fila = random.randint(0,filas-1)
    pos_columna = random.randint(0,columnas-1)
    
    posicion = (pos_fila, pos_columna)
    return posicion


def ubicar_barcos_aleatoriamente(flota: list, matriz: list, filas: int, columnas: int):
    """
    Toma la flota de barcos creada, la matriz de datos, y la cantidad de filas y columnas, para ubicar los valores de cada barco en los casilleros del tablero y de la matriz de datos evaluando si es posible por cada posicion generada aleatoriamente
    """
    lista_posiciones_barcos = []  # Lista para almacenar los datos de los barcos
    id_barco = 1
    retorno = []

    for i in range(len(flota)):  # tipos de barcos
        for j in range(len(flota[i])): # barcos por tipo
            largo_barco = flota[i][j]['tamaño']

            # Ubico el barco en la matriz
            casillero_libre = False
            while casillero_libre == False:
                posicion = generar_pos_aleatoria(filas, columnas)
                pos_fila, pos_columna = posicion

                match largo_barco:
                    case 1:
                        if matriz[pos_fila][pos_columna] == 0: # Sino hay barcos
                            casillero_libre = True
                            matriz[pos_fila][pos_columna] = largo_barco
                            #Genera un dict con los datos del barco
                            lista_posiciones_barcos.append({
                                'id_barco': id_barco,
                                'coordenadas': (pos_fila, pos_columna),
                                'partes_del_barco': (1, 1), # que parte es del total de partes
                                'parte_averiada': False
                            })
                    case 2:
                        # Verifica si en la pos_columna generada se puede colocar el barco(por su tamaño) y si los casilleros de la matriz estan vacios
                        if pos_columna < columnas - 1 and matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0:
                            casillero_libre = True
                            for parte in range(largo_barco): # genera un numero para cada parte del barco para la posicion de la columna
                                matriz[pos_fila][pos_columna + parte] = largo_barco
                                lista_posiciones_barcos.append({
                                    'id_barco': id_barco,
                                    'coordenadas': (pos_fila, pos_columna + parte),
                                    'partes_del_barco': (parte + 1, largo_barco), # que parte es del total de partes
                                    'parte_averiada': False
                                })
                    case 3:
                        if pos_columna < columnas - 2 and matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0 and matriz[pos_fila][pos_columna+2] == 0:
                            casillero_libre = True
                            for parte in range(largo_barco):
                                matriz[pos_fila][pos_columna + parte] = largo_barco
                                lista_posiciones_barcos.append({
                                    'id_barco': id_barco,
                                    'coordenadas': (pos_fila, pos_columna + parte),
                                    'partes_del_barco': (parte + 1, largo_barco),
                                    'parte_averiada': False
                                })
                    case 4:
                        if pos_columna < columnas - 3 and matriz[pos_fila][pos_columna] == 0 and matriz[pos_fila][pos_columna+1] == 0 and matriz[pos_fila][pos_columna+2] == 0 and matriz[pos_fila][pos_columna+3] == 0:
                            casillero_libre = True
                            for parte in range(largo_barco):
                                matriz[pos_fila][pos_columna + parte] = largo_barco
                                lista_posiciones_barcos.append({
                                    'id_barco': id_barco,
                                    'coordenadas': (pos_fila, pos_columna + parte),
                                    'partes_del_barco': (parte + 1, largo_barco),
                                    'parte_averiada': False
                                })
            id_barco += 1  # Incremento el ID para el siguiente barco
    retorno.append(matriz)
    retorno.append(lista_posiciones_barcos)

    return retorno


def a_jugar ():
    """    
    Cuando comienza el juego: crea la flota, la matriz vacia, y finalmente ubica los barcos aleatoriamente
    Devuelve la matriz de barcos de datos ubicados
    """
    print('\n Comienza el juego!  \n')
    flota = crea_navios_automaticamente()
    matriz_comienzo = comienza_juego(inicializar_matriz, 'Facil') # Inicializa segun el nivel
    cant_filas = len(matriz_comienzo)
    cant_columnas = len(matriz_comienzo[0])
    matriz_barcos_posiciones = ubicar_barcos_aleatoriamente(flota, matriz_comienzo, cant_filas, cant_columnas) # Barcos ubicados
    
    return matriz_barcos_posiciones


def dibuja_tablero(tamaño_tablero, ancho_casillero, ventana, posicion_x, posicion_y, matriz_barcos, partes_barcos_coordenadas): # dibuja el tablero completo con valores
    """
    Dibuja el tablero con sus rectangulos y casilleros: que tendran los datos del barco y coordenadas
    """
    
    lista_casilleros_rect = [] # lista de diccionarios
    #rectangulos_dibujados = []
    barcos_averiados = {}
    rectangulos = []
    id_casillero = 1

    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            
            x_rect = posicion_x + columna * ancho_casillero
            y_rect = posicion_y + fila * ancho_casillero
            rect_tablero = pygame.Rect(x_rect, y_rect, ancho_casillero, ancho_casillero)
            rectangulo_tablero = pygame.draw.rect(ventana, fondo_color_tablero, rect_tablero, 1)  # Dibuja las líneas del tablero
            rectangulos.append(rectangulo_tablero)
            
            # Crea un diccionario para cada casillero con sus datos y asigna su valor de la matriz creada
            barco_valor = matriz_barcos[fila][columna]
            # Con los rects del tablero construyo un dict de cada casillero con sus datos en el tablero (puede tener o no parte de un barco)   
            casillero_rect = {'x':rect_tablero.x, 'y':rect_tablero.y, 'valor':barco_valor, 'id':id_casillero, 'fila':fila, 'columna':columna}
            lista_casilleros_rect.append(casillero_rect)
        
            if id_casillero not in barcos_averiados:
                barcos_averiados[id_casillero] = 0 # Inicializa partes averiadas del barco
    
            id_casillero += 1

    retorno = [lista_casilleros_rect, barcos_averiados, rectangulos] 
    return retorno

def dibuja_rects(tamaño_tablero, ancho_casillero, ventana, posicion_x, posicion_y): # Dibujo el tablero con sus rectangulos sin valores, para poder machear el click del usuario en estos
    """
    Dibuja los rectangulos y lineas del tablero de juego
    """
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

def actualizar_puntaje(usuario, puntajes, nuevo_puntaje):
    """
    Cuando acierta o no un casillero al interactuar con el tablero, se modifica el puntaje del usuario. Sino esta el usuario inicializa sus datos y valores
    """
    # Buscamos al usuario en la lista de puntajes
    if usuario in puntajes:
        puntajes[usuario]['puntaje_actual'] += nuevo_puntaje  # Actualiza el puntaje sumando el nuevo
    else: # crea un usuario nuevo con sus claves correspondientes
        puntajes[usuario] = {
        "ultimo_puntaje": 0,
        "mejor_puntaje_historico": 0,
        "puntaje_actual": 0
    }
    return puntajes

def actualiza_marcador(puntajes, ventana, puntaje_actual, x_puntajes, y_puntajes, usuario):
    """
    Renderiza el marcador sobre el tablero con los puntajes que van cambiando
    """
    actualizado = puntajes[usuario]['puntaje_actual']
    actualizado_str = str(actualizado) 
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    txt_puntaje_actualizado = fuente_puntaje_actual.render(actualizado_str, False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actualizado, (x_puntajes + 50, y_puntajes + 10))
    return actualizado

def inicializa_marcador(usuario, puntajes, x_puntajes, y_puntajes, ventana, puntaje_actual):
    """
    Renderiza en cero el marcador
    """
    marcador_inicializado = '000'
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    txt_puntaje_actualizado = fuente_puntaje_actual.render(marcador_inicializado, False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actualizado, (x_puntajes + 35, y_puntajes + 10))
    return marcador_inicializado

def actualizar_puntaje_cierre(usuario, puntajes_juego_partida):
    """
    Al guardar la partida si el usuario no esta en la lista lo crea. Si esta, actualiza todos sus puntajes 
    """
    if usuario not in puntajes_juego_partida:
        puntajes_juego_partida[usuario] = {
        "ultimo_puntaje": 0,
        "mejor_puntaje_historico": 0,
        "puntaje_actual": 0
            }

    else:
        puntajes_juego_partida[usuario]['ultimo_puntaje'] = puntajes_juego_partida[usuario]['puntaje_actual']
        # poner puntaje actual en cero
        puntajes_juego_partida[usuario]['puntaje_actual'] = 0
        # y si el ultimo es mayor que el historico reemplazarlo
        if puntajes_juego_partida[usuario]['ultimo_puntaje'] > puntajes_juego_partida[usuario]['mejor_puntaje_historico']:
            puntajes_juego_partida[usuario]['mejor_puntaje_historico'] = puntajes_juego_partida[usuario]['ultimo_puntaje']


def inicializa_usuario_nuevo(usuario, puntajes_juego_dict):
    """
    Inicializa un nuevo usuario con puntajes sino esta en la lista
    """
    if usuario not in puntajes_juego_dict:
        puntajes_juego_dict[usuario] = {
        "ultimo_puntaje": 0,
        "mejor_puntaje_historico": 0,
        "puntaje_actual": 0
    }
    return puntajes_juego_dict

# GUARDAR EN JSON
def guardar_puntaje_json (puntajes_juego, ruta= 'teoria_juegos/Batalla_Naval/puntajes.json'):
    """
    Abre el archivo JSON para guardar datos actualizados al guardar la partida
    """
    with open(ruta, 'w') as archivo:
        json.dump(puntajes_juego, archivo, indent=4)
    

# MODIFICA LA MATRIZ AL TOCAR UN BARCO
def modifica_matriz_disparos(matriz, barco)-> list:
    """
    Cambia el valor de la matriz de datos segun sea acierto, agua, barco averiado, y el valor de cada parte de barco. Ademas verifica si el barco fue hundido para actualizar los puntajes
    """
    fila = barco['fila']
    columna = barco['columna']
    matriz[fila][columna] = 9 # valor para barco averiado
    return matriz

# Interaccion con el tablero
def click_tablero(coordenadas_click, tamaño_tablero, ancho_casillero, ANCHO_PANTALLA, ALTO_PANTALLA, barcos_casilleros, matriz, puntajes_juego_dict, usuario, barcos_averiados, ventana, puntaje_actual,  x_puntajes, y_puntajes, color_barco_tocado, color_agua, partes_barco_coordenadas, rectangulos):
    """
    Cuando el usuario interactua con el tablero haciendo clicks, se modifica la matriz de valores, los casilleros, se actualizan los puntajes segun corresponda para ese usuario, 
    """
    for i in range(len(rectangulos)): # cambiar al for
        rect_seleccionado = rectangulos[i]
        if rect_seleccionado.collidepoint(coordenadas_click):
        # veo si hay un barco en ese casillero y su valor
            casillero_tocado = barcos_casilleros[i]
            barco_valor = barcos_casilleros[i]['valor']
            posicion_fila_columna = ()
            posicion_fila_columna = casillero_tocado['fila'], casillero_tocado['columna']
            #print(f'casillero_tocado >> {casillero_tocado}')
            
            if barco_valor != 0:  # Si hay un barco
                if barco_valor == 9: # Si ya estaba tocado/averiado
                    #print(f' Barco averiado! en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y}')
                    pass
                else: # Barco tocado
                    barcos_casilleros[i]['valor'] = 9 # uso 9 para barcos tocados/heridos
                    # Modifica la matriz de barcos
                    matriz_modificada = modifica_matriz_disparos(matriz, casillero_tocado)
                    # MODIFICAR EL COLOR al barco tocado
                    pygame.draw.rect(ventana, color_barco_tocado, rect_seleccionado)  
                    # MODIFICA EL PUNTAJE DEL USUARIO
                    nuevo_puntaje = 5
                    actualizar_puntaje(usuario, puntajes_juego_dict, nuevo_puntaje)

                    # Busca el id_barco tocado para validar si esta hundido o no
                    for j in range (len(partes_barco_coordenadas)):
                        if posicion_fila_columna == partes_barco_coordenadas[j]['coordenadas']:
                            partes_barco_coordenadas[j]['parte_averiada'] = True # Marco la parte averiada
                            id_barco_tocado = partes_barco_coordenadas[j]['id_barco']
                            hundido = validar_barco_hundido(id_barco_tocado, partes_barco_coordenadas)
                            if hundido:
                                puntaje_hundido = 10 * partes_barco_coordenadas[j]['partes_del_barco'][1]
                                actualizar_puntaje(usuario, puntajes_juego_dict, puntaje_hundido)
            else:
                pygame.draw.rect(ventana, color_agua, rect_seleccionado)  # Redibujar el rectángulo con el nuevo color
                nuevo_puntaje = -1
                actualizar_puntaje(usuario, puntajes_juego_dict, nuevo_puntaje)

            # Actualiza el marcador de los puntajes
            actualiza_marcador(puntajes_juego_dict, ventana, puntaje_actual, x_puntajes, y_puntajes, usuario)
            pygame.display.update(rect_seleccionado)  # Solo actualiza el área del clic

            break  # Salir si ya toco un casillero 

    return puntajes_juego_dict

# Ordenamiento de puntajes para mostrar por pantalla

def ordena_puntajes_historicos(puntajes_juego_dict):
    """
    Toma el dict de todos los usuarios con sus puntajes y los ordena. Ademas devuelve una lista con los 3 mejores puntajes
    """
    lista_usuarios_ordenada = list(puntajes_juego_dict.items())
    
    for i in range(len(lista_usuarios_ordenada) - 1):
        for j in range(i + 1, len(lista_usuarios_ordenada)):
            if lista_usuarios_ordenada[i][1]["mejor_puntaje_historico"] < lista_usuarios_ordenada[j][1]["mejor_puntaje_historico"]:
                # Intercambiamos las posiciones si es necesario
                lista_usuarios_ordenada[i], lista_usuarios_ordenada[j] = lista_usuarios_ordenada[j], lista_usuarios_ordenada[i]
    
    # Seleccionamos los 3 primeros elementos de la lista ordenada
    mejores_3 = []
    for i in range(len(lista_usuarios_ordenada)):
        if i < 3:
            mejores_3.append(lista_usuarios_ordenada[i])
    
    retorno = [mejores_3, lista_usuarios_ordenada]
    return retorno

def crear_pantalla_historicos (ventana, los_mejores_3, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, volver_atras):
    """
    Dibujamos una pantalla nueva para mostrar el historico de los puntajes
    """
    ventana.fill(fondo_ventana) # detras de la imagen fondo negro
    ventana.blit(imagen_fondo_oceano, (0,0)) # imagen fondo del tablero 
    botones_menu_inactivos(nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, volver_atras)
    volver_atras = pygame.Rect(350, 500, 70, 50)
    pygame.draw.rect(ventana, color_boton_volver_atras, volver_atras)  
    volver_atras_txt = fuente_botones.render('MENU', True, color_letra_botones)
    ventana.blit(volver_atras_txt, (volver_atras.x + 9, volver_atras.y + 12))
    titulo = fuente_titulo.render("Top 3 Históricos", True, color_letra_titulo)
    ventana.blit(titulo, (200, 50))
    
    posicion_y = 150
    for i in range (len(los_mejores_3)):
        usuario_puntajes = los_mejores_3[i]
        usuario = usuario_puntajes[0]
        mejor_historico = usuario_puntajes[1]['mejor_puntaje_historico']
        texto = f"{i+1} >>>  {usuario}: {mejor_historico} puntos"
        texto_renderizado = fuente_puntaje_actual.render(texto, True, color_letra_botones)
        ventana.blit(texto_renderizado, (150, posicion_y))
        posicion_y += 50
        pygame.display.flip()
     

def validar_barco_hundido(id_barco, partes_barco_coordenadas) -> bool:
    """
    Evaluar si todas las partes del barco con el id proporcionado están averiadas
    """    
    for parte in partes_barco_coordenadas:
        if parte['id_barco'] == id_barco and parte['parte_averiada'] == False: # not (False) = True
            return False  # Si alguna parte no está averiada, no está hundido
    return True  # Todas las partes están averiadas


def crea_navios_automaticamente():
    """
    Crea la flota de barcos y sus componentes. Por setea manualmente la cantidad de barcos por tipo
    """

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

def comienza_juego(inicializar_matriz:callable, nivel:str):
    """
    Segun el parametro Nivel se crea una matriz con el tamaño especifico
    """
    match nivel:
        case 'Facil':
            matriz = inicializar_matriz(10,10,0)
        case 'Medio':
            matriz =  inicializar_matriz(20,20,0) 
        case 'Dificil':
            matriz =  inicializar_matriz(40,40,0) 
    return matriz