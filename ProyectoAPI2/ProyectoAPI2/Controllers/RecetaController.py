from typing import Union
from fastapi import APIRouter
from pydantic import BaseModel
from DAL.Services.RecetaService import RecetaService
from DAL.Models.ResponseModel import ResponseModel
from DAL.Models.RecetaModel import RecetaModel

RecetaController = APIRouter()
responseModel=ResponseModel()
recetaService= RecetaService()

class RecetaJsonModel(BaseModel):
    ID: int
    IdPlato: int
    IdIngrediente: int
    Cantidad: int
    UnidadMedidaCantidad: str
    
    def mapearRecetaJsonModel(self):
            recetaModel = RecetaModel()
            recetaModel.ID = self.ID
            recetaModel.IdPlato = self.IdPlato
            recetaModel.IdIngrediente = self.IdIngrediente
            recetaModel.Cantidad = self.Cantidad
            recetaModel.UnidadMedidaCantidad = self.UnidadMedidaCantidad
            return recetaModel

#http://127.0.0.1:8000/docs
@RecetaController.get("/ConsultarReceta")
def ConsultarReceta(IdReceta:int):
    return recetaService.consultarReceta(IdReceta)

@RecetaController.get("/ConsultarRecetaPorPlato")
def ConsultarRecetaPorPlato(IdPlato:int):
    return recetaService.consultarRecetaPorPlato(IdPlato)

@RecetaController.get("/EliminarReceta")
def EliminarReceta(IdReceta:int):
    return recetaService.eliminarReceta(IdReceta)

@RecetaController.post("/RegistrarReceta")
def RegistrarReceta(recetaJson:RecetaJsonModel):
    return recetaService.registrarReceta(recetaJson.mapearRecetaJsonModel())

@RecetaController.post("/ModificarReceta")
def ModificarReceta(recetaJson:RecetaJsonModel):
    return recetaService.modificarReceta(recetaJson.mapearRecetaJsonModel())

#@RecetaController.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}