--exec ModificarIngrediente @ID=1
CREATE PROCEDURE ModificarIngrediente
	@ID INT,
	@Nombre VarCHAR(50),
	@Existencias INT,
	@UnidadMedidaCantidad varchar(4)
AS
BEGIN
	UPDATE Ingredientes
	SET 
	Nombre = @Nombre,
	Existencias = @Existencias,
	UnidadMedidaCantidad = @UnidadMedidaCantidad
	WHERE ID= @ID
END;
