--DROP TABLE ILUSTRACIONES
--INSERT INTO Ilustraciones(Nombre,IdPlato,Direccion) VALUES(,,)
CREATE TABLE Ilustraciones(
ID INT IDENTITY(1,1) PRIMARY KEY,
Nombre Varchar (4),
IdPlato INT,
Direccion VarCHAR(100),
Foreign KEY (IdPlato) REFERENCES PLATOS(ID)
)