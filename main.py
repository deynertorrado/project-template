''' Definimos el punto de entrada del proyecto '''
# Vista


''' Importamos las librerías del proyecto '''
from fastapi import FastAPI
from router import router
from fastapi.middleware.cors import CORSMiddleware
import dotenv
import os


''' Código del programa '''
app = FastAPI()
# Cargamos la variable de entorno del archivo .env
dotenv.load_dotenv()
# Obtenemos el valor de la variable "ACCESS_HOST"
access_host = os.getenv("ACCESS_HOST")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Esto restringe el acceso a algunas direcciones
    allow_credentials=True,
    allow_methods=["*"],  # Esto permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Esto permite todos los encabezados
)

''' EndPoints '''
# Definimos la raíz del servidor
@app.get("/")
def main_route():
    return { "Message": "This is a main route" }

# Redireccionamos todas las rutas al "router"
# En el "prefix" pasamos el argumento de "/api" para reconocer las demas rutas con ese prefijo
app.include_router(router, prefix="/api")