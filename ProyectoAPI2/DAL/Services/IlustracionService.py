
from DAL.Providers.IlustracionProvider import IlustracionProvider,ResponseIlustracionModel

class IlustracionService:
    
    IlustracionProvider = IlustracionProvider()
    responseIlustracionModel = ResponseIlustracionModel()
    def consultarIlustracion(self,IDIlustracion):
        try:
            responseIlustracionModel=self.IlustracionProvider.consultarIlustracion(IDIlustracion)
        except Exception as e:
            responseIlustracionModel.conError("Ha ocurrido un error al consultar la Ilustracion: " + e.args[0])
        return responseIlustracionModel
        
    def consultarIlustracionPorPlato(self,IDPlato):
        try:
            responseIlustracionModel=self.IlustracionProvider.consultarIlustracionPorPlato(IDPlato)
        except Exception as e:
            responseIlustracionModel.conError("Ha ocurrido un error al consultar las Ilustraciones del plato seleccionado: " + e.args[0])
        return responseIlustracionModel

    def eliminarIlustracion(self,IdIlustracion):
        try:
            responseIlustracionModel=self.IlustracionProvider.eliminarIlustracion(IdIlustracion)
        except Exception as e:
                responseIlustracionModel.conError("Ha ocurrido un error al eliminar la Ilustracion: " + e.args[0])
        return responseIlustracionModel
    
    def registrarIlustracion(self,Ilustracion):
        try:
            responseIlustracionModel=self.IlustracionProvider.registrarIlustracion(Ilustracion)
        except Exception as e:
            responseIlustracionModel.conError("Ha ocurrido un error al registrar la Ilustracion: " + e.args[0])
        return responseIlustracionModel
    
    def modificarIlustracion(self,Ilustracion):
        try:
            responseIlustracionModel=self.IlustracionProvider.modificarIlustracion(Ilustracion)
        except Exception as e:
            responseIlustracionModel.conError("Ha ocurrido un error al modificar la Ilustracion: " + e.args[0])
        return responseIlustracionModel