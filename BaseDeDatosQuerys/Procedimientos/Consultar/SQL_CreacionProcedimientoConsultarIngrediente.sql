--exec ConsultarIngrediente @ID=1
CREATE PROCEDURE ConsultarIngrediente
	@ID INT
AS
BEGIN
	SELECT * FROM Ingredientes WHERE ID= @ID
END;

