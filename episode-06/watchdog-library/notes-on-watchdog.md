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

Vamos a ver un ejemplo sencillo, solo monstrará un mensaje por pantalla cada
vez que se cree un fichero. En primer lugar realizamos una serie de
imporaciones:

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
_watchdog_, o una nuestra. 

En la clase hay varios metodos que podemos utilizar o redefinir. El
más básico es el método `dispatch` que recibe **todos** los eventos. La
implementación base lo que hace es reenviar los eventos a otros métodos, que se
corresponden con los tipos de eventos que se pueden producir. Por ejemplo, el
método `on_created` será llamado por `dispatch` para aquellos eventos
que sean resultado de la creación de un fichero o directorio. Otros métodos que
podemos reescribir son:

- `on_deleted`: llamado cuando se borra un fichero o directorio.

- `on_modified`: llamado cuando se modifica un fichero o directorio.

- `on_moved`: llamado cuando un fichero o directorio se renombra o se mueve a
  otra carpeta.

- `on_closed`: es llamado cuando se cierra un fichero abierto en modo de
  escritura.

- `on_any_event`: Llamado par todos los eventos. 


Vamos a crear en primer lugar
nuestra propia clase para el Handler, derivado de `FileSystemEventHandler`, y
sobreescribiremos el método `on_created`:


```python
class SimpleHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"hay un nuevo fichero {event.src_path}!")
```

Ahora necesitamos otro objeto, conocido como el observador (*Observer*),
que sera el que realmente monitoriza el sistema de ficheros. Para crearlo se le
pasa como primer parámetro una instancia de nuestro handler o manejador y como
segundo la ruta del sistema de archivos que queremos monitorizar. Tiene
otros parámetros adicioanles, en este ejemplo usaremos también `recursive`, que
sirve par indicar si debemos monitorizar solo la carpeta indicada o la carpeta
mas todas sus subcarpetas.


```python
my_observer.schedule(SimpleHandler(), '.', recursive=True)
```

Ya hemos creado el observador, y le hemos pasado nuestro manejador de
eventos. Lo hemos puesto vigilando el directorio actual (`.`), indicando
también que estamos interesados en los subdirectorios.

Ahora ya podemos iniciar el observador. Este proceso inicia un bucle
infinito, ya que la condición de salida del _while_ es la constante
`True`, que obviamente nunca va a cambiar de valor. La única manera
de salir de ese bucle infinito es provocando una interrupción en el nivel
superior del sistema operativo, con la combinación ++ctrl+c++.

```python
my_observer.start()
try:
    while True:
        time.sleep(10)
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

### Otros Handlers o manejadores

Además de poder crear nuestras propias clases de _Handlers_, watchdog
incluye otras clases derivadas más especializadas y que puede que nos sean
útiles.

La clase `PatternMatchingEventHandler` nos permite definir los tipos de
archivos en los que estamos interesados, y solo se nos informaran de los
eventos que afe3ctan a ese tipo de ficheros. Por ejemplo, podemos monitorizar
solo los cambios que afectan a ficheros `.PDF` o que ignore determionados
directorios, etc...

La clase `RegexMatchingEventHandler` es similar, pero nos deja usar expresiones
regulares para definir los ficheros que nos interesan.

Por último, la clase `LoggingEventHandler` es como la clase base pero envia a
un log todos los eventos que se producen.

### Utilidades de shell

Si hemos instalado wathdog, disponemos de una utilidad de línea de comandos
llamada `watchmedo`. Con `watchmedo --help` podemos obtener más información
sobre su uso.

El siguiente ejemplo muestra en un log todos los cambios realizados sobre
ficheros con las extensiones `*.txt` o `*.py`, ignorando los eventos
relacionados con directorios.

```shell
watchmedo log \
    --patterns="*.py;*.txt" \
    --ignore-directories \
    --recursive
```

Con la suborden `shell-command` podemos ejecutar un comanmdo de shell ante
cualquiera cambio monitorizado:

```shell
watchmedo shell-command \
    --patterns="*.py;*.txt" \
    --recursive \
    --command='echo "${watch_src_path}"'
```

Podemos predefinir en un fichero `tricks.yaml` diferentes operrciones a
realizar cuando se produzcan eventos en el sistema de ficheros. La sintaxis no
se complicada y se puede consultar en la [página de documentación de
Watchdog](https://python-watchdog.readthedocs.io/)

### Nota de cata

| Concepto               | Nivel |
| ---------------------- | ----- |
| Usa nombres divertidos | █████ |
| Utilidad               | ████░ |
| Revolucionario         | ███░░ |
