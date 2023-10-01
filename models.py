''' Definimos el modelo del negocio (logica) '''
# Modelo

''' Importamos las librerias del proyecto '''
from pydantic import BaseModel


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
        self.cowsDB = []

    ''' Funciones '''
    # Retornamos el listado de todas nuestras vacas
    def get_cows(self):
        return self.cowsDB

    # Agregamos una nueva vaca a la lista
    def add_cow(self, cow: Cow):
        self.cowsDB.append(cow)