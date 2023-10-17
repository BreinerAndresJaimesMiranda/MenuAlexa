from DAL.DBConnection.ConnectionSQLServer import connectionSQLServer
from DAL.Models.RecetaModel import RecetaModel
from DAL.Models.ResponseModel import ResponseModel


class ResponseRecetaModel(ResponseModel):
    def sinError(self,datos,Mensaje):
        super().sinError(Mensaje)
        self.datos=datos
        

class RecetaProvider(connectionSQLServer):
    responseRecetaModel = ResponseRecetaModel()
    
    
    def consultarReceta(self,IDReceta):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarReceta @ID="+str(IDReceta)+";")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearReceta(filas)
                self.responseRecetaModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseRecetaModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseRecetaModel.conError("Ha ocurrido un error al consultar la receta: "+e.args[0])
        return self.responseRecetaModel
        
    def consultarRecetaPorPlato(self,IDPlato):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarRecetasPorPlato @IdPlato="+str(IDPlato)+";")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearReceta(filas)
                self.responseRecetaModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseRecetaModel.conError(ResponseDBModel.Mensaje)
        except Exception as e:
            self.responseRecetaModel.conError("Ha ocurrido un error al consultar la receta por plato: "+e.args[0])
        return self.responseRecetaModel

    def eliminarReceta(self,IdReceta):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filasAfectadas=self.ejecutarConsultaAfectacion("exec EliminarReceta @ID="+str(IdReceta)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se han eliminado las "+str(filasAfectadas)+" recetas que coincidian con el id proporcionado"
                else:
                    MensajeSalida = "no se han encontrado recetas que coincidan con el id proporcionado"
                self.responseRecetaModel.sinError("",MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseRecetaModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseRecetaModel.conError("Ha ocurrido un error al eliminar la receta: "+e.args[0])
        return self.responseRecetaModel
      
    def registrarReceta(self,receta):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec RegistrarReceta "+
                        	"@IdPlato ="+str(receta.IdPlato)+
                            ",@IdIngrediente ="+str(receta.IdIngrediente)+
                            ",@Cantidad ="+str(receta.Cantidad)+
                            ",@UnidadMedidaCantidad ='"+receta.UnidadMedidaCantidad+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarReceta @ID="+str(IdReceta)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha registrado correctamente la receta"
                else:
                    MensajeSalida = "no se ha podido registrar la receta"
                self.responseRecetaModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseRecetaModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseRecetaModel.conError("Ha ocurrido un error al registrar la receta: "+e.args[0])
        return self.responseRecetaModel
    
    def modificarReceta(self,receta):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec ModificarReceta "+
                            "@ID = "+str(receta.ID)+
                        	",@IdPlato ="+str(receta.IdPlato)+
                            ",@IdIngrediente ="+str(receta.IdIngrediente)+
                            ",@Cantidad ="+str(receta.Cantidad)+
                            ",@UnidadMedidaCantidad ='"+receta.UnidadMedidaCantidad+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarReceta @ID="+str(IdReceta)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha modificado correctamente la receta"
                else:
                    MensajeSalida = "no se ha podido registrar la receta"
                self.responseRecetaModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseRecetaModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseRecetaModel.conError("Ha ocurrido un error al modificar la receta: "+e.args[0])
        return self.responseRecetaModel

    def mapearReceta(self,Recetas):
        response = []
        for fila in Recetas:
            receta = RecetaModel()
            recetaFraccionada=str(fila).replace("(", "").replace(")", "").split(",")
            receta.ID = int(recetaFraccionada[0])
            receta.IdPlato = int(recetaFraccionada[1])
            receta.IdIngrediente = int(recetaFraccionada[2])
            receta.Cantidad = int(recetaFraccionada[3])
            receta.UnidadMedidaCantidad = recetaFraccionada[4] 
            response.append(receta)
        return response
