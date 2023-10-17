import pyodbc
from DAL.Models.ResponseModel import ResponseModel
class connectionSQLServer:
    
    HOST = "localhost\SQLEXPRESS"#nombre de servidor
    USER = "MenuAlexa"
    PASSWORD = "MenuAlexa"
    DATABASE = "DB_RecetarioAlexa"
    connectionString=""

    def __init__(self):
        self.connectionString = "DRIVER={ODBC Driver 18 for SQL Server};SERVER="+self.HOST+";DATABASE="+self.DATABASE+";UID="+self.USER+";PWD="+self.PASSWORD+";TrustServerCertificate=YES"

    def conexionBD(self):
        responseDBModel = ResponseDBModel()
        try:
            connection = pyodbc.connect(self.connectionString)
            responseDBModel.sinError(connection)
        except Exception as e:
            responseDBModel.sinError(e.args[0])
        return responseDBModel
        
    def connectionOpen(self):
        responseDBModel =self.conexionBD()
        if responseDBModel.Error == False:
            self.conn = responseDBModel.connection
            self.cur = self.conn.cursor()
        return responseDBModel
        
    def connectionClose(self):
        self.cur.close()
        self.conn.close()

    def ejecutarConsultaBusqueda(self,query):
        self.cur.execute(query)
        filas = self.cur.fetchall()
        self.conn.commit()
        return filas
        
    def ejecutarConsultaAfectacion(self,query):
        print(query)
        self.cur.execute(query)
        filasAfectadas =self.cur.rowcount
        self.conn.commit()
        return filasAfectadas
        
class ResponseDBModel(ResponseModel):

    def conError(self,Exception):
        super().conError("Ha ocurrido un problema al conectarse a la base de datos: "+Exception)
    
    def sinError(self,connection):
        super().sinError("Conexion exitosa con la base de datos")
        self.connection=connection
        
    