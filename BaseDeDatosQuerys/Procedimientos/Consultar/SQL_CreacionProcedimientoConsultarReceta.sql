--exec ConsultarReceta @ID=1
CREATE PROCEDURE ConsultarReceta
	@ID INT
AS
BEGIN
	SELECT * FROM Recetas WHERE ID= @ID
END;
