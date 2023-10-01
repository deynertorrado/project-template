''' Definimos el punto de entrada del proyecto '''
# Vista

''' Importamos las librerías del proyecto '''
from fastapi import FastAPI
from router import router


''' Código del programa '''
app = FastAPI()


''' EndPoints '''
# Definimos la raíz del servidor
@app.get("/")
def main_route():
    return { "Message": "This is a main route" }

# Redireccionamos todas las rutas al "router"
# En el "prefix" pasamos el argumento de "/api" para reconocer las demas rutas con ese prefijo
app.include_router(router, prefix="/api")