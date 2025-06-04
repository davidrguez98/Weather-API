# Weather Console App ☁️🌦️

Aplicación de consola desarrollada en Python que permite consultar la previsión meteorológica de una ciudad durante un rango de días. Se conecta a la API de Visual Crossing y devuelve un informe detallado del tiempo, incluyendo temperatura media, máximas, mínimas y probabilidad de precipitaciones.

## 🧠 Descripción

El usuario introduce una ciudad y un número de días de previsión (por ejemplo, 3 días), y el programa obtiene los datos meteorológicos reales desde la API externa. La información se muestra por consola de forma clara y estructurada, ideal como práctica de consumo de APIs, gestión de errores y estructuración de datos en Python.

## ⚙️ Funcionalidad

- Solicita al usuario una ciudad y número de días.
- Realiza una petición a la API de Visual Crossing.
- Gestiona errores comunes (ciudad no encontrada, problemas de red, etc.).
- Muestra la previsión día por día: temperatura media, máxima, mínima y precipitaciones.

## 🛠️ Tecnologías usadas

- **Python 3.10+**
- **requests** para consumir la API externa.
- **datetime** para formatear las fechas.
- **API de Visual Crossing** como fuente de datos meteorológicos.

## 📁 Estructura del proyecto

```
Weather-API/
│
├── backend/
│   └── weather_functions.py    # Lógica principal de conexión, formateo y visualización
│
├── tests/
│   └── tests.py                # Tests unitarios para funciones de backend (si aplica)
│
├── main.py                     # Punto de entrada: ejecuta el programa desde consola
├── requirements.txt            # Librerías necesarias
└── README.md                   # Documentación del proyecto
```

## 🚀 Instalación y ejecución

1. Clona el repositorio:
   ```
   git clone https://github.com/davidrguez98/Weather-API.git
   cd Weather-API
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

4. Ejecuta el programa:
   ```
   python main.py
   ```

   El programa te pedirá que escribas una ciudad y un rango de días.

## 📝 Ejemplo de uso

```
Escribe una ciudad: Madrid
Rango de días de previsión: 1

METEOROLOGY IN MADRID:
Date: 04-06-2025
Average temp.: 24.6°C
Max temp.: 28.2°C
Min temp.: 18.4°C
Precipitation probability: The probability of precipitation is 20%
...
```

## 🤝 Contacto

Si quieres ponerte en contacto conmigo:

- [LinkedIn](https://www.linkedin.com/in/davidrguez98/)
- Correo: ropeda98@gmail.com
