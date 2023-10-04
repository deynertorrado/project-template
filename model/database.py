''' Definimos las rutas del proyecto '''
# Base de Datos


''' Importamos las librerías del proyecto '''
from supabase import create_client
# from pydantic import BaseModel
from model.models import User
import dotenv
import os

''' Código del programa '''
# Cargamos las variables de entorno del archivo .env
dotenv.load_dotenv()
# Obtenemos el valor de las variables en entorno
url_spbd = os.getenv("URL_SUPABASE")
key_spbd = os.getenv("KEY_SUPABASE")
# Nos conectamos a la BD
supabase = create_client(url_spbd, key_spbd)

''' Clases '''
# Definimos nuestro modelo de usuario
# class User(BaseModel):
#     username: str
#     password: str

# Definimos nuestra clase DB
class dbMethods:
    
    # Verificamos si el usuario existe en la DB
    async def verify_user_db(self, user: User):
        response = await supabase.table('usuarios').select().eq('username', user.username).eq('password', user.password).execute()
        data = response['data']
        if not data:
            return False
        return True