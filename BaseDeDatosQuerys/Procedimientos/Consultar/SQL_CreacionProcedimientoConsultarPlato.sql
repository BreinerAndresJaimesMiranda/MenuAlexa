--exec ConsultarPlato @ID=1
CREATE PROCEDURE ConsultarPlato
	@ID INT
AS
BEGIN
	SELECT * FROM Platos WHERE ID= @ID
END;