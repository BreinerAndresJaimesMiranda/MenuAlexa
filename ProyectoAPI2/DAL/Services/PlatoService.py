
from DAL.Providers.PlatoProvider import PlatoProvider,ResponsePlatoModel

class PlatoService:
    
    PlatoProvider = PlatoProvider()
    responsePlatoModel = ResponsePlatoModel()
    def consultarPlato(self,IDPlato):
        try:
            responsePlatoModel=self.PlatoProvider.consultarPlato(IDPlato)
        except Exception as e:
            responsePlatoModel.conError("Ha ocurrido un error al consultar el plato: " + e.args[0])
        return responsePlatoModel
        
    def consultarPlatoPorNombre(self,Nombre):
        try:
            responsePlatoModel=self.PlatoProvider.consultarPlatoPorNombre(Nombre)
        except Exception as e:
            responsePlatoModel.conError("Ha ocurrido un error al consultar los platos con el nombre seleccionado: " + e.args[0])
        return responsePlatoModel

    def eliminarPlato(self,IdPlato):
        try:
            responsePlatoModel=self.PlatoProvider.eliminarPlato(IdPlato)
        except Exception as e:
                responsePlatoModel.conError("Ha ocurrido un error al eliminar el plato: " + e.args[0])
        return responsePlatoModel
    
    def registrarPlato(self,Plato):
        try:
            responsePlatoModel=self.PlatoProvider.registrarPlato(Plato)
        except Exception as e:
            responsePlatoModel.conError("Ha ocurrido un error al registrar el plato: " + e.args[0])
        return responsePlatoModel
    
    def modificarPlato(self,Plato):
        try:
            responsePlatoModel=self.PlatoProvider.modificarPlato(Plato)
        except Exception as e:
            responsePlatoModel.conError("Ha ocurrido un error al modificar el plato: " + e.args[0])
        return responsePlatoModel