from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Empleados(db.Model):
    _tablename_='empleados'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    email = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    sueldo = db.Column(db.Double)

class Pedidos(db.Model):
    _tablename_='pedidos'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    direccion = db.Column(db.String(50))
    telefono = db.Column(db.Integer)
    ingredientes = db.Column(db.String(40))
    numPizzas = db.Column(db.Integer)
    tamanio = db.Column(db.String(20))
    total = db.Column(db.Integer)
    fecha = db.Column(db.Date)
    diaN = db.Column(db.String(20))

