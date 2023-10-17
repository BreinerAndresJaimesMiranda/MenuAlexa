
from DAL.Providers.RecetaProvider import RecetaProvider,ResponseRecetaModel

class RecetaService:
    
    recetaProvider = RecetaProvider()
    responseRecetaModel = ResponseRecetaModel()
    def consultarReceta(self,IDReceta):
        try:
            responseRecetaModel=self.recetaProvider.consultarReceta(IDReceta)
        except Exception as e:
            responseRecetaModel.conError("Ha ocurrido un error al consultar la receta: " + e.args[0])
        return responseRecetaModel
        
    def consultarRecetaPorPlato(self,IDPlato):
        try:
            responseRecetaModel=self.recetaProvider.consultarRecetaPorPlato(IDPlato)
        except Exception as e:
            responseRecetaModel.conError("Ha ocurrido un error al consultar las recetas del plato seleccionado: " + e.args[0])
        return responseRecetaModel

    def eliminarReceta(self,IdReceta):
        try:
            responseRecetaModel=self.recetaProvider.eliminarReceta(IdReceta)
        except Exception as e:
                responseRecetaModel.conError("Ha ocurrido un error al eliminar la receta: " + e.args[0])
        return responseRecetaModel
    
    def registrarReceta(self,receta):
        try:
            responseRecetaModel=self.recetaProvider.registrarReceta(receta)
        except Exception as e:
            responseRecetaModel.conError("Ha ocurrido un error al registrar la receta: " + e.args[0])
        return responseRecetaModel
    
    def modificarReceta(self,receta):
        try:
            responseRecetaModel=self.recetaProvider.modificarReceta(receta)
        except Exception as e:
            responseRecetaModel.conError("Ha ocurrido un error al modificar la receta: " + e.args[0])
        return responseRecetaModel