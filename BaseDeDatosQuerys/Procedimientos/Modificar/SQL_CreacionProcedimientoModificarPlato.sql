--exec ModificarPlato @ID=1
CREATE PROCEDURE ModificarPlato
	@ID INT,
	@Nombre VarCHAR(50),
	@Preparacion VarChar(300)
AS
BEGIN
	UPDATE Platos
	SET 
	Nombre = @Nombre,
	Preparacion = @Preparacion
	WHERE ID= @ID
END;
