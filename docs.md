# Prueba técnica: Python Developer

## Carolina Rojas Duque - Quipux - 29 de junio de 2024

Este documento contiene una descripción corta de los pasos llevados a cabo para la solución de la prueba, así como instrucciones para su verificación.

### Sobre el modelo de clasificación

El modelo se entrenó en el archivo `model/model_generation.py`. Notando que esta parte no era la más fundamental en la prueba, no le dediqué mucho tiempo a indagar sobre el desempeño del mismo ni a intentar diferentes modelos y estrategias, sino que entrené un *RandomForest* para clasificación, que es adecuado para el número de datos y de características del dataset. Hice una partición de 80% entrenamiento y 20% prueba, obteniendo un accuracy del 100% que 