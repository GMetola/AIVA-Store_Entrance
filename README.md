# AIVA-Store_Entrance

De una manera resumida, el sistema grabará permanentemente el escaparate y la entrada de una tienda y contabilizará los usuarios que entran en ella; comparando con los usuarios que han pasado por delante de la misma.

### Procedimiento de ejecución

Este código se puede descargar mediante un git clone sobre el url de esta pagina o mediante la pestaña download en la parte superior izquierda.

Este código se puede ejecutar dentro de un sistema que contenga las librerias detalladas en el requirements.txt

## Implantación a través de docker
Por comodidad para el usuario, hemos habilitado un container de docker descargable aquí (https://hub.docker.com/r/metolag/videoanalysis-peopledetector)
A través del docker "metolag/videoanalysis-peopledetector", podrá obtener todas las librerías necesarias.

Tras cargar el docker, debe entrar en la carpeta AIVA-Store_Entrance, descargada directamente de GitHub.
Hay que introducir un vídeo en dicha carpeta del docker.
Para ejecutar el programa deberá introducir el siguiente comando:
  - python FollowPeople.py -video "nombre del video.extension"

Para comodidad del usuario, se ha incluido un vídeo en el propio Git, por lo que, para realizar una prueba, puede ejecutar lo siguiente:
- python FollowPeople.py -video EnterExitCrossingPaths1front.mpg

El formato del video puede ser diferente y no ha de ir entre comillas.
Los resultados se obtendran en la misma dirección donde este almacenado el codigo.

#### Ayuda

No dude en ejecutar la función help() en caso de cualquier duda con partes del código. Ejemplo: help(Ff)

## Autores

* **Gabriel Metola** - *Responsable de producto* - (https://github.com/GMetola)
* **Francisco José Vega** - *Gestor de desarrollo* - (https://github.com/franjvega)

Vea una lista de participantes [contributors](https://github.com/GMetola/AIVA-Store_Entrance/graphs/contributors) que participaron en este proyecto.

