from DAL.DBConnection.ConnectionSQLServer import connectionSQLServer
from DAL.Models.IngredienteModel import IngredienteModel
from DAL.Models.ResponseModel import ResponseModel


class ResponseIngredienteModel(ResponseModel):
    def sinError(self,datos,Mensaje):
        super().sinError(Mensaje)
        self.datos=datos
        

class IngredienteProvider(connectionSQLServer):
    responseIngredienteModel = ResponseIngredienteModel()
    
    
    def consultarIngrediente(self,IDIngrediente):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarIngrediente @ID="+str(IDIngrediente)+";")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearIngrediente(filas)
                self.responseIngredienteModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIngredienteModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIngredienteModel.conError("Ha ocurrido un error al consultar el ingrediente: "+e.args[0])
        return self.responseIngredienteModel
        
    def consultarIngredientePorNombre(self,Nombre):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarIngredientePorNombre @Nombre='%"+str(Nombre)+"%';")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearIngrediente(filas)
                self.responseIngredienteModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIngredienteModel.conError(ResponseDBModel.Mensaje)
        except Exception as e:
            self.responseIngredienteModel.conError("Ha ocurrido un error al consultar el ingrediente por plato: "+e.args[0])
        return self.responseIngredienteModel

    def eliminarIngrediente(self,IdIngrediente):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filasAfectadas=self.ejecutarConsultaAfectacion("exec EliminarIngrediente @ID="+str(IdIngrediente)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se han eliminado las "+str(filasAfectadas)+" Ingredientes que coincidian con el id proporcionado"
                else:
                    MensajeSalida = "no se han encontrado Ingredientes que coincidan con el id proporcionado"
                self.responseIngredienteModel.sinError("",MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIngredienteModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIngredienteModel.conError("Ha ocurrido un error al eliminar el ingrediente: "+e.args[0])
        return self.responseIngredienteModel
      
    def registrarIngrediente(self,Ingrediente):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec RegistrarIngrediente "+
                        	"@Nombre = '"+str(Ingrediente.Nombre)+"'"+
                            ",@Existencias ="+str(Ingrediente.Existencias)+
                            ",@UnidadMedidaCantidad ='"+Ingrediente.UnidadMedidaCantidad+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarIngrediente @ID="+str(IdIngrediente)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha registrado correctamente el ingrediente"
                else:
                    MensajeSalida = "no se ha podido registrar el ingrediente"
                self.responseIngredienteModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIngredienteModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIngredienteModel.conError("Ha ocurrido un error al registrar el ingrediente: "+e.args[0])
        return self.responseIngredienteModel
    
    def modificarIngrediente(self,Ingrediente):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec ModificarIngrediente "+
                            "@ID = "+str(Ingrediente.ID)+
                        	",@Nombre = '"+str(Ingrediente.Nombre)+"'"+
                            ",@Existencias ="+str(Ingrediente.Existencias)+
                            ",@UnidadMedidaCantidad ='"+Ingrediente.UnidadMedidaCantidad+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarIngrediente @ID="+str(IdIngrediente)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha modificado correctamente el ingrediente"
                else:
                    MensajeSalida = "no se ha podido registrar el ingrediente"
                self.responseIngredienteModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIngredienteModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIngredienteModel.conError("Ha ocurrido un error al modificar el ingrediente: "+e.args[0])
        return self.responseIngredienteModel

    def mapearIngrediente(self,Ingredientes):
        response = []
        for fila in Ingredientes:
            Ingrediente = IngredienteModel()
            IngredienteFraccionado=str(fila).replace("(", "").replace(")", "").split(",")
            Ingrediente.ID = int(IngredienteFraccionado[0])
            Ingrediente.Nombre = IngredienteFraccionado[1]
            Ingrediente.Existencias = int(IngredienteFraccionado[2])
            Ingrediente.UnidadMedidaCantidad = IngredienteFraccionado[3]
            response.append(Ingrediente)
        return response
