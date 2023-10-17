--exec ConsultarIngredientePorNombre @ID=1
CREATE PROCEDURE ConsultarIngredientePorNombre
	@Nombre VarCHAR(50)
AS
BEGIN
	SELECT * FROM Ingredientes WHERE Nombre LIKE @Nombre
END;
