--exec RegistrarIngrediente @ID=1
CREATE PROCEDURE RegistrarIngrediente
	@Nombre VarCHAR(50),
	@Existencias INT,
	@UnidadMedidaCantidad varchar(4)
AS
BEGIN
	INSERT INTO Ingredientes(Nombre,Existencias,UnidadMedidaCantidad)
	VALUES( 
	@Nombre,
	@Existencias,
	@UnidadMedidaCantidad
	)
END;
