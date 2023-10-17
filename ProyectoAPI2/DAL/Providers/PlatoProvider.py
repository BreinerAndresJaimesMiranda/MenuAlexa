from DAL.DBConnection.ConnectionSQLServer import connectionSQLServer
from DAL.Models.PlatoModel import PlatoModel
from DAL.Models.ResponseModel import ResponseModel


class ResponsePlatoModel(ResponseModel):
    def sinError(self,datos,Mensaje):
        super().sinError(Mensaje)
        self.datos=datos
        

class PlatoProvider(connectionSQLServer):
    responsePlatoModel = ResponsePlatoModel()
    
    
    def consultarPlato(self,IDPlato):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarPlato @ID="+str(IDPlato)+";")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al ID proporcionado"
                datosMapeados =self.mapearPlato(filas)
                self.responsePlatoModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responsePlatoModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responsePlatoModel.conError("Ha ocurrido un error al consultar el Plato: "+e.args[0])
        return self.responsePlatoModel
        
    def consultarPlatoPorNombre(self,Nombre):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filas=self.ejecutarConsultaBusqueda("exec ConsultarPlatoPorNombre @Nombre='%"+str(Nombre)+"%';")
                self.connectionClose()
                if len(filas) > 0:
                    MensajeSalida="Datos consultados Correctamente"
                else:
                    MensajeSalida="No hay datos asociados al nombre proporcionado"
                datosMapeados =self.mapearPlato(filas)
                self.responsePlatoModel.sinError(datosMapeados,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responsePlatoModel.conError(ResponseDBModel.Mensaje)
        except Exception as e:
            self.responsePlatoModel.conError("Ha ocurrido un error al consultar el plato por Nombre: "+e.args[0])
        return self.responsePlatoModel

    def eliminarPlato(self,IdPlato):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                filasAfectadas=self.ejecutarConsultaAfectacion("exec EliminarPlato @ID="+str(IdPlato)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se han eliminado los "+str(filasAfectadas)+" Platos que coincidian con el id proporcionado"
                else:
                    MensajeSalida = "no se han encontrado Platos que coincidan con el id proporcionado"
                self.responsePlatoModel.sinError("",MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responsePlatoModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responsePlatoModel.conError("Ha ocurrido un error al eliminar el plato: "+e.args[0])
        return self.responsePlatoModel
      
    def registrarPlato(self,Plato):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec RegistrarPlato "+
                        	"@Nombre ='"+str(Plato.Nombre)+"'"+
                            ",@Preparacion ='"+str(Plato.Preparacion)+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarPlato @ID="+str(IdPlato)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha registrado correctamente el plato"
                else:
                    MensajeSalida = "no se ha podido registrar el plato"
                self.responsePlatoModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responsePlatoModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responsePlatoModel.conError("Ha ocurrido un error al registrar el plato: "+e.args[0])
        return self.responsePlatoModel
    
    def modificarPlato(self,Plato):
        try:
            ResponseDBModel=self.connectionOpen()
            if ResponseDBModel.Error==False:
                query = ("exec ModificarPlato "+
                            "@ID = "+str(Plato.ID)+
                        	",@Nombre ='"+str(Plato.Nombre)+"'"+
                            ",@Preparacion ='"+str(Plato.Preparacion)+"';")
                filasAfectadas=self.ejecutarConsultaAfectacion(query)#"exec RegistrarPlato @ID="+str(IdPlato)+";")
                self.connectionClose()
                if filasAfectadas > 0:
                    MensajeSalida ="se ha modificado correctamente el plato"
                else:
                    MensajeSalida = "no se ha podido registrar el plato"
                self.responsePlatoModel.sinError(filasAfectadas,MensajeSalida)#ResponseDBModel.Mensaje)
            else:
                self.responsePlatoModel.conError(ResponseDBModel.Mensaje) 
        except Exception as e:
            self.responsePlatoModel.conError("Ha ocurrido un error al modificar el plato: "+e.args[0])
        return self.responsePlatoModel

    def mapearPlato(self,Platos):
        response = []
        for fila in Platos:
            Plato = PlatoModel()
            PlatoFraccionado=str(fila).replace("(", "").replace(")", "").split(",")
            Plato.ID = int(PlatoFraccionado[0])
            Plato.Nombre = PlatoFraccionado[1]
            Plato.Preparacion = PlatoFraccionado[2]
            response.append(Plato)
        return response
