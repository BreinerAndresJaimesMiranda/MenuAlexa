--exec EliminarIngrediente @ID=1
CREATE PROCEDURE EliminarIngrediente
	@ID INT
AS
BEGIN
	DELETE FROM Ingredientes WHERE ID= @ID
END;

