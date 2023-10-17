from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from DAL.Services.IngredienteService import IngredienteService
from DAL.Models.ResponseModel import ResponseModel
from DAL.Models.IngredienteModel import IngredienteModel

IngredienteController = APIRouter()
responseModel=ResponseModel()
IngredienteService= IngredienteService()

class IngredienteJsonModel(BaseModel):
    ID : int
    Nombre : str
    Existencias : int
    UnidadMedidaCantidad : str
    
    def mapearIngredienteJsonModel(self):
            ingredienteModel = IngredienteModel()
            ingredienteModel.ID = self.ID
            ingredienteModel.Nombre = self.Nombre
            ingredienteModel.Existencias = self.Existencias
            ingredienteModel.UnidadMedidaCantidad = self.UnidadMedidaCantidad
            return ingredienteModel

#http://127.0.0.1:8000/docs
@IngredienteController.get("/ConsultarIngrediente")
def ConsultarIngrediente(IdIngrediente:int):
    return IngredienteService.consultarIngrediente(IdIngrediente)

@IngredienteController.get("/ConsultarIngredientePorNombre")
def ConsultarIngredientePorNombre(Nombre:str):
    return IngredienteService.consultarIngredientePorNombre(Nombre)

@IngredienteController.get("/EliminarIngrediente")
def EliminarIngrediente(IdIngrediente:int):
    return IngredienteService.eliminarIngrediente(IdIngrediente)

@IngredienteController.post("/RegistrarIngrediente")
def RegistrarIngrediente(IngredienteJson:IngredienteJsonModel):
    return IngredienteService.registrarIngrediente(IngredienteJson.mapearIngredienteJsonModel())

@IngredienteController.post("/ModificarIngrediente")
def ModificarIngrediente(IngredienteJson:IngredienteJsonModel):
    return IngredienteService.modificarIngrediente(IngredienteJson.mapearIngredienteJsonModel())

#@IngredienteController.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}