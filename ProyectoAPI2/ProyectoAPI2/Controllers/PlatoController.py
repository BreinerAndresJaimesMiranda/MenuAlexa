from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from DAL.Services.PlatoService import PlatoService
from DAL.Models.ResponseModel import ResponseModel
from DAL.Models.PlatoModel import PlatoModel

PlatoController = APIRouter()
responseModel=ResponseModel()
PlatoService= PlatoService()

class PlatoJsonModel(BaseModel):
    ID: int
    Nombre: str
    Preparacion: str
    
    def mapearPlatoJsonModel(self):
            platoModel = PlatoModel()
            platoModel.ID = self.ID
            platoModel.Nombre = self.Nombre
            platoModel.Preparacion = self.Preparacion
            return platoModel

#http://127.0.0.1:8000/docs
@PlatoController.get("/ConsultarPlato")
def ConsultarPlato(IdPlato:int):
    return PlatoService.consultarPlato(IdPlato)

@PlatoController.get("/ConsultarPlatoPorNombre")
def ConsultarPlatoPorNombre(Nombre:str):
    return PlatoService.consultarPlatoPorNombre(Nombre)

@PlatoController.get("/EliminarPlato")
def EliminarPlato(IdPlato:int):
    return PlatoService.eliminarPlato(IdPlato)

@PlatoController.post("/RegistrarPlato")
def RegistrarPlato(PlatoJson:PlatoJsonModel):
    return PlatoService.registrarPlato(PlatoJson.mapearPlatoJsonModel())

@PlatoController.post("/ModificarPlato")
def ModificarPlato(PlatoJson:PlatoJsonModel):
    return PlatoService.modificarPlato(PlatoJson.mapearPlatoJsonModel())

#@PlatoController.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}