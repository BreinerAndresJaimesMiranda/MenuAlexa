--exec ConsultarPlatoPorNombre @ID=1
CREATE PROCEDURE ConsultarPlatoPorNombre
	@Nombre VarCHAR(50)
AS
BEGIN
	SELECT * FROM Platos WHERE Nombre LIKE @Nombre
END;