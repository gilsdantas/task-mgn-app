from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

# En app se encuentra nuestro servidor web de Flask
app = Flask(__name__)


@app.route('/')  # route for the initial page
def home():
    todas_las_tareas = db.session.query(Tarea).all()  # Consultamos y almacenamos todas las tareas de la base de datos

    # Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas.
    # Vamos a entregar esta variable al template index.html
    return render_template("index.html", lista_de_tareas=todas_las_tareas)


@app.route('/crear-tarea', methods=['POST'])  # route for creating a task
def crear():
    # tarea es un objeto de la clase Tarea (una instancia de la clase)
    # id no es necesario asignarlo manualmente, porque la primary key se genera automáticamente
    categorias = {
        0: "Sin categoria",
        1: "Educación",
        2: "Salud",
        3: "Compras",
        4: "Otros",
    }
    tarea = Tarea(
        contenido=request.form['contenido_tarea'],
        categoria=categorias[int(request.form['categoria_tarea'])],
        data_fecha=request.form['data_fecha_tarea'],
        hecha=False
    )
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home'))  # Esto nos redirecciona a la función home()


@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    # Se busca dentro de la base de datos, aquel registro cuyo id coincida con el aportado por el parametro de la ruta.
    # Cuando se encuentra se elimina
    tarea = db.session.query(Tarea).filter_by(id=int(id)).delete()

    # Ejecutar la operación pendiente de la base de datos
    db.session.commit()

    # Esto nos redirecciona a la función home() y si todo ha ido bien, al refrescar,
    # la tarea eliminada ya no aparecera en el  listado
    return redirect(url_for('home'))


@app.route('/tarea-hecha/<id>')
def hecha(id):
    # Se obtiene la tarea que se busca
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()

    # Guardamos en la variable booleana de la tarea, su contrario
    tarea.hecha = not tarea.hecha

    # Ejecutar la operación pendiente de la base de datos return redirect(url_for('home')) # Esto nos redirecciona a
    # la función home()
    db.session.commit()

    # Esto nos redirecciona a la función home() y si todo ha ido bien, al refrescar, la tarea eliminada ya no
    # aparecera en el  listado
    return redirect(url_for('home'))


if __name__ == '__main__':
    # Creamos el modelo de datos
    db.Base.metadata.create_all(db.engine)

    # El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos código,
    # el servidor de Flask se reinicie solo
    app.run(debug=True)
