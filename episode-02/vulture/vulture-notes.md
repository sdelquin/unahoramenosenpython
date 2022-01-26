## Vulture

![Vulture#](./vulture.jpg)


### Que es vulture

: Analiza código python buscando código muerto, es decir, partes del programa que
nunca se ejecutan

Ojo: Dada la naturaleza dinamica de Python, no puedes estar totalmente seguro de que una
función, por ejemplo, no sea llamada. Eso significa que la certeza de que un fragmento de
código sea ejecutada no es `True`/`False` sino que se indica con un porcentaje o
probabilidad de que el código esté realmente muerto.

Si nos reporta un 100%, es que es seguro que ese codigo no se va a ejecutar nunca (Por
ejemplo, lo que venga detras de un return):

Ver [vulture_sample_01.py](vulture_sample_01.py)

[Ejemplo de uso]

### Falso positivos

Se puede crear un whitellist. Aun mejor, puedes hacer que vulture te genere la whitelist por
tí:

```
vulture vulture_sample_01.py --make-whitelist > whitelist.py
```

Y luego podemos usar el fichero de _whitelist_ como segundo parámetro:

```
vulture vulture_sample_01.py whitelist.py
```


Produce la misma salida que [pyflakes](https://github.com/PyCQA/pyflakes)/

### Flake8 noqa

A modo de compatibilidad con [flake8](https://flake8.pycqa.org/en/latest/), Vulture
soporta el uso de un comentario con el texto `# NOQA` para ignorar tanto la importacion
de módulos no usados como la asignación a variables sin uso.

Se puede integrar con herramientas de CI


## Enlaces:

- [Repositorio en GitHub de Vulture](https://github.com/jendrikseipp/vulture)
- [Python Repo - Find dead Python code](https://pythonrepo.com/repo/jendrikseipp-vulture-python-code-refactoring)

