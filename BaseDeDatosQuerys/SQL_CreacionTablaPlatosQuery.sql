--DROP TABLE PLATOS
--INSERT INTO Platos(Nombre,Preparacion) VALUES(,)
CREATE TABLE Platos(
ID INT IDENTITY(1,1) PRIMARY KEY,
Nombre VarCHAR(50),
Preparacion VarChar(300)
)