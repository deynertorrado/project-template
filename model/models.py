''' Definimos el modelo del negocio (logica) '''
# Modelo


''' Importamos las librerias del proyecto '''
from datetime import datetime, timedelta
from pydantic import BaseModel
from model.database import dbMethods
import jwt
import os
import dotenv


''' Código del programa '''
# Cargamos las variables de entorno del archivo .env
dotenv.load_dotenv()
# Obtenemos el valor de las variables en entorno
secret_key = os.getenv("SECRET_KEY")
algorithm = os.getenv("ALGORITHM")
token_expire = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

# Inicializamos "db_methods"
db_manager = dbMethods()

''' Funciones '''
# Definimos nuestro acceso con JWT
def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm=algorithm)
    return encoded_jwt


''' Clases '''
# Definimos nuestro modelo de "Vaca"
class Cow(BaseModel):
    id: int
    name: str
    breed: str
    weight: float
    birth: str
    age: int

# Definimos nuestra clase y metodos para interactuar con la DB
class CowManager:
    # Definimos una lista para simular una DB
    def __init__(self):
        self.cows_db = []

    ''' Métodos '''
    # Retornamos el listado de todas nuestras vacas
    def get_cows(self):
        return self.cows_db

    # Agregamos una nueva vaca a la lista
    def add_cow(self, cow: Cow):
        self.cows_db.append(cow)

# Definimos nuestro modelo de usuario
class User(BaseModel):
    username: str
    password: str

# Definimos nuestra clase y metodos para interactuar con la DB
class UserManager:
    def __init__(self):
        self.user_db = [
            {
                "username": "ryan01",
                "password": "1234"
            }
        ]

    ''' Métodos '''
    # Verificamos el usuario en la DB y le asignamos su JWT
    def verify_user(self, user: User):
            if db_manager.verify_user_db(user):
                access_token_expires = timedelta(minutes=token_expire)
                access_token = create_access_token(
                    data={"sub": user.username}, expires_delta=access_token_expires
                )
                return {"access_token": access_token, "token_type": "bearer"}
            return {"message": "the user does not exist in the database"}