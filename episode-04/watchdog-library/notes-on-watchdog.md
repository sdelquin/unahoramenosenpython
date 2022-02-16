## Monitorizar cambios en el sistema de ficheros con Watchdog

**Watchdog** es una librería y un conjunto de utilidades para monitorizar
eventos del sistema de ficheros. Cada plataforma (Win32/64, Mac/OS, Unix/Linux)
usa API's diferentes para este proposito, así que Whatchdog funciona como una
interfaz comun para los tres sistemas.

Con esta libreria podemos establecer un programa que monitorize o vigile (de
ahí lo de *watchdog*) una parte del sistema de archivos. Cuando acurre algún
evento en este sistema, como que se borre un archivo, se cree  un directorio,
se renombre un fichero, etc. se nos notifica para que actuemos en consecuencia

Como ejemplo, podriamos poner la configuración de un router en un directorio, y
monitorizarlo con _watchdog_. Si se salva una nueva versión de la
configuración, podriamos:

1) Leer la nueva configuracion

2) Chequear que no hay errores

3) Enviar la configuración al router

4) Reiniciar el router


### Instalar watchdog

Se puede instalar con pip:

```shell
pip install watchdog
```

### Ejemplo

Vamos a ver un ejemplo"

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
```

El primer paso es crear un manejador de eventos, que es el objeto que va a
recibir las notificaciones del sistema de ficheros y actuará en consecuencia.
En esta caso usaremos la clase `FileSystemEventHandler`, que es la clase base
para los manejadores de eventos, aunque veremos que normalmente se suele usar
una clase derivada de esta, ya sea algunas de las incluidas con el propio
_watchdog_, o una clase nuestra. 

En la clase Base hay varios metodos que podemos utilizar o redefinir. El
más básico es el método `dispatch` que recive **todos** los eventos. La
implemntación base lo que hace es reenviar los eventos a otrosmétodos, que se
corresponden con los tipos de eventos que se pueden producir. Por ejemplo, el
método `on_created` será llamado por `dispatch` para aquellos eventos
que sean resultado de la creación de un fichero o directorio.


```python
my_event_handler = FileSystemHandler()
```

Ahora que hemos creado el _handler_, podemos escribir el código a ejecutar
cuando se produzcan los eventos.

vamos a definir uno para cuando se crea un fichero:

```python
def on_created(event):
    print(f"hay un nuevo {event.src_path} fichero!")
```

Ahora podemos asignar el evento a esta función:

```python
my_event_handler.on_created = on_created
```

Ahora necesitamos otro objeto, conocido como el observador (*Observer*),
que sera el que monitoriza el sistema de ficheros.

Vamos a crearlo:

```python
path = "."
go_recursively = True

my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
```

Ya hemos creado el observador, y le hemos pasado nuestro manejador de
eventos. Lo hemos puesto vigilando el directorio actual (`.`). Indicamos
que estamos interesados también en los subdirectorios.

Ahora ya podemos iniciar el observador. Este proceso inicia un ciclo
infinito, ya que la condición de salida del _while_ es la constante
`True`, que obviamente nunca va a cambiar de valor. La única manera
de salir de ese bucle infinito es provocando una interrupción en el nivel
superior del sistema operativo, con la combinación ++ctrl+c++.

```python
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
```

Ahora podemos abrir otra terminal, y crear un archivo desde el sistema
operativo. Con _Linux/Unix/MacOS_, lo mas fácil es usar el comando `touch`:

```shell
touch hola.txt
```

Para Windows una forma podría ser:

```shell
fsutil file createnew hola.txt 0
```

En la primera terminal, la que está ejecutando nuestro código `watchdog`,
deberíamos ver el mensaje indicando la creación del fichero.
