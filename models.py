import db
from sqlalchemy import Column, Integer, String, Boolean

"""
Creamos una clase llamada Tarea Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servirá luego
para la base de datos) Esta clase va a almacenar toda la información referente a una tarea
"""
class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True)  # Identificador único de cada tarea (no puede haber dos tareas con el mismo id, por eso es primary key)
    contenido = Column(String(20), nullable=False)  # Contenido de la tarea, un texto de máximo 200 caracteres hecha
    hecha = Column(Boolean)  # Booleano que indica si una tarea ha sido hecha o no
    categoria = Column(Integer(), nullable=False)
    data_fecha = Column(String(10))

    def __init__(self, contenido, hecha, categoria, data_fecha):
        # Recordemos que el id no es necesario crearlo manualmente, lo añade la base de datos automaticamente
        self.contenido = contenido
        self.hecha = hecha
        self.categoria = categoria
        self.data_fecha = data_fecha

    def __repr__(self):
        return "Tarea {}: {} ({}) ({}) ({})".format(
            self.id,
            self.contenido,
            self.hecha,
            self.categoria,
            self.data_fecha
        )

    def __str__(self):
        return "Tarea {}: {} ({}) ({}) ({})".format(
            self.id,
            self.contenido,
            self.hecha,
            self.categoria,
            self.data_fecha
        )
