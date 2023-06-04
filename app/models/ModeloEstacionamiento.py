from .entities.Dueno import Dueno
from .entities.Estacionamiento import Estacionamiento


class ModeloEstacionamiento():

    @classmethod
    def listar_estacionamientos(self, db):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT EST.llave, EST.nombre, EST.barrio, EST.precio,
                DUE.apellidos, DUE.nombres, DUE.ciudad
                FROM estacionamiento EST JOIN dueno DUE ON EST.dueno_id = DUE.id 
                ORDER BY EST.nombre ASC"""
            cursor.execute(sql)
            data = cursor.fetchall()
            estacionamientos = []
            for row in data:
                due = Dueno(0, row[4], row[5], row[6])
                est = Estacionamiento(row[0], row[1], due, row[2], row[3])
                estacionamientos.append(est)
            return estacionamientos
        except Exception as ex:
            raise Exception(ex)
