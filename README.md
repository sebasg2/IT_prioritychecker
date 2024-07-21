# IT_prioritychecker

# IT Incident Priority Checker

## Descripción del Proyecto

Este proyecto es una aplicación web que permite a los usuarios verificar la prioridad de incidentes de TI mediante una clasificación automática en tres niveles: bajo (low), medio (medium) y alto (high). La aplicación utiliza un modelo de lenguaje de Microsoft Phi-3-mini-4k-instruct, alojado en Hugging Face, para analizar las descripciones de los incidentes y determinar su prioridad. Los resultados se almacenan en una base de datos MySQL alojada en AWS.

## Funcionalidades

1. **Clasificación de Prioridad**: La aplicación clasifica los incidentes de TI en tres niveles de prioridad (low, medium, high) basándose en la descripción proporcionada.
2. **Almacenamiento en Base de Datos**: Los resultados de la clasificación se almacenan en una base de datos MySQL en AWS, incluyendo detalles como el ID del usuario, el incidente en si, la fecha y la prioridad del incidente.
3. **Interfaz Web**: Una interfaz web donde los usuarios pueden ingresar la descripción del incidente y obtener la prioridad clasificada.

## Tecnologías Utilizadas

- **FastAPI**: Framework web para crear la API.
- **Hugging Face Inference API**: Para acceder al modelo de lenguaje Phi-3-mini-4k-instruct de Microsoft.
- **pymysql**: Para interactuar con la base de datos MySQL.
- **AWS RDS**: Servicio de base de datos en la nube donde se aloja la base de datos MySQL.
- **HTML/CSS**: Para la interfaz web.

## Requisitos

- Python 3.8 o superior
- FastAPI
- pymysql
- Hugging Face Inference Client
- Una base de datos MySQL alojada en AWS

## Instalación

1. **Clona el repositorio**:
   ```sh
   git clone https://github.com/tuusuario/it-priority-checker.git
   cd it-priority-checker

  2. **Link al dockerhub**
     https://hub.docker.com/repository/docker/sebasgu/app_itpriority/general
