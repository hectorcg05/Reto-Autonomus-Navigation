
# Reto-Autonomus-Navigation
Este codigo (Codigo AUTONOMUS NAVIGATION) presenta una simulación de un rover buscando a un codigo ArUco mediante la biblioteca de turtle de Python. A continuación se describirá cada parte del codigo.

## Sección de funciones
Se definió una función para cada movimiento del rover (derecha, izquierda, arriba y abajo), esto para que se pueda realizar el algortimo de busqueda que más abajo se explicará. Se tomo como referencia un plano cartesiano en dimensión 2D con eje X y eje Y, un movimiento a la derecha suma 1 en terminos de X (x+1, y), para la izquierda resta 1 en x (x-1, y), para moverse hacia arriba se suma 1 en Y (x, y+1) y para abajo se resta 1 en Y (x, y-1). Se definio como limite de suma. 

#### Dato extra de las funciones
Para cada una de las 4 funciones se definieron limites para que en algún punto ya no avance en cualquier eje, para las funciones de izquierda y derecha se definio que solo se mueva si el Rover esta dentro del rango de la pantalla (400px) y para las funciones de arriba y abajo se definio como limite 295px para que no se salga de la ventana de visualización. 
También para cada una de las funciones se declaro que si la distancia entre el Rover y el ArUco es menor a 4 unidades que el ArUco desaparezca y sume 1 en el contador, esto se explicará más a detalle después. 


## Formato de la ventana
Más abajo se definio el tamaño de la pantalla como 800 pixeles de ancho y 600 de alto, es decir 400 px en el eje x negativo y 400 px en el x positivo, para el eje Y positivo 300 pixeles y 300 px para el Y negativo, por esto se definieron limites en el movimiento del Rover.

## Declaración y carga de variables
Para que la visualización del programa sea más grafica se utilizaron imagenes que representen al Rover (ROVERM), al ArUco y al fondo (MARTEESCENARIO), también se definieron sus terminaciones (pac,pac1 y escenario) para guardar la carga de imagenes.
Como se definió en el reto, se declaro que el rover inciara en el origen (0,0) y que el codigo ArUco iniciara en una posición aleatoria dentro de la ventana (entre el eje X (-380,380) y el eje Y (-280,280)).

## Algoritmo de búsqueda
El algoritmo de búsqueda se basa en la función "while". Para este algoritmo se va a utilizar la distancia entre el rover y el ArUco como recurso principal para la búsqueda autonoma. Primero se almacena en una variable la distancia entre ambos objetos después el algoritmo consiste en hacer movimientos del rover dentro del mapa para determinar si se aleja o se acerca al ArUco. Inicia con un movimiento hacia arriba y la nueva distancia se almacena en otra variable, esto para comparar estas distancias, si la distancia después del movimiento hacia arriba bajo significa que se esta acercando al ArUco y lo seguira haciendo hasta que en vez de disminuir la distancia incremente, para esto se utilizo el ciclo while. Este mismo algoritmo se utilizo para movimientos hacia abajo, izquierda y derecha, gracias a este algortimo, el rover seguira moviendose hasta que llegue al ArUco, cuando la distancia entre el rover y el ArUco sea menor a 4 se sumara 1 al contador previamente definido, desaparecerá la imagen del ArUco debido a que ya lo encontro, y al final se determina una condición que si el contador es igual a 1 (o sea que ya encontro al ArUco) se rompa el programa y termine la simulación. 
![image](https://github.com/hectorcg05/Reto-Autonomus-Navigation/assets/135381068/d922324b-cb3f-410c-ba54-124ef95a8c0b)
En este plano se muestra la representación de las distancias y ayuda a entender el algoritmo, la distancia entre el rover y el ArUco no ayuda a saber la posición en el mapa del ArUco ya que podría estar en cualquier bloque del plano, y gracias al algoritmo determina en que sentido se tiene que mover el rover para que disminuya la distancia y llegue al ArUco
