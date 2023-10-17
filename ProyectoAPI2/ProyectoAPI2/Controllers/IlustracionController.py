from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from DAL.Services.IlustracionService import IlustracionService
from DAL.Models.ResponseModel import ResponseModel
from DAL.Models.IlustracionModel import IlustracionModel

IlustracionController = APIRouter()
responseModel=ResponseModel()
IlustracionService= IlustracionService()

class IlustracionJsonModel(BaseModel):
    ID : int
    Nombre : str
    IdPlato : int
    Direccion : str
    
    def mapearIlustracionJsonModel(self):
            ilustracionModel = IlustracionModel()
            ilustracionModel.ID = self.ID
            ilustracionModel.Nombre = self.Nombre
            ilustracionModel.IdPlato = self.IdPlato
            ilustracionModel.Direccion = self.Direccion
            return ilustracionModel

#http://127.0.0.1:8000/docs
@IlustracionController.get("/ConsultarIlustracion")
def ConsultarIlustracion(IdIlustracion:int):
    return IlustracionService.consultarIlustracion(IdIlustracion)

@IlustracionController.get("/ConsultarIlustracionPorPlato")
def ConsultarIlustracionPorPlato(IdPlato:int):
    return IlustracionService.consultarIlustracionPorPlato(IdPlato)

@IlustracionController.get("/EliminarIlustracion")
def EliminarIlustracion(IdIlustracion:int):
    return IlustracionService.eliminarIlustracion(IdIlustracion)

@IlustracionController.post("/RegistrarIlustracion")
def RegistrarIlustracion(IlustracionJson:IlustracionJsonModel):
    return IlustracionService.registrarIlustracion(IlustracionJson.mapearIlustracionJsonModel())

@IlustracionController.post("/ModificarIlustracion")
def ModificarIlustracion(IlustracionJson:IlustracionJsonModel):
    return IlustracionService.modificarIlustracion(IlustracionJson.mapearIlustracionJsonModel())

#@IlustracionController.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}