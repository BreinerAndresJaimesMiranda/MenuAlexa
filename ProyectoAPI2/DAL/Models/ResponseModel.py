class ResponseModel():
    Error = True
    Mensaje = ""
    
    def conError(self,Mensaje):
        self.Error = True
        self.Mensaje = Mensaje
    
    def sinError(self,Mensaje):
        self.Error=False
        self.Mensaje = Mensaje
        
    