# Colores y fuentes utilizadas en el juego
import pygame

pygame.init()
#Colores
fondo_ventana = (0,0,0)
fondo_color_tablero = (203, 218, 242) # Celeste
# Casilleros
#color_casillero = (240, 28, 5) # Rojo para el texto
color_casillero_texto = (0,0,0) # Negro para el texto - para que no se vean los barcos
color_barco_tocado = (235, 86, 52) # Naranja
color_agua = (52, 235, 208) # celeste

color_letra_botones = (255,255,255)
color_letra_botones_activo = (230,230,230)
color_botones_juego = (0, 0, 255)
color_letra_puntaje = (210,210,210)

color_boton_jugar_inactivo = (0,0,255)
color_boton_nivel_inactivo = (0,0,255)
color_boton_puntaje_inactivo = (0,0,255)
color_boton_salir_inactivo = (0,0,255)
color_boton_nivel_activo = (0,0,180)
color_boton_jugar_activo = (0,0,180)
color_boton_puntaje_activo = (0,0,180)
color_boton_salir_activo = (0,0,180)
color_boton_puntaje = (15,15,15)
color_usuario_boton = (106, 46, 191)
color_usuario_boton_activo = (209, 20, 6)
color_usuario_boton_inactivo = (20, 209, 6)
color_boton_guardar = (0,255,50)


#Fuentes
fuente_botones = pygame.font.SysFont("Comic Sans" , 18, True) #tamaño de la letra
fuente_casilleros = pygame.font.SysFont('Times New Roman', 22, True, True)
fuente_puntaje_actual = pygame.font.SysFont('Verdana', 25, True, True)
