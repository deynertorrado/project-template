''' Definimos las rutas del proyecto '''
# Controlador


''' Importamos las librerías del proyecto '''
from fastapi import APIRouter
from model.models import Cow, CowManager, User, UserManager


''' Código del programa '''
# Definimos nuestro nuevo router
router = APIRouter()
# Creamos una instancia de la clase CowManager
cow_manager = CowManager()
# Creamos una instancia de la clase UserManager
user_manager = UserManager()


''' EndPoints '''
# Verificamos el acceso a la WebApp
@router.post("/login")
async def login_user(user: User):
    return user_manager.verify_user(user)

# Creamos una nueva vaca
@router.post("/cows")
async def create_cow(cow: Cow):
    cow_manager.add_cow(cow)
    return {"Message": "The cow has been created"}

# Obtenemos todos los datos de las vacas
@router.get("/cows")
async def get_info_cows():
    return cow_manager.get_cows()