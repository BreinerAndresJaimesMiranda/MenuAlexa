--exec RegistrarReceta @ID=1
CREATE PROCEDURE RegistrarReceta
	@IdPlato INT,
	@IdIngrediente INT,
	@Cantidad INT,
	@UnidadMedidaCantidad varchar(4)
AS
BEGIN
	INSERT INTO Recetas(IdPlato,IdIngrediente,Cantidad,UnidadMedidaCantidad)
	VALUES( 
	@IdPlato,
	@IdIngrediente,
	@Cantidad,
	@UnidadMedidaCantidad
	)
END;
