
from DAL.Providers.IngredienteProvider import IngredienteProvider,ResponseIngredienteModel

class IngredienteService:
    
    IngredienteProvider = IngredienteProvider()
    responseIngredienteModel = ResponseIngredienteModel()
    def consultarIngrediente(self,IDIngrediente):
        try:
            responseIngredienteModel=self.IngredienteProvider.consultarIngrediente(IDIngrediente)
        except Exception as e:
            responseIngredienteModel.conError("Ha ocurrido un error al consultar el ingrediente: " + e.args[0])
        return responseIngredienteModel
        
    def consultarIngredientePorNombre(self,Nombre):
        try:
            responseIngredienteModel=self.IngredienteProvider.consultarIngredientePorNombre(Nombre)
        except Exception as e:
            responseIngredienteModel.conError("Ha ocurrido un error al consultar los ingredientes con el nombre seleccionado: " + e.args[0])
        return responseIngredienteModel

    def eliminarIngrediente(self,IdIngrediente):
        try:
            responseIngredienteModel=self.IngredienteProvider.eliminarIngrediente(IdIngrediente)
        except Exception as e:
                responseIngredienteModel.conError("Ha ocurrido un error al eliminar el ingrediente: " + e.args[0])
        return responseIngredienteModel
    
    def registrarIngrediente(self,Ingrediente):
        try:
            responseIngredienteModel=self.IngredienteProvider.registrarIngrediente(Ingrediente)
        except Exception as e:
            responseIngredienteModel.conError("Ha ocurrido un error al registrar el ingrediente: " + e.args[0])
        return responseIngredienteModel
    
    def modificarIngrediente(self,Ingrediente):
        try:
            responseIngredienteModel=self.IngredienteProvider.modificarIngrediente(Ingrediente)
        except Exception as e:
            responseIngredienteModel.conError("Ha ocurrido un error al modificar el ingrediente: " + e.args[0])
        return responseIngredienteModel