--exec EliminarIlustracion @ID=1
CREATE PROCEDURE EliminarIlustracion
	@ID INT
AS
BEGIN
	DELETE FROM Ilustraciones WHERE ID= @ID
END;