from biblioteca_funciones import *
import pygame
from colores_naval import *

#Inicia el juego
pygame.init()

sonido_juego()

# Configuracion de la pantalla/ventana
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600
ventana = pygame.display.set_mode([ANCHO_PANTALLA, ALTO_PANTALLA])
ventana.fill(fondo_ventana)

pygame.display.set_caption("Batalla Naval 1.0")
logo = pygame.image.load("teoria_juegos/Batalla_Naval/imagenes_naval/logo_barcos.jpg")
pygame.display.set_icon(logo)


# Imagen barco
imagen_barcos = pygame.image.load('teoria_juegos/Batalla_Naval/imagenes_naval/logo_batalla_naval.jpg')
imagen_barcos = pygame.transform.scale(imagen_barcos, (800, 600))
imagen_barcos.set_alpha(5)
rect_img_barcos = imagen_barcos.get_rect()
rect_img_barcos.x = 20
rect_img_barcos.y = 35

# Imagen Oceano fondo tablero
imagen_fondo_oceano = pygame.image.load('teoria_juegos/Batalla_Naval/imagenes_naval/oceano.jpg')
imagen_fondo_oceano = pygame.transform.scale(imagen_fondo_oceano, (800, 600))
imagen_fondo_oceano.set_alpha(150)

# Imagen barco
imagen_fondo_tablero = pygame.image.load('teoria_juegos/Batalla_Naval/imagenes_naval/Fondo_blanco.jpg')
imagen_fondo_tablero = pygame.transform.scale(imagen_fondo_tablero, (800, 600))
#imagen_fondo_tablero.set_alpha(5)
rect_img_fondo_blanco = imagen_fondo_tablero.get_rect()
#rect_img_fondo_blanco.x = 20
#rect_img_fondo_blanco.y = 35



# Botones del menu
ancho_boton = 120 
alto_boton = 50
x_boton = ANCHO_PANTALLA/7
y_boton = 500

nivel = pygame.Rect(x_boton, y_boton, ancho_boton, alto_boton)
jugar = pygame.Rect(x_boton + 150, y_boton, ancho_boton, alto_boton)
puntajes_historicos = pygame.Rect(x_boton + 300, y_boton, ancho_boton, alto_boton)
salir = pygame.Rect(x_boton + 450, y_boton, ancho_boton, alto_boton)

# Botones durante el juego (a la derecha del tablero)
x_boton_derecha = ANCHO_PANTALLA - 150  # Margen derecho
y_boton_derecha = 100
x_puntajes = 325
y_puntajes = 15
salir_jugando = pygame.Rect(x_boton_derecha, y_boton_derecha, ancho_boton, alto_boton)
puntaje_actual = pygame.Rect(x_puntajes, y_puntajes, ancho_boton, alto_boton)
reiniciar_jugando = pygame.Rect(x_boton_derecha, y_boton_derecha + 100, ancho_boton, alto_boton)
volver_menu = pygame.Rect(x_boton_derecha, y_boton_derecha + 200, ancho_boton, alto_boton)

def dibujar_botones_juego(ventana:pygame.Surface):
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
def botones_menu_inactivos():
    # LOS SACO DE LA PANTALLA
    nivel.x = ANCHO_PANTALLA-1000
    jugar.x = ANCHO_PANTALLA-1000
    puntajes_historicos.x = ANCHO_PANTALLA-1000
    salir.x = ANCHO_PANTALLA-1000

def botones_menu_activos ():
    # vuelven a su posicion original activos.
    nivel.x = x_boton
    jugar.x = x_boton + 150
    puntajes_historicos.x = x_boton + 300
    salir.x = x_boton + 450


# Dibujar el tablero
ancho_casillero = 45
tamaño_tablero = 10


def dibuja_tablero(ventana, posicion_x, posicion_y, matriz_barcos): # dibuja el tablero completo con valores

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
        
def dibuja_rects(ventana, posicion_x, posicion_y): # Dibujo el tablero con sus rectangulos sin valores, para poder machear el click del usuario en estos

    rectangulos = []
    for fila in range(tamaño_tablero):
        for columna in range(tamaño_tablero):
            
            x_rect = posicion_x + columna * ancho_casillero
            y_rect = posicion_y + fila * ancho_casillero
            rect_tablero = pygame.Rect(x_rect, y_rect, ancho_casillero, ancho_casillero)
            rectangulo_tablero = pygame.draw.rect(ventana, fondo_color_tablero, rect_tablero, 1)  # Dibuja las líneas del tablero
            rectangulos.append(rectangulo_tablero)
    return rectangulos


#Configuraciones para cada estado/pantalla del juego
def menu_juego():
    ventana.blit(imagen_barcos, (0,0)) # Imagen de Fondo
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


def jugando (ventana):
    ventana.fill(fondo_ventana) # detras de la imagen fondo negro
    ventana.blit(imagen_fondo_oceano, (0,0)) # imagen fondo del tablero 
    botones_menu_inactivos() # Desactiva los botones del menu al comenzar el juego
    dibujar_botones_juego(ventana)
    matriz_barcos_ubicados = a_jugar() # Se genera la logica del juego.
    
    retorno_lista_rects = dibuja_tablero(ventana, posicion_x=ANCHO_PANTALLA/5, posicion_y=ALTO_PANTALLA/7, matriz_barcos= matriz_barcos_ubicados) # Se prepara el tablero
    lista_rects_generados = retorno_lista_rects[0] 
    barcos_xy_valor = retorno_lista_rects[1]
    barcos_averiados = retorno_lista_rects[2]
    
    datos_retorno = [matriz_barcos_ubicados, lista_rects_generados, barcos_xy_valor, barcos_averiados]
    return datos_retorno

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

def actualiza_marcador(puntajes):
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

# Interaccion con el tablero
def click_tablero(matriz, puntajes, usuario, barcos_averiados):
    lista_rects_valores = dibuja_rects(ventana, posicion_x=ANCHO_PANTALLA/5, posicion_y=ALTO_PANTALLA/7)
    
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

            actualiza_marcador(puntajes)
            break  # Salir si ya toco un casillero 

    return puntajes

# EJECUCION DEL JUEGO
estado_pantalla = 'inicio'

corriendo = True
while corriendo:

    # bucle del juego
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            estado_pantalla = 'saliendo' # > saliendo
            corriendo = False

        # Eventos al hacer click
        if evento.type == pygame.MOUSEBUTTONDOWN:
            coordenadas_click = pygame.mouse.get_pos()

            if jugar.collidepoint(coordenadas_click):
                estado_pantalla = 'inicia_juego' # > inicia_juego
                
            if salir.collidepoint(coordenadas_click) or salir_jugando.collidepoint(coordenadas_click):
                estado_pantalla = 'saliendo' # > saliendo
                corriendo = False
            
            if puntajes_historicos.collidepoint(coordenadas_click):
                pass

            # Eventos al hacer click en un casillero del tablero
                # si el click es en algun casillero

            if estado_pantalla == 'cargado':
                click_tablero(matriz_datos, puntajes, usuario, barcos_averiados)
                
                
        
                
    
    #Eventos de colores
    # De los botones
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if nivel.collidepoint(mouse_x, mouse_y):
        color_boton_nivel = color_boton_nivel_activo
    else:
        color_boton_nivel = color_boton_nivel_inactivo
    if jugar.collidepoint(mouse_x, mouse_y):
        color_boton_jugar = color_boton_jugar_activo
    else:
        color_boton_jugar = color_boton_jugar_inactivo
    if puntajes_historicos.collidepoint(mouse_x, mouse_y):
        color_boton_puntaje = color_boton_puntaje_activo
    else:
        color_boton_puntaje = color_boton_puntaje_inactivo
    if salir.collidepoint(mouse_x, mouse_y):
        color_boton_salir = color_boton_salir_activo
    else:
        color_boton_salir = color_boton_salir_inactivo

    # Estados del juego
    match estado_pantalla:
        case 'inicio':
            usuario = menu_juego()
            puntajes = puntaje(usuario)
        case 'inicia_juego':
            # datos_retorno = [matriz_barcos_ubicados, lista_rects_generados, barcos_xy_valor]
            
            datos_retorno_jugando = jugando(ventana)
            matriz_datos = datos_retorno_jugando[0]
            barcos_casilleros = datos_retorno_jugando[2]
            barcos_averiados = datos_retorno_jugando[3]
            estado_pantalla = 'cargado'

            
        case 'cargado':
            pass
            #estado_pantalla = 'pausa'
        
        case 'pausa':
            pass

        case 'reinicia':
            pass
        
        case 'saliendo':
            saliendo(nick='Mauro')



    
    
            

        

# Refresh de la pantalla de juego
    pygame.display.update()



pygame.quit()



