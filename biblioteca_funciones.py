import random
import json
import pygame.mixer as mixer
import pygame
from colores_naval import *

#pygame.init()


#Musica del juego
def sonido_juego ():
    mixer.init()
    ruta_musica = 'teoria_juegos/Batalla_Naval/archivos_naval/naval_music.mp3'
    #sonido = mixer.Sound(ruta_musica)
    #sonido.set_volume(0.4)
    #sonido.play()
    
     # Cargar y reproducir música en bucle
    mixer.music.load(ruta_musica)
    mixer.music.set_volume(0.5)
    #mixer.music.play(loops=-1)  # -1 indica reproducción infinita

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


def saliendo(usuario:str)-> str:
    mensaje = f'\n**********\nSaliendo del juego! hasta la proxima {usuario}...\n**********\n'
    print(mensaje)
    return mensaje


def menu_juego(ventana, imagen_barcos, nivel, jugar, puntajes_historicos, salir, color_boton_nivel, color_boton_jugar, color_boton_puntaje, color_boton_salir, y_boton, x_boton, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, txt_usuario_boton, guardar_puntaje):
    ventana.blit(imagen_barcos, (0,0)) # Imagen de Fondo
    imagen_barcos.set_alpha(255)
    botones_jugando_inactivos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, guardar_puntaje)
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


def dibujar_botones_juego(ventana:pygame.Surface, color_boton_salir, color_boton_guardar, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha, usuario_caja_texto, color_usuario_boton, guardar_puntaje, x_guardar, y_guardar):
    # Botones a la derecha del tablero    
    pygame.draw.rect(ventana, color_boton_salir, salir_jugando)
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    pygame.draw.rect(ventana, color_boton_salir, reiniciar_jugando)
    pygame.draw.rect(ventana, color_boton_salir, volver_menu)
    pygame.draw.rect(ventana, color_boton_guardar, guardar_puntaje)
    
    # ACA IBA EL RECT DE usuario boton texto
    txt_puntaje_actual = fuente_puntaje_actual.render('0000', False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actual, (x_puntajes + 35, y_puntajes + 15))
    txt_salir_jugando = fuente_botones.render('Salir', False, color_letra_botones)
    ventana.blit(txt_salir_jugando, (x_boton_derecha + 35, y_boton_derecha+10))
    txt_reiniciar_jugando = fuente_botones.render('Reiniciar', False, color_letra_botones)
    ventana.blit(txt_reiniciar_jugando, (x_boton_derecha + 22, y_boton_derecha + 110))
    txt_volver_menu = fuente_botones.render('Volver', False, color_letra_botones)
    ventana.blit(txt_volver_menu, (x_boton_derecha + 30, y_boton_derecha + 210))
    #txt_usuario_boton = fuente_botones.render('Ingrese su usuario aqui: ', False, color_letra_botones)
    #ventana.blit(txt_usuario_boton, (x_puntajes + 253, y_puntajes + 15))
    txt_guardar = fuente_botones.render('Guardar Puntaje', False, color_letra_botones)
    ventana.blit(txt_guardar, (x_guardar + 4, y_guardar + 5))
    

def ingresar_usuario_texto (ventana, usuario_caja_texto, ingreso_texto):
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
    pygame.draw.rect(ventana, color_casillero_texto, usuario_caja_texto)
    margen_x = 5
    margen_y = (usuario_caja_texto.height - txt_usuario_boton.get_height()) // 2  # Centrado vertical
    texto_x = usuario_caja_texto.x + margen_x
    texto_y = usuario_caja_texto.y + margen_y
    #txt_usuario_boton = fuente_botones.render('Ingrese su usuario: ', False, color_letra_botones)
    ventana.blit(txt_usuario_boton, (texto_x, texto_y))
    pygame.display.update(usuario_caja_texto)
    return txt_usuario_boton

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

def botones_jugando_inactivos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, guardar_puntaje):
    # LOS SACO DE LA PANTALLA
    salir_jugando.x = ANCHO_PANTALLA+1000
    puntaje_actual.x = ANCHO_PANTALLA+1000
    reiniciar_jugando.x = ANCHO_PANTALLA+1000
    volver_menu.x = ANCHO_PANTALLA+1000
    usuario_caja_texto.x = ANCHO_PANTALLA+1000
    guardar_puntaje.x = ANCHO_PANTALLA+1000

def botones_jugando_activos(salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, x_puntajes, x_boton_derecha, guardar_puntaje, x_guardar, y_guardar):
    # LOS SACO DE LA PANTALLA
    salir_jugando.x = x_boton_derecha
    puntaje_actual.x = x_puntajes
    reiniciar_jugando.x = x_boton_derecha
    volver_menu.x = x_boton_derecha
    usuario_caja_texto.x = x_puntajes + 250
    guardar_puntaje.x = x_guardar


def jugando (tamaño_tablero, ancho_casillero, ventana, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, ALTO_PANTALLA, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha, usuario_caja_texto, color_usuario_boton, txt_usuario_boton, color_boton_guardar, guardar_puntaje, x_guardar, y_guardar):
    ventana.fill(fondo_ventana) # detras de la imagen fondo negro
    ventana.blit(imagen_fondo_oceano, (0,0)) # imagen fondo del tablero 
    botones_menu_inactivos(nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA) # Desactiva los botones del menu al comenzar el juego
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
# datos_retorno[0] >> una lista de 2 listas

def generar_pos_aleatoria (filas:int, columnas:int)-> tuple:
    pos_fila = random.randint(0,filas-1)
    pos_columna = random.randint(0,columnas-1)
    
    posicion = (pos_fila, pos_columna)
    return posicion


def ubicar_barcos_aleatoriamente(flota: list, matriz: list, filas: int, columnas: int):
    cont_lleno = 0
    cont_libre = 0
    lista_posiciones_barcos = []  # Lista para almacenar los datos de los barcos
    id_barco = 1  # ID inicial para los barcos / VER DE CREAR LOS ID EN LA FUNCION QUE CREA LOS NAVIOS(FLOTA)
    retorno = []
    for i in range(len(flota)):  # tipos de barcos
        for j in range(len(flota[i])):  # barcos por tipo
            # Tomo un barco y su tamaño
            barco = flota[i][j]
            largo_barco = flota[i][j]['tamaño']

            # Ubico el barco en la matriz
            casillero_libre = False
            while casillero_libre == False:
                posicion = generar_pos_aleatoria(filas, columnas)
                pos_fila, pos_columna = posicion

                # Validar espacios según el tamaño del barco
                match largo_barco:
                    case 1:
                        if matriz[pos_fila][pos_columna] == 0:
                            casillero_libre = True
                            matriz[pos_fila][pos_columna] = largo_barco
                            lista_posiciones_barcos.append({
                                'id_barco': id_barco,
                                'coordenadas': (pos_fila, pos_columna),
                                'partes_del_barco': (1, 1), # que parte es del total de partes
                                'parte_averiada': False
                            })
                    case 2:
                        # Verifica si en la pos_columna generada se puede colocar el barco, evaluando si los casilleros de la matriz estan vacios
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
        
    # Cuando comienza el juego: crea la flota, la matriz vacia, y finalmente ubica los barcos aleatoriamente
    print('\n Comienza el juego!  \n')
    flota = crea_navios_automaticamente()
    matriz_comienzo = comienza_juego(inicializar_matriz, 'Facil') # Inicializa segun el nivel
    cant_filas = len(matriz_comienzo)
    cant_columnas = len(matriz_comienzo[0])
    matriz_barcos_posiciones = ubicar_barcos_aleatoriamente(flota, matriz_comienzo, cant_filas, cant_columnas) # Barcos ubicados
    
    return matriz_barcos_posiciones


def dibuja_tablero(tamaño_tablero, ancho_casillero, ventana, posicion_x, posicion_y, matriz_barcos, partes_barcos_coordenadas): # dibuja el tablero completo con valores
    lista_casilleros_rect = [] # lista de diccionarios
    rectangulos_dibujados = []
    barcos_averiados = {} # {'1':0, '2':0}
    rectangulos = []
    #lista_rects = [] # lista de rectangulos
    id_casillero = 1

    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            
            x_rect = posicion_x + columna * ancho_casillero
            y_rect = posicion_y + fila * ancho_casillero
            rect_tablero = pygame.Rect(x_rect, y_rect, ancho_casillero, ancho_casillero)
            rectangulo_tablero = pygame.draw.rect(ventana, fondo_color_tablero, rect_tablero, 1)  # Dibuja las líneas del tablero
            rectangulos.append(rectangulo_tablero)
            
            #lista_rects.append(rect_tablero) # lista de rectangulos

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

        
# PUNTAJES
""" def puntaje(usuario)-> list[dict]:
    puntajes = []

    for puntaje_usuario in puntajes:
        if puntaje_usuario['usuario'] == usuario:
            return puntajes # si ya existe el usuario devuelve la lista entera
    # Sino estaba el usuario lo crea    
    puntaje_usuario = {'usuario': usuario, 'ultimo_puntaje': 0, 'mejor_puntaje_historico': 0, 'puntaje_actual': 0}
    puntajes.append(puntaje_usuario)
    return puntajes """

""" def puntaje(usuario)-> list[dict]:
    puntajes = []
    puntaje_usuario = {'usuario': usuario, 'ultimo_puntaje': int, 'mejor_puntaje_historico': int, 'puntaje_actual': 0}
    puntajes.append(puntaje_usuario)
    
    return puntajes """

def actualizar_puntaje(usuario, puntajes, nuevo_puntaje):
    # Buscamos al usuario en la lista de puntajes
    if usuario in puntajes:
        puntajes[usuario]['puntaje_actual'] += nuevo_puntaje  # Actualiza el puntaje sumando el nuevo
    else: # crea un usuario nuevo con sus claves correspondientes
        puntajes[usuario] = {
        "ultimo_puntaje": 0,
        "mejor_puntaje_historico": 0,
        "puntaje_actual": nuevo_puntaje
    }
    return puntajes

def actualiza_marcador(puntajes, ventana, puntaje_actual, x_puntajes, y_puntajes, usuario):
    actualizado = puntajes[usuario]['puntaje_actual']
    actualizado_str = str(actualizado) 
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    txt_puntaje_actualizado = fuente_puntaje_actual.render(actualizado_str, False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actualizado, (x_puntajes + 50, y_puntajes + 10))
    return actualizado

def inicializa_marcador(usuario, puntajes, x_puntajes, y_puntajes, ventana, puntaje_actual):
    #puntajes[usuario]['puntaje_actual'] = 0
    #marcador_inicializado = puntajes[usuario]['puntaje_actual']
    marcador_inicializado = '000'
    pygame.draw.rect(ventana, color_boton_puntaje, puntaje_actual)
    txt_puntaje_actualizado = fuente_puntaje_actual.render(marcador_inicializado, False, color_letra_puntaje)
    ventana.blit(txt_puntaje_actualizado, (x_puntajes + 50, y_puntajes + 10))
    return marcador_inicializado

def actualizar_puntaje_cierre(usuario, puntajes_juego_partida):
    # poner ultimo puntaje como el puntaje actual 
    puntajes_juego_partida[usuario]['ultimo_puntaje'] = puntajes_juego_partida[usuario]['puntaje_actual']
    # poner puntaje actual en cero
    puntajes_juego_partida[usuario]['puntaje_actual'] = 0
    # y si el ultimo es mayor que el historico reemplazarlo
    if puntajes_juego_partida[usuario]['ultimo_puntaje'] > puntajes_juego_partida[usuario]['mejor_puntaje_historico']:
        puntajes_juego_partida[usuario]['mejor_puntaje_historico'] = puntajes_juego_partida[usuario]['ultimo_puntaje']


def inicializa_usuario_nuevo(usuario, puntajes_juego_dict):
    if usuario not in puntajes_juego_dict:
        puntajes_juego_dict[usuario] = {
        "ultimo_puntaje": 0,
        "mejor_puntaje_historico": 0,
        "puntaje_actual": 0
    }
    return puntajes_juego_dict

# GUARDAR EN JSON
def guardar_puntaje_json (puntajes_juego, ruta= 'teoria_juegos/Batalla_Naval/puntajes.json'):
    with open(ruta, 'w') as archivo:
        #datos_puntajes = json.load(archivo)
        json.dump(puntajes_juego, archivo, indent=4)
    


# MODIFICA LA MATRIZ AL TOCAR UN BARCO
def modifica_matriz_disparos(matriz, barco)-> list:
    fila = barco['fila']
    columna = barco['columna']
    matriz[fila][columna] = 9 # valor para barco averiado
    return matriz

# Interaccion con el tablero
def click_tablero(coordenadas_click, tamaño_tablero, ancho_casillero, ANCHO_PANTALLA, ALTO_PANTALLA, barcos_casilleros, matriz, puntajes_juego_dict, usuario, barcos_averiados, ventana, puntaje_actual,  x_puntajes, y_puntajes, color_barco_tocado, color_agua, partes_barco_coordenadas, rectangulos):

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
                    print(f' Barco averiado! en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y}')
                else:
                    print(f' Tocaste un barco en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y} ')
                    #print(f' El barco es: {casillero_tocado} ')
                    barcos_casilleros[i]['valor'] = 9 # uso 9 para barcos tocados/heridos
                    # Modifica la matriz de barcos
                    matriz_modificada = modifica_matriz_disparos(matriz, casillero_tocado)
                    
                    # MODIFICAR EL COLOR AL RECT que contiene el texto
                    pygame.draw.rect(ventana, color_barco_tocado, rect_seleccionado)  

                    # MODIFICA EL PUNTAJE DEL USUARIO
                    nuevo_puntaje = 5
                    actualizar_puntaje(usuario, puntajes_juego_dict, nuevo_puntaje)
                    #print(f' \n--- Puntaje_actual > {puntajes_juego_dict[usuario]['puntaje_actual']}')

                    # Busca el id_barco tocado para validar si esta hundido o no
                    for j in range (len(partes_barco_coordenadas)):
                        #print(j)
                        if posicion_fila_columna == partes_barco_coordenadas[j]['coordenadas']:
                            print(j)
                            partes_barco_coordenadas[j]['parte_averiada'] = True # Marco la parte averiada
                            id_barco_tocado = partes_barco_coordenadas[j]['id_barco']
                            #print(f'>>> id_barco_tocado : {id_barco_tocado}')
                            #print(f' \n--- Puntaje_actual > {puntajes_juego_dict[usuario]['puntaje_actual']}')
                            # Valida si esta hundido
                            hundido = validar_barco_hundido(id_barco_tocado, partes_barco_coordenadas)
                            #print(f'>>> Barco hundido : {hundido}')

                            # Actualiza el puntaje
                            if hundido:
                                puntaje_hundido = 10 * partes_barco_coordenadas[j]['partes_del_barco'][1]
                                actualizar_puntaje(usuario, puntajes_juego_dict, puntaje_hundido)
                                #print(f' \n--- Puntaje_actual > {puntajes_juego_dict[usuario]['puntaje_actual']}')
            else:
                pygame.draw.rect(ventana, color_agua, rect_seleccionado)  # Redibujar el rectángulo con el nuevo color
                #print(f' Agua en las coordenadas: {rect_seleccionado.x, rect_seleccionado.y}')
                # MODIFICA EL PUNTAJE DEL USUARIO - 1
                nuevo_puntaje = -1
                actualizar_puntaje(usuario, puntajes_juego_dict, nuevo_puntaje)

            # Actualiza el marcador de los puntajes
            #actualiza_marcador(puntajes)
            actualiza_marcador(puntajes_juego_dict, ventana, puntaje_actual, x_puntajes, y_puntajes, usuario)
            pygame.display.update(rect_seleccionado)  # Solo actualiza el área del clic

            break  # Salir si ya toco un casillero 

    return puntajes_juego_dict


# VERIFICAR SI EL BARCO ESTA HUNDIDO PARA EL PUNTAJE
""" 
def validar_barco_hundido(id_barco, partes_barco_coordenadas) -> bool:
    
    for parte in partes_barco_coordenadas:
        id_barco = parte['id_barco']
        if id_barco not in barcos:
            barcos[id_barco] = []
        barcos[id_barco].append(parte['parte_averiada'])
        
    for id_barco, partes in barcos.items():
        hundido = True
        for parte in partes:
            if not parte: #not parte = True: True == True? >>> True 
                hundido = False
                break

    return hundido
 """
def validar_barco_hundido(id_barco, partes_barco_coordenadas) -> bool:
    # Evaluar si todas las partes del barco con el id proporcionado están averiadas
    for parte in partes_barco_coordenadas:
        if parte['id_barco'] == id_barco and parte['parte_averiada'] == False: # not (False) = True
            return False  # Si alguna parte no está averiada, no está hundido
    return True  # Todas las partes están averiadas


def obtener_partes_barco(id_barco, barcos_averiados, barcos_casilleros):

    # partes averiadas deberia estar en otro lado inicializada desde cero
    partes_averiadas = [] # [{}, {}, {}] va a tener partes(barco{}-casilleros) averiadas
    for barco in barcos_casilleros:
        if barco['id'] == id_barco:
            partes_averiadas.append(barco)  # Añadimos la parte del barco a la lista

    # Cuantas partes del barco han sido tocadas
    partes_tocadas = 0 
    if id_barco in barcos_averiados:
        if barcos_averiados[id_barco] != 0: # esta validacion ya la estoy haciendo en 
            partes_tocadas = barcos_averiados[id_barco]
        else:
            partes_tocadas = 0

    # Si el numero de partes tocadas es igual al numero total de partes del barco => hundido 
    hundido = False
    if partes_tocadas == len(partes_averiadas): # pero aca habria que agregar que sea para determiando barco
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

def comienza_juego(inicializar_matriz:callable, nivel:str):
    match nivel:
        case 'Facil':
            matriz = inicializar_matriz(10,10,0)
        case 'Medio':
            matriz =  inicializar_matriz(20,20,0) 
        case 'Dificil':
            matriz =  inicializar_matriz(40,40,0) 
    return matriz





