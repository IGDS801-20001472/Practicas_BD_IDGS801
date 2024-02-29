from flask import Flask, render_template, request
import forms
from flask import flash
from flask_wtf.csrf import CSRFProtect
from wtforms import validators
from flask import g
from config import DevelopmentConfig

from models import db
from models import Empleados

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




@app.route("/")
def nose():
    return render_template("layout.html")



@app.route("/Empleados", methods = ['GET', 'POST'])
def index():
    create_form = forms.UserFormEmp(request.form)
    emp = ''
    if request.method == 'POST':
        emp = Empleados(nombre = create_form.nombre.data, 
                       direccion = create_form.direccion.data, 
                       email = create_form.email.data,
                       telefono = create_form.telefono.data,
                       sueldo = create_form.sueldo.data)
        #insert alumnos() values()
        db.session.add(emp)
        db.session.commit()


        emp = Empleados.query.all()
        print(emp)
    return render_template("Empleados.html", form = create_form, Empleados = emp)









if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()