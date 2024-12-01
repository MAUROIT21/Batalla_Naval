### APUNTES DEL JUEGO DE BATALLA NAVAL




"""
. hacer el juego lo mas basico posible, primero la logica, luego la pantalla
. pueden ser los barcos todos horizontales, con 1 y ceros, con colores, o con imagenes. 
. Cada barco puede ser 1, 22, 333, 444 depende de su tamaño.
. Para cada pantalla, en realidad no hay pantallas. Por cada funcionalidad o boton, van apareciendo o desapareciendo los elementos, se va actualizando la pantalla.
. En el bucle principal, colocar las funciones que estan en la biblioteca, poca logica (solo lo necesario)
. En cada casillero (rectangulo), si acierta colocar o descubrir el nro acertado del tipo de barco o bien colocar una imagen de averia, Cruces y Circulos (fuego x ej) o agua si no acerto.







CORRECIONES:
+ Puntajes
+ El nombre del usuario puede ser guardado al principio o al salir y finalizar la partida.
- Agregar el boton de volver al menu principal
+! Al ir y volver de las pantallas, desabilitar los botones y tablero

- PASAR SIEMPRE EN LAS FUNCIONES LOS PARAMETROS! 
- Llevar todas las funciones a biblioteca_funciones
- Refactorizar funcion enumerate()
- Cambiar el tablero que no se vean los barcos
- Imagen de fondo para el tablero
- Sacar boton ver puntajes en la pantalla del tablero y directamte mostrarlo 
- Colores para los casilleros del tablero
- Minusculas para todas las variables
"""

""" 
LOGICA DEL BARCO HUNDIDO
. Cuanto toco un casillero con una parte del barco, esa parte debe cambiar su estado. 
    Al mismo tiempo, deberia validar si el barco esta hundido o no al tocar esa parte.
    Si esta hundido realiza el calculo del puntaje y sino no lo hace. 

1) > barcos_casilleros = creada en dibuja tablero : lista de dict de cada casillero con sus coordenadas, valor
    casillero_rect = {'x':rect_tablero.x, 'y':rect_tablero.y, 'valor':barco_valor, 'id':id_casillero, 'fila': fila, 'columna': columna}

2) > barcos_averiados = se crea en dibuja_tablero > inicializa cada casillero en 0, quizas no la uso!?!?

3) > [lista_posiciones_barcos] = [partes_barco_coordenadas] = creada en ubicar_barcos_aleatoriamente: 

{   'id_barco': id_barco, 
    'coordenadas': (pos_fila, pos_columna),
    'partes_del_barco': (parte, largo_barco),
    'parte_averiada': False/True
} 

 """