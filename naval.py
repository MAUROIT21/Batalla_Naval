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


# Dibujar el tablero
ancho_casillero = 45
tamaño_tablero = 10

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

            if estado_pantalla == 'cargado':
                click_tablero(coordenadas_click, tamaño_tablero, ancho_casillero, ANCHO_PANTALLA, ALTO_PANTALLA, barcos_casilleros, matriz_datos, puntajes, usuario, barcos_averiados, ventana, puntaje_actual,  x_puntajes, y_puntajes, color_barco_tocado, color_agua)
                
            if volver_menu.collidepoint(coordenadas_click):
                estado_pantalla = 'inicio'
                # Reiniciar puntaje_marcador, volver al menu
                # Deberia cargar el juego de nuevo, su fondo de pantalla, los botones del menu y la musica.


            # boton Reiniciar: solo reinicia el tablero, no cambia de pantalla.
                
        
    
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
            # Limpiar pantalla, tablero, puntajes            
            usuario = menu_juego(ventana, imagen_barcos, nivel, jugar, puntajes_historicos, salir, color_boton_nivel, color_boton_jugar, color_boton_puntaje, color_boton_salir, y_boton, x_boton)
            puntajes = puntaje(usuario)
        case 'inicia_juego':
            # poner activos los botones y marcador

            datos_retorno_jugando = jugando(tamaño_tablero, ancho_casillero, ventana, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, ALTO_PANTALLA, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha)
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



