--exec ModificarIlustracion @ID=1
CREATE PROCEDURE ModificarIlustracion
	@ID INT,
	@Nombre VarCHAR(4),
	@IdPlato INT,
	@Direccion VarCHAR(100)
AS
BEGIN
	UPDATE Ilustraciones
	SET 
	Nombre = @Nombre,
	IdPlato = @IdPlato,
	Direccion = @Direccion
	WHERE ID= @ID
END;
