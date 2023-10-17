from fastapi import FastAPI
from ProyectoAPI2.Controllers.RecetaController import RecetaController
from ProyectoAPI2.Controllers.IngredienteController import IngredienteController
from ProyectoAPI2.Controllers.IlustracionController import IlustracionController
from ProyectoAPI2.Controllers.PlatoController import PlatoController


app = FastAPI()

app.include_router(RecetaController, prefix="/RecetaController", tags=["RecetaController"])
app.include_router(IngredienteController, prefix="/IngredienteController", tags=["IngredienteController"])
app.include_router(IlustracionController, prefix="/IlustracionController", tags=["IlustracionController"])
app.include_router(PlatoController, prefix="/PlatoController", tags=["PlatoController"])

