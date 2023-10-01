''' Definimos las rutas del proyecto '''
# Controlador

''' Importamos las librerías del proyecto '''
from fastapi import APIRouter
from models import Cow, CowManager


''' Código del programa '''
# Definimos nuestro nuevo router
router = APIRouter()
# Creamos una instancia de la clase CowManager
cow_manager = CowManager()


''' EndPoints '''
# Obtenemos todas las vacas
@router.get("/")
def get_info():
    cow_manager.get_cows()

# Creamos una nueva vaca
@router.post("/")
def post_info(cow: Cow):
    cow_manager.add_cow(cow)
    return { "Message": "The cow has been created" }