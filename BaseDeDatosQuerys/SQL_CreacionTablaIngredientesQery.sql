--DROP TABLE INGREDIENTES
--INSERT INTO Ingredientes(Nombre,Existencias,UnidadMedidaCantidad) VALUES(,,)
CREATE TABLE Ingredientes(
ID INT IDENTITY(1,1) PRIMARY KEY,
Nombre VarCHAR(50),
Existencias INT,
UnidadMedidaCantidad varchar(4)
)