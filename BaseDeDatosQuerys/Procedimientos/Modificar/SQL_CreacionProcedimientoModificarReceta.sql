--exec ModificarReceta @ID=1
CREATE PROCEDURE ModificarReceta
	@ID INT,
	@IdPlato INT,
	@IdIngrediente INT,
	@Cantidad INT,
	@UnidadMedidaCantidad varchar(4)
AS
BEGIN
	UPDATE Recetas
	SET 
	IdPlato = @IdPlato,
	IdIngrediente = @IdIngrediente,
	Cantidad = @Cantidad,
	UnidadMedidaCantidad = @UnidadMedidaCantidad
	WHERE ID= @ID
END;
