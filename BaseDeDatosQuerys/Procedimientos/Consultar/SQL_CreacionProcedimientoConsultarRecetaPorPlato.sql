--exec ConsultarRecetasPorPlato @IdPlato=1
CREATE PROCEDURE ConsultarRecetasPorPlato
	@IdPlato INT
AS
BEGIN
	SELECT * FROM Recetas WHERE IdPlato= @IdPlato
END;
