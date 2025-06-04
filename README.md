# Weather API ☀️🌧️

Proyecto backend que proporciona información meteorológica actual basada en la ubicación de una ciudad. Esta API está diseñada para ser consumida por aplicaciones frontend como [weather-web](https://github.com/davidrguez98/weather-web), facilitando datos actualizados de forma sencilla y estructurada.

## 🧠 Descripción

Este proyecto expone una API REST que conecta con un servicio externo de datos climáticos (OpenWeather) para devolver información como temperatura, sensación térmica, humedad, descripción del clima, entre otros. Se trata de un proyecto didáctico desarrollado como parte de mi formación en desarrollo backend.

## ⚙️ Funcionalidad

- Endpoint para obtener el clima actual de una ciudad mediante su nombre.
- Middleware para manejo de errores y validación de entrada.
- Soporte para variables de entorno para proteger la clave de la API.
- Respuestas formateadas de manera clara para su uso directo en interfaces de usuario.

## 🛠️ Tecnologías usadas

- **Node.js** como entorno de ejecución.
- **Express** para la creación de la API.
- **Axios** para la realización de peticiones HTTP.
- **dotenv** para gestión de variables de entorno.
- **Cors** para permitir peticiones desde frontend.

## 📁 Estructura del proyecto

```
Weather-API/
│
├── controllers/         # Lógica de negocio y procesamiento de datos
├── routes/              # Definición de endpoints
├── utils/               # Funciones auxiliares (formateo, validaciones)
├── .env.example         # Ejemplo de variables de entorno necesarias
├── index.js             # Punto de entrada de la aplicación
├── package.json         # Dependencias y scripts
└── README.md            # Información del proyecto
```

## 🚀 Instalación y puesta en marcha

1. Clona el repositorio:
   ```
   git clone https://github.com/davidrguez98/Weather-API.git
   cd Weather-API
   ```

2. Instala las dependencias:
   ```
   npm install
   ```

3. Crea un archivo `.env` en la raíz del proyecto y añade tu clave de la API de OpenWeather. Puedes usar el archivo `.env.example` como referencia:
   ```
   API_KEY=tu_clave_de_openweather
   ```

4. Inicia el servidor:
   ```
   node index.js
   ```

   El servidor se iniciará en `http://localhost:3000` (o el puerto que hayas configurado).

## 🤝 Contacto

Si quieres ponerte en contacto conmigo:

- [LinkedIn](https://www.linkedin.com/in/davidrguez98/)
- Correo: ropeda98@gmail.com
