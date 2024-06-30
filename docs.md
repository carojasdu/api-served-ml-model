# Prueba técnica: Python Developer

## Carolina Rojas Duque - Quipux - 29 de junio de 2024

Este documento contiene una descripción corta de los pasos llevados a cabo para la solución de la prueba, así como instrucciones para su verificación.

### Sobre el modelo de clasificación

El modelo se entrenó en el archivo `model/model_generation.py`. Notando que esta parte no era la más fundamental en la prueba, no se le dedicó mucho tiempo a indagar sobre el desempeño del mismo ni a intentar diferentes modelos y estrategias, sino que se entrenó un *RandomForest* para clasificación, que es adecuado para el número de datos y características del dataset. Se hizo una partición de 80% entrenamiento y 20% prueba, obteniendo un accuracy del 100%, que, de nuevo, debería verificarse con validación cruzada o metodologías adicionales de Machine Learning.

Los pesos se guardaron en formato **joblib**, que se usa típicamente dado que optimiza el tamaño del archivo. Esto es una buena práctica y resulta útil, debido a que anexaremos este archivo al contenedor de Docker.

### Sobre la API

Se implementó la API con **FastAPI**, generándose un endpoint en `/` con un mensaje descriptivo de la misma, y otro en `/predict` con las especificaciones solicitadas. Gracias al framework usado, es posible acceder a `/docs` para ver una documentación técnica y estandarizada de los mismos, así como facilidades para ensayarlos.

La estructura del .json de entrada del endpoint `/predict` es de la siguiente forma:

```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```
donde los valores presentados corresponden a la primera muestra del dataset. En cuanto a la estructura de salida, es de la siguiente forma:

```json
{
  "prediction": 0
}
```
siendo el valor presentado, el correspondiente a los valores anteriores. Se decide devolver la clase numérica, para permitir mayor flexibilidad en el post-procesamiento de la salida de la API.

### Contenerización

El archivo `Dockerfile` contiene la configuración para la creación de la imagen a partir de la cual crear el contenedor que despliega la API. Este requiere el archivo de pesos, el script de la API y el archivo de `requirements.txt` con las librerías necesarias. 

Se verificó la inclusión de las dependencias estrictamente necesarias para el despliegue de la aplicación, con el fin de garantizar eficiencia en el peso del contenedor. Además, se guardan los archivos dentro de una carpeta específica en el contenedor para mejores prácticas. 

Para crear la imagen corra:

```bash
docker build -t model-api .
```

ubicándose en la carpeta descomprimida. Y para desplegar el contenedor localmente:

```bash
docker run --name model-api-container -p 8000:8000 model-api
```

con lo cual el contenedor queda desplegado en el puerto 8000. En este punto puede acceder a [http://localhost:8000/docs](http://localhost:8000/docs) y ensayar los endpoints con diferentes valores.

#### Pruebas para cada clase

A continuación se dejan estructuras **.json** de una muestra de cada clase, extraídas del dataset Iris.

Clase 0 (Setosa):

```json
{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
}
```

Clase 1 (Versicolour):

```json
{
    "sepal_length": 6.6,
    "sepal_width": 3.0,
    "petal_length": 4.4,
    "petal_width": 1.4
}
```

Clase 2 (Virginica):

```json
{
    "sepal_length": 5.9,
    "sepal_width": 3,
    "petal_length": 5.1,
    "petal_width": 1.8
}
```