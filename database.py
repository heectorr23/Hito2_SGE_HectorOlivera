import pymysql

class Database:
    def __init__(self):
        self.conn = pymysql.connect(
            host="localhost",
            user="root",
            password="curso",
            database="ENCUESTAS"
        )
        self.cursor = self.conn.cursor()

    def add_record(self, age, sex, consumption, beer, weekend_drinks, distilled_drinks, wine, control_loss, alcohol_dependence, digestive_issues, high_tension, headache):
        query = "INSERT INTO ENCUESTA (edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(query, (age, sex, consumption, beer, weekend_drinks, distilled_drinks, wine, control_loss, alcohol_dependence, digestive_issues, high_tension, headache))
        self.conn.commit()

    def update_record(self, id, age, sex, consumption, beer, weekend_drinks, distilled_drinks, wine, control_loss, alcohol_dependence, digestive_issues, high_tension, headache):
        query = "UPDATE ENCUESTA SET edad=%s, Sexo=%s, BebidasSemana=%s, CervezasSemana=%s, BebidasFinSemana=%s, BebidasDestiladasSemana=%s, VinosSemana=%s, PerdidasControl=%s, DiversionDependenciaAlcohol=%s, ProblemasDigestivos=%s, TensionAlta=%s, DolorCabeza=%s WHERE idEncuesta=%s"
        self.cursor.execute(query, (age, sex, consumption, beer, weekend_drinks, distilled_drinks, wine, control_loss, alcohol_dependence, digestive_issues, high_tension, headache, id))
        self.conn.commit()

    def delete_record(self, id):
        query = "DELETE FROM ENCUESTA WHERE idEncuesta=%s"
        self.cursor.execute(query, (id,))
        self.conn.commit()

    def fetch_records(self, order_by="idEncuesta"):
        query = f"SELECT idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza FROM ENCUESTA ORDER BY {order_by}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def export_to_excel(self):
        query = "SELECT * FROM ENCUESTA"
        self.cursor.execute(query)
        return self.cursor.fetchall()