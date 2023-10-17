--exec EliminarPlato @ID=1
CREATE PROCEDURE EliminarPlato
	@ID INT
AS
BEGIN
	DELETE FROM Platos WHERE ID= @ID
END;