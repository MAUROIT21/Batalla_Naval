from biblioteca_funciones import *
import pygame
from colores_naval import *

#Inicia el juego
pygame.init()
sonido_juego()

puntajes_juego_dict = {}
ruta = 'teoria_juegos/Batalla_Naval/puntajes.json'

def cargar_puntajes_json(ruta):
    with open(ruta, "r") as archivo:
        cargado = json.load(archivo)
        return cargado

puntajes_juego_dict = cargar_puntajes_json(ruta)
#print(puntajes_juego_dict)

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

volver_atras = pygame.Rect(350, 500, 70, 50)

# Botones durante el juego (a la derecha del tablero)
x_boton_derecha = ANCHO_PANTALLA - 150  # Margen derecho
y_boton_derecha = 100
x_puntajes = 325
y_puntajes = 15
x_caja_texto = 575
y_caja_texto = 15   
x_guardar = 300
y_guardar = 550
salir_jugando = pygame.Rect(x_boton_derecha, y_boton_derecha, ancho_boton, alto_boton)
puntaje_actual = pygame.Rect(x_puntajes, y_puntajes, ancho_boton, alto_boton)
reiniciar_jugando = pygame.Rect(x_boton_derecha, y_boton_derecha + 100, ancho_boton, alto_boton)
volver_menu = pygame.Rect(x_boton_derecha, y_boton_derecha + 200, ancho_boton, alto_boton)
usuario_caja_texto = pygame.Rect(x_caja_texto, y_caja_texto, ancho_boton + 90, alto_boton)
guardar_puntaje = pygame.Rect(x_guardar, y_guardar, ancho_boton + 30, alto_boton-10)


# Dibujar el tablero
ancho_casillero = 45
tamaño_tablero = 10


# EJECUCION DEL JUEGO
estado_pantalla = 'inicio'
        
corriendo = True
ingreso_texto = ''

while corriendo:
    # bucle del juego
    

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            estado_pantalla = 'saliendo' # > saliendo
            corriendo = False
        
        # Capturar eventos de teclado
        if evento.type == pygame.TEXTINPUT:
            if usuario_caja_texto.collidepoint(pygame.mouse.get_pos()):  # Solo cuando el mouse está sobre la caja
                largo_texto = len(ingreso_texto)

                if largo_texto < 10:  
                    ingreso_texto += evento.text
                else:
                    print('Texto supera el limite...')

        elif evento.type == pygame.KEYDOWN:
            if usuario_caja_texto.collidepoint(pygame.mouse.get_pos()):  # Solo cuando el mouse está sobre la caja
                if evento.key == pygame.K_BACKSPACE:
                    ingreso_texto = ingreso_texto[:-1]  # Borrar último carácter
                elif evento.key == pygame.K_RETURN:
                    usuario = ingreso_texto
                    # guardar aqui el usuario y crear el nuevo dict{usuario} en puntajes_juego_dict{}
                    inicializa_usuario_nuevo(usuario, puntajes_juego_dict)
                    print(puntajes_juego_dict)
                    print("Usuario ingresado:", usuario)
        txt_usuario_boton = ingresar_usuario_texto(ventana, usuario_caja_texto, ingreso_texto)
        pygame.display.update(usuario_caja_texto)
        

        # Eventos al hacer click
        if evento.type == pygame.MOUSEBUTTONDOWN:
            coordenadas_click = pygame.mouse.get_pos()

            if jugar.collidepoint(coordenadas_click):
                usuario = ingreso_texto
                inicializa_marcador(usuario, puntajes_juego_dict, x_puntajes, y_puntajes, ventana, puntaje_actual)

                estado_pantalla = 'inicia_juego'
                
            if salir.collidepoint(coordenadas_click) or salir_jugando.collidepoint(coordenadas_click):
                estado_pantalla = 'saliendo'
                corriendo = False
            
            if puntajes_historicos.collidepoint(coordenadas_click):
                estado_pantalla = 'puntajes_historicos'

            if estado_pantalla == 'cargado':
                usuario = ingreso_texto
                puntajes_juego_partida = click_tablero(coordenadas_click, tamaño_tablero, ancho_casillero, ANCHO_PANTALLA, ALTO_PANTALLA, barcos_casilleros, matriz_datos, puntajes_juego_dict, usuario, barcos_averiados, ventana, puntaje_actual, x_puntajes, y_puntajes, color_barco_tocado, color_agua, partes_barco_coordenadas, rectangulos)
                
                if guardar_puntaje.collidepoint(coordenadas_click):
                    usuario = ingreso_texto
                    print(usuario)                    
                    actualizar_puntaje_cierre(usuario, puntajes_juego_partida)
                    inicializa_marcador(usuario, puntajes_juego_partida, x_puntajes, y_puntajes, ventana, puntaje_actual)
                    guardar_puntaje_json(puntajes_juego_partida)
                    estado_pantalla = 'inicio'
                
            if volver_menu.collidepoint(coordenadas_click) or volver_atras.collidepoint(coordenadas_click):
                estado_pantalla = 'inicio'
                
            if reiniciar_jugando.collidepoint(coordenadas_click):
                estado_pantalla = 'inicia_juego'
            
    # Eventos de colores
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
            menu_juego(ventana, imagen_barcos, nivel, jugar, puntajes_historicos, salir, color_boton_nivel, color_boton_jugar, color_boton_puntaje, color_boton_salir, y_boton, x_boton, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, usuario_caja_texto, ANCHO_PANTALLA, txt_usuario_boton, guardar_puntaje, volver_atras)
        case 'inicia_juego':
            datos_retorno_jugando = jugando(tamaño_tablero, ancho_casillero, ventana, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, ALTO_PANTALLA, color_boton_salir, color_boton_puntaje, salir_jugando, puntaje_actual, reiniciar_jugando, volver_menu, x_puntajes, x_boton_derecha, y_puntajes, y_boton_derecha, usuario_caja_texto, color_usuario_boton, txt_usuario_boton, color_boton_guardar, guardar_puntaje, x_guardar, y_guardar, volver_atras)
            matriz_datos = datos_retorno_jugando[0]
            barcos_casilleros = datos_retorno_jugando[1]
            barcos_averiados = datos_retorno_jugando[2]
            partes_barco_coordenadas = datos_retorno_jugando[3]
            rectangulos = datos_retorno_jugando[4]
            inicializa_marcador(usuario, puntajes_juego_dict, x_puntajes, y_puntajes, ventana, puntaje_actual)
            estado_pantalla = 'cargado'
        
        case 'cargado':
            pass
        
        case 'puntajes_historicos':
            ordenado = ordena_puntajes_historicos(puntajes_juego_dict)
            los_mejores_3 = ordenado[0]
            #print(los_mejores_3)
            #print(len(los_mejores_3))            

            crear_pantalla_historicos(ventana, los_mejores_3, imagen_fondo_oceano, nivel, jugar, puntajes_historicos, salir, ANCHO_PANTALLA, volver_atras)

            estado_pantalla = 'ver_puntajes'
            
            # Cambia de pantalla, ejecuta el ordenamiento, muestra resultados e imprime en pantalla. Boton de volver (podria ser el mismo que el otro de Volver)
        case 'ver_puntajes':
            volver_atras.x = 350

        case 'saliendo':
            saliendo(usuario)

# Refresh de la pantalla de juego
    pygame.display.update()


pygame.quit()



