from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
import re
import uvicorn
import json
from huggingface_hub import InferenceClient
from langchain_core.prompts import PromptTemplate
import pymysql
from datetime import datetime
from fastapi.responses import FileResponse

app = FastAPI()

# Define el ID del repositorio y el token de Hugging Face
repo_id = "microsoft/Phi-3-mini-4k-instruct"
hf_token = "hftoken"  # Reemplazar con tu token real de Hugging Face

# Inicializa el InferenceClient con el token de Hugging Face
llm_client = InferenceClient(
    model=repo_id,
    token=hf_token,
    timeout=120,
)

def call_llm(inference_client: InferenceClient, prompt: str):
    # Realiza la solicitud a la API de Hugging Face
    response = inference_client.post(
        json={
            "inputs": prompt,
            "parameters": {"max_new_tokens": 200},
            "task": "text-generation",
        },
    )
    # Decodifica y devuelve el texto generado
    return json.loads(response.decode())[0]["generated_text"]

def insert_into_db(user_id: int, prompt: str, priority_value: str):
    # Configuración de la conexión a la base de datos
    username = "admin"
    password = "sg1515eg"
    host = "database-2.cbm2c84euy0d.eu-north-1.rds.amazonaws.com"
    port = 3306
    database = "it_prioritydb"

    try:
        db = pymysql.connect(
            host=host,
            user=username,
            password=password,
            port=port,
            cursorclass=pymysql.cursors.DictCursor
        )
        cursor = db.cursor()

        # Usa la base de datos específica
        cursor.execute(f"USE {database}")

        # Obtén la fecha actual
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Define los datos a insertar
        data_to_insert = {
            'user_id': user_id,
            'date': current_date,
            'incident': prompt,
            'priority': priority_value
        }

        # Inserta los datos en la tabla incident
        insert_data_query = '''
        INSERT INTO incident (user_id, date, incident, priority)
        VALUES (%(user_id)s, %(date)s, %(incident)s, %(priority)s)
        '''
        cursor.execute(insert_data_query, data_to_insert)
        db.commit()
        print("Datos insertados con éxito.")

        # Recupera y muestra los datos de la tabla incident
        cursor.execute('SELECT * FROM incident')
        records = cursor.fetchall()
        for record in records:
            print(record)

    except pymysql.MySQLError as e:
        raise HTTPException(status_code=500, detail=f"Error de base de datos: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'db' in locals() and db:
            db.close()

@app.get("/")
async def pagina():
    return FileResponse("index.html")

@app.get("/priority")
async def priority(prompt: str, user_id: int = 1):
    # Define la plantilla del prompt
    template = PromptTemplate(
        input_variables=["text"],
        template="classify this priority for an IT incident. You must classify it in one word, the three options you have are low, medium, and high priorities. Here is how you should format your answer, priority= 'your answer'. The situation is: {text}"
    )
    formatted_prompt = template.format(text=prompt)
    response = call_llm(llm_client, formatted_prompt)
    
    # Extrae la prioridad usando split
    parts = response.split("priority=")
    if len(parts) >= 3:
        priority_value = parts[2].split()[0].replace("'", "")  # Obtén la primera palabra después de la segunda 'priority=' y elimina las comillas
    else:
        raise HTTPException(status_code=400, detail="Segunda instancia de prioridad no encontrada en la respuesta")
    
    insert_into_db(user_id, prompt, priority_value)

    return {"priority": priority_value}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8888)
    




