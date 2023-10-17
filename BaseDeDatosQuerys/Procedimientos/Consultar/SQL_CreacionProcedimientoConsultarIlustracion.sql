--exec ConsultarIlustracion @ID=1
CREATE PROCEDURE ConsultarIlustracion
	@ID INT
AS
BEGIN
	SELECT * FROM Ilustraciones WHERE ID= @ID
END;