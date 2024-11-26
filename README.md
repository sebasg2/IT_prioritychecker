# IT Incident Priority Checker

## Project Description

This project is a web application that allows users to check the priority of IT incidents through automatic classification into three levels: low, medium, and high. The application uses the Microsoft Phi-3-mini-4k-instruct language model hosted on Hugging Face to analyze incident descriptions and determine their priority. The results were previously stored in an AWS-hosted MySQL database. **However, the AWS database is currently down, and the application is no longer operational.**
<br>

![It_priority_checker](https://github.com/user-attachments/assets/20a7f18d-11b7-460f-88fb-6ea49b3834de)

## Features

1. **Priority Classification**: The application classifies IT incidents into three priority levels (low, medium, high) based on the provided description.
2. **Database Storage**: The classification results, including user ID, incident description, date, and priority, were stored in an AWS-hosted MySQL database. (Currently unavailable due to the AWS database being down.)
3. **Web Interface**: A user-friendly web interface where users could input the incident description and receive the classified priority. (No longer operational.)

## Technologies Used

- **FastAPI**: Framework to build the web API.
- **Hugging Face Inference API**: To access the Microsoft Phi-3-mini-4k-instruct language model.
- **pymysql**: For interaction with the MySQL database.
- **AWS RDS**: Cloud-hosted MySQL database service (currently unavailable).
- **HTML/CSS**: For the web interface.

## Requirements

- Python 3.8 or later
- FastAPI
- pymysql
- Hugging Face Inference Client
- An AWS-hosted MySQL database (Currently unavailable)

## Installation

1. **Clone the repository**:
git clone https://github.com/yourusername/it-priority-checker.git cd it-priority-checker



2. **Install dependencies**:
pip install -r requirements.txt


3. **Configure environment variables**: 
Set the following environment variables in a `.env` file:
- `DB_HOST`: MySQL database host
- `DB_USER`: MySQL username
- `DB_PASSWORD`: MySQL password
- `DB_NAME`: MySQL database name
- `HF_API_KEY`: Hugging Face API key

4. **Run the application**:
uvicorn main:app --reload



5. **Access the application**: 
Open your browser and go to `http://127.0.0.1:8000`.

## Docker

The application is also available as a Docker image. To use it, follow these steps:

1. **Pull the Docker image**:
docker pull sebasgu/app_itpriority


2. **Run the Docker container**:
docker run -p 8000:8000 --env-file .env sebasgu/app_itpriority



3. **Access the application**: 
Open your browser and go to `http://127.0.0.1:8000`.

## DockerHub Link
[DockerHub Repository](https://hub.docker.com/repository/docker/sebasgu/app_itpriority/general)

---

# Verificador de Prioridad de Incidentes de TI

## Descripción del Proyecto

Este proyecto es una aplicación web que permite a los usuarios verificar la prioridad de incidentes de TI mediante una clasificación automática en tres niveles: bajo, medio y alto. La aplicación utiliza el modelo de lenguaje Phi-3-mini-4k-instruct de Microsoft, alojado en Hugging Face, para analizar las descripciones de los incidentes y determinar su prioridad. Los resultados se almacenaban en una base de datos MySQL alojada en AWS. **Sin embargo, la base de datos de AWS actualmente no está disponible, por lo que la aplicación ya no funciona.**

## Funcionalidades

1. **Clasificación de Prioridad**: La aplicación clasificaba los incidentes de TI en tres niveles de prioridad (bajo, medio, alto) basándose en la descripción proporcionada.
2. **Almacenamiento en Base de Datos**: Los resultados de la clasificación, que incluían el ID del usuario, la descripción del incidente, la fecha y la prioridad, se almacenaban en una base de datos MySQL alojada en AWS. (Actualmente no disponible.)
3. **Interfaz Web**: Una interfaz web amigable donde los usuarios podían ingresar la descripción del incidente y obtener la prioridad clasificada. (Ya no operativo.)

## Tecnologías Utilizadas

- **FastAPI**: Framework para construir la API web.
- **Hugging Face Inference API**: Para acceder al modelo de lenguaje Phi-3-mini-4k-instruct de Microsoft.
- **pymysql**: Para la interacción con la base de datos MySQL.
- **AWS RDS**: Servicio de base de datos MySQL alojada en la nube (actualmente no disponible).
- **HTML/CSS**: Para la interfaz web.

## Requisitos

- Python 3.8 o superior
- FastAPI
- pymysql
- Hugging Face Inference Client
- Una base de datos MySQL alojada en AWS (Actualmente no disponible)

## Instalación

1. **Clona el repositorio**:
git clone https://github.com/tuusuario/it-priority-checker.git cd it-priority-checker


2. **Instala las dependencias**:
pip install -r requirements.txt



3. **Configura las variables de entorno**: 
Crea un archivo `.env` con las siguientes variables:
- `DB_HOST`: Host de la base de datos MySQL
- `DB_USER`: Usuario de MySQL
- `DB_PASSWORD`: Contraseña de MySQL
- `DB_NAME`: Nombre de la base de datos MySQL
- `HF_API_KEY`: Clave API de Hugging Face

4. **Ejecuta la aplicación**:
uvicorn main:app --reload



5. **Accede a la aplicación**: 
Abre tu navegador y ve a `http://127.0.0.1:8000`.

## Docker

La aplicación también está disponible como una imagen de Docker. Para usarla, sigue estos pasos:

1. **Descarga la imagen de Docker**:
docker pull sebasgu/app_itpriority



2. **Ejecuta el contenedor de Docker**:
docker run -p 8000:8000 --env-file .env sebasgu/app_itpriority


3. **Accede a la aplicación**: 
Abre tu navegador y ve a `http://127.0.0.1:8000`.










