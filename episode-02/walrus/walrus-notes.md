## Walrus Operator

- Nombre técnico: _Assignment expression operator_

- Sintax and semantic:

> In most contexts where arbitrary Python expressions can be used, a named expression can
> appear. This is of the form NAME := expr where expr is any valid Python expression other
> than an unparenthesized tuple, and NAME is an identifier.

def statement [Sentencia] -> hace algo

def expression [Expresión] -> evalua un valor

- Qué hace `=`: Asignar una variable

- Que hace `:=`: Asignar una variable **Y devolver el valor**

Principio de diseñó: No se debería poder usar ambos operadores de
forma intercambiable, la asignación normal y el Walrus, para evitar errores.

Ejemplo del tipo de errores que queremos evitar:

En C podías hacer

```c
#include <stdio.h>

int main(int argc, char *args) {
    int a;
    a = 1;
    if (a = 23) {
        printf("a vale %d", a);
    }
}
```

El resultado de esto es que se imprime "a vale 23". [Por qué?] El codigo correcto sería:

```c
#include <stdio.h>

int main(int argc, char *args) {
    int a;
    a = 1;
    if (a == 23) {
        printf("a vale %d", a);
    }
}
```

Se ha intentado que esto no pueda pasar en Python, de forma que no se puedan intercambiar
libremente una expresion con `=` con otra con `:=`

Es decir, en Python podemos hacer:

```python
>>> a = 23
```

Pero no:

```python
>>> a := 23
  File "<stdin>", line 1
    a := 3
      ^
SyntaxError: invalid syntax
```

Podrias hacer:

```python
>>> (a := 23)
```

Pero está totalmente desaconsejado. En cualquier caso, reemplazar el `:=` por `=` también da
error aquí:

```python
>>> (a = 23)
  File "<stdin>", line 1
    (a = 23)
       ^
SyntaxError: invalid syntax
```

En general, en cualquier sitio donde tengas una expresion puedes usar el operador walrus:

```python
>>> print(10 + 5)
15
>>> print(n := 10 + 5)
15
>>> assert n == 15
>>> print(n = 15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'n' is an invalid keyword argument for print()
```

## Ejemplos de uso:

### Para evitar llamadas duplicadas

Ver [walrus_sample_01.py](walrus_sample_01.py)

### En un bucle While:

```python
name = input('Como te llamas: ')
while name:
    print(f"Hola, {name}!")
    name = input('Como te llamas: ')
```

Puede reescribirse con dos líneas menos:

```python
while name := input('Como te llamas:'):
    print(f"Hola, {name}!")
```

Además, se evita otro error común que sería cambiar una de las sentencias pero olvidarnos
de la otra.

### Expresiones regulares

Este es para mí el caso más claro:

Ver [walrus_sample_02.py](walrus_sample_02.py).

### Compresiones

Otro caso frecuente es para evitar cálculos duplicados en la comprensión. Por ejemplo,
supongamos que tenemos una lista de números y quiero obtener otra lista con los cubos de
esos

números, pero solo si son menores que $47$. Podemos hacerlo así:

```python
>>> items = [11, 7, 3, 2, 6]
>>> print([x**3 for x in items if x**3 < 47])
[27, 8]
```

El problema es que esto realiza la operación de elevar al cudo **dos veces**, una para la
comprobación y otra para calcular el valor a almacenar. Podemos evitar el doble cálculo así:

```python
items = []
for item in items:
    cube = item ** 3
    if cube < 47:
        items.append(cube)
```

Pero esto nos priva de las ventajas de la comprensión de listas. Ahora con el operador `:=`
podemos evitar las llamadas inncesarias facilmente:

```python
items = [11, 7, 3, 2, 6]
print([cube for x in items if (cube := x**3) < 47])
```

Nota: Los paréntesis son necesarios aquí. ¿Por qué?

De nuevo, se evita también el error común de olvidarnos de cambiar todas las expresiones.

## Reglas básicas para el cuidado de los ~~Gremlins~~ Walrus

- No funcionan dentro de las _f-strings_

- Solo se pueden asignar nombres simples

- No se produce desempaquetado de tuplas con el operador walrus

- Ojo con la prioridad, es muy baja

```python
>>> number = 3
>>> if square := number ** 2 > 5:
...     print(square)
...
True
```

### Recomendaciones de estilo

Son similares a las del operador `=`, dejar espacios alrededor del operador y usar
paréntesis para establecer la jerarquía, pero no más paréntesis de los necesarios.

## Integraci'on continua

Se puede usar un _pre-commit_ _hook_ para que Vulture se ejecute en cada
_Commit_to run Vulture before each commit. Para eso hay que tener el siguiente contenido
en el fichero `.pre-commit-config.yaml` dentro de tu repositorio.

```
repos:
  - repo: https://github.com/jendrikseipp/vulture
    rev: 'v2.3'  # or any later Vulture version
    hooks:
      - id: vulture
```

## Score

| Concepto               | Nivel |
| ---------------------- | ----- |
| Usa nombres divertidos | █████ |
| Utilidad               | ██░░░ |
| Revolucionario         | █░░░░ |

### Enlaces

- [PEP 572 -- Assignment Expressions](https://www.python.org/dev/peps/pep-0572/)

- [Real Python - The Walrus operator](https://realpython.com/python-walrus-operator/)

- [Toward Data Science - The Walrus Operator in Python](https://towardsdatascience.com/the-walrus-operator-in-python-a315e4f84583)

- [PyCon 2019 talk PEP 572: The Walrus Operator](https://pyvideo.org/pycon-us-2019/pep-572-the-walrus-operator.html)
