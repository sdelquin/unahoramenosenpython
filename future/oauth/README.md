# Interfaz de línea de comandos para twitter

El codigo del artículo orgiginal es un poco farragoso, pero toca
varios aspectos interesantes

Linrerias usados:
- request
- request_oauth
- click
- rich
- poetry
    

Una cosa interesante de este articulo es que nos habla de determinados
metadatos que por lo visto twitter incluye en cada tweet,y que puede
ser muy interesante para filtarlos. La gente de Twitter tiene en un
repositorio de GitHub un fichero CSV enorme con las categorias que le
puede asignar a un tweet. 

    <https://github.com/twitterdev/twitter-context-annotations>

Cada entrada en este fichero describe una entidad usando tres valores:

- uno o más identificadores de dominio (`domain_id`)
- un identificador de la entidad (`entity_id`)
- el nombre de la entidad (`entity_name`) 

Por ejemplo, en el fichero csv podriamos ver
que tenemos esta entrada para Python:

```
131,1357506193879486469,Python
```

O esta otra para _Machine Learning_:

```
"66,131",898661583827615744,Machine learning
```

Esta entrada está vinculada a dos dominios, en estos casos viene entrecomillada
y con los valores separados por comas. Pero la que nos interesa sería la
entrada `entity_id`. En teoría, si filtramos por ese valor de entidad, nos
devolveria los tweets que hablan sobre Python.



Each entry consists of the domain_id, entity_id and entity_name. We can see that ML falls under the Interests and Hobbies category with a domain_id of 66 and an entity_id of 852262932607926273.

Fuente: [Building an authenticated Python CLI](https://www.notia.ai/articles/building-an-authenticated-python-cli)
