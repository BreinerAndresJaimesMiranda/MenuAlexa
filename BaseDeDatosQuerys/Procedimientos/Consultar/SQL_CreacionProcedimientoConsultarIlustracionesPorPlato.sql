--exec ConsultarIlustracionesPorPlato @IdPlato=1
CREATE PROCEDURE ConsultarIlustracionesPorPlato
	@IdPlato INT
AS
BEGIN
	SELECT * FROM Ilustraciones WHERE IdPlato= @IdPlato
END;