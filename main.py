from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__) # En app se encuentra nuestro servidor web de Flask


@app.route('/')  # route for the initial page
def home():
    todas_las_tareas = db.session.query(Tarea).all() #Consultamos y almacenamos todas las tareas de la base de datos
    # Ahora en la variable todas_las_tareas se tienen almacenadas todas las tareas. Vamos a entregar esta variable al template index.html
    return render_template("index.html",lista_de_tareas=todas_las_tareas)


@app.route('/crear-tarea', methods=['POST'])  # route for creating a task
def crear():
    # tarea es un objeto de la clase Tarea (una instancia de la clase)
    tarea = Tarea(contenido=request.form['contenido_tarea'], hecha=False) # id no es necesario asignarlo manualmente, porque la primary key se genera automáticamente
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for('home')) # Esto nos redirecciona a la función home()


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Creamos el modelo de datos
    app.run(debug=True) # El debug=True hace que cada vez que reiniciemos el servidor o modifiquemos código, el servidor de Flask se reinicie solo
