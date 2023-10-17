--exec EliminarReceta @ID=1
CREATE PROCEDURE EliminarReceta
	@ID INT
AS
BEGIN
	DELETE FROM Recetas WHERE ID= @ID
END;
