from DAL.DBConnection.ConnectionSQLServer import connectionSQLServer
from DAL.Models.IlustracionModel import IlustracionModel
from DAL.Models.ResponseModel import ResponseModel


class ResponseIlustracionModel(ResponseModel):
    def sinError(self,datos,Mensaje):
        super().sinError(Mensaje)
        self.datos=datos
        

class IlustracionProvider(connectionSQLServer):
    responseIlustracionModel = ResponseIlustracionModel()
    
    
    def consultarIlustracion(self,IDIlustracion):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarIlustracion @ID="+str(IDIlustracion)+";")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearIlustracion(filas)
                self.responseIlustracionModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIlustracionModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIlustracionModel.conError("Ha ocurrido un error al consultar la Ilustracion: "+e.args[0])
        return self.responseIlustracionModel
        
    def consultarIlustracionPorPlato(self,IDPlato):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarilustracionesPorPlato @IdPlato="+str(IDPlato)+";")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearIlustracion(filas)
                self.responseIlustracionModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIlustracionModel.conError(ResponseDBModel.Mensaje)
        except Exception as e:
            self.responseIlustracionModel.conError("Ha ocurrido un error al consultar la Ilustracion por plato: "+e.args[0])
        return self.responseIlustracionModel

    def eliminarIlustracion(self,IdIlustracion):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filasAfectadas=self.ejecutarConsultaAfectacion("exec EliminarIlustracion @ID="+str(IdIlustracion)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se han eliminado las "+str(filasAfectadas)+" ilustraciones que coincidian con el id proporcionado"
                else:
                    MensajeSalida = "no se han encontrado ilustraciones que coincidan con el id proporcionado"
                self.responseIlustracionModel.sinError("",MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIlustracionModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIlustracionModel.conError("Ha ocurrido un error al eliminar la Ilustracion: "+e.args[0])
        return self.responseIlustracionModel
      
    def registrarIlustracion(self,Ilustracion):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec RegistrarIlustracion "+
                        	"@Nombre ='"+Ilustracion.Nombre+"'"+
                            ",@IdPlato ="+str(Ilustracion.IdPlato)+
                            ",@Direccion ='"+Ilustracion.Direccion+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarIlustracion @ID="+str(IdIlustracion)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha registrado correctamente la Ilustracion"
                else:
                    MensajeSalida = "no se ha podido registrar la Ilustracion"
                self.responseIlustracionModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIlustracionModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIlustracionModel.conError("Ha ocurrido un error al registrar la Ilustracion: "+e.args[0])
        return self.responseIlustracionModel
    
    def modificarIlustracion(self,Ilustracion):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec ModificarIlustracion "+
                            "@ID = "+str(Ilustracion.ID)+
                        	",@Nombre ='"+Ilustracion.Nombre+"'"+
                            ",@IdPlato ="+str(Ilustracion.IdPlato)+
                            ",@Direccion ='"+Ilustracion.Direccion+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarIlustracion @ID="+str(IdIlustracion)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha modificado correctamente la Ilustracion"
                else:
                    MensajeSalida = "no se ha podido registrar la Ilustracion"
                self.responseIlustracionModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responseIlustracionModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responseIlustracionModel.conError("Ha ocurrido un error al modificar la Ilustracion: "+e.args[0])
        return self.responseIlustracionModel

    def mapearIlustracion(self,ilustraciones):
        response = []
        for fila in ilustraciones:
            Ilustracion = IlustracionModel()
            IlustracionFraccionada=str(fila).replace("(", "").replace(")", "").split(",")
            Ilustracion.ID = int(IlustracionFraccionada[0])
            Ilustracion.Nombre = IlustracionFraccionada[1]
            Ilustracion.IdPlato = int(IlustracionFraccionada[2])
            Ilustracion.Direccion = IlustracionFraccionada[3]
            response.append(Ilustracion)
        return response
