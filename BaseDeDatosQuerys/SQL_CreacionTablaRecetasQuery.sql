--DROP TABLE RECETAS
--INSERT INTO Recetas(IdPlato,IdIngrediente,Cantidad,UnidadMedidaCantidad) VALUES(,,,)
CREATE TABLE Recetas(
ID INT IDENTITY(1,1) PRIMARY KEY,
IdPlato INT,
IdIngrediente INT,
Cantidad INT,
UnidadMedidaCantidad varchar(4),
Foreign KEY (IdPlato) REFERENCES PLATOS(ID),
Foreign KEY (IdIngrediente) REFERENCES INGREDIENTES(ID)
)



