--exec RegistrarPlato @ID=1
CREATE PROCEDURE RegistrarPlato
	@Nombre VarCHAR(50),
	@Preparacion VarChar(300)
AS
BEGIN
	INSERT INTO Platos(Nombre,Preparacion)
	VALUES( 
	@Nombre,
	@Preparacion
	)
END;
