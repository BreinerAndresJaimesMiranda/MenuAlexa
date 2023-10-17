--exec RegistrarIlustracion @ID=1
CREATE PROCEDURE RegistrarIlustracion
	@Nombre VarCHAR(4),
	@IdPlato INT,
	@Direccion VarCHAR(100)
AS
BEGIN
	INSERT INTO Ilustraciones(Nombre,IdPlato,Direccion)
	VALUES( 
	@Nombre,
	@IdPlato,
	@Direccion
	)
END;
