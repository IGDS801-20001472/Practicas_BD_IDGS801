from flask import Flask, render_template, request, redirect, url_for, flash
import forms, datetime
from flask import flash
from flask_wtf.csrf import CSRFProtect
from wtforms import validators
from flask import g
from config import DevelopmentConfig
from sqlalchemy import func
from models import db
from models import Empleados
from models import Pedidos


import tkinter as tk
from tkinter import messagebox




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



pedidos = []
ventasFiltradas = []
listaAnios = []



@app.route('/eliminar_pedido', methods=['POST'])
def eliminar_pedido():
    pedido_index = int(request.form.get('pedido_index')) - 1  


    if 0 <= pedido_index < len(pedidos):
        del pedidos[pedido_index]  


    return redirect('/Pedidos')





    


@app.route("/Pedidos", methods = ['GET', 'POST'])
def Pedido():
    formPizza = forms.PedidosForm(request.form)    
    if request.method == 'POST':

        dias_semana = {0: "Lunes",1: "Martes",2: "Miercoles",3: "Jueves",4: "Viernes",5: "Sabado",6: "Domingo"}

        for pedido_data in pedidos:
            fecha = datetime.date(int(pedido_data['anio']), int(pedido_data['mes']), int(pedido_data['dia']))
            diaSema = fecha.weekday()
            nDiaSema = dias_semana[diaSema]
            pedido = Pedidos(
                nombre=pedido_data['nombre'],
                direccion=pedido_data['direccion'],
                tamanio=pedido_data['tamanio'],
                telefono=pedido_data['telefono'],
                ingredientes=', '.join(pedido_data['ingredientes']),
                numPizzas=pedido_data['num_pizzas'],
                total=pedido_data['subtotal'],
                fecha=fecha,
                diaN=nDiaSema
            )
            db.session.add(pedido)
            db.session.commit()
        mensaje = 'Pedidos guardados con Exito.'
        flash(mensaje)
        pedidos.clear()
        return redirect('/Pedidos')
        

        
    # ped= Pedidos.query.all()
    # print(ped)
    tableDataV = ventasFiltradas
    totalV = 0
    print(ventasFiltradas)
    for venta in tableDataV:
        totalV += venta['total']
    
        
    print(totalV)

   

    return render_template("Pizzeria.html", form = formPizza,  pedidos=pedidos,
                            totalV = totalV, vFiltro = tableDataV)




@app.route('/agregar_pedido', methods=['POST', 'GET'])
def agregar_pedido():

    formPizza = forms.PedidosForm(request.form)

    if request.method == "POST":
        nombre = formPizza.nombre.data
        direccion = formPizza.direccion.data
        telefono = request.form.get('telefono')
        tamanio = request.form.get('tamanio')
        ingredientes = request.form.getlist('ingredientes')
        num_pizzas = request.form.get('numPizzas')
        subtotal = request.form.get('subtotal')
        if tamanio == "Chica":
            subtotal = ((len(ingredientes) * 10)+ 40)* (int(num_pizzas))
        if tamanio == "Mediana":
            subtotal = ((len(ingredientes) * 10)+ 80)* (int(num_pizzas))
        if tamanio == "Grande":
            subtotal = ((len(ingredientes) * 10)+ 120)* (int(num_pizzas))
        dia = request.form.get('dia')
        mes = request.form.get('mes')
        anio = request.form.get('anio')
        diaN = request.form.get('diaN')

        pedidos.append({'nombre': nombre, 'telefono': telefono, 'direccion': direccion,
                'tamanio': tamanio, 'ingredientes': ingredientes, 'num_pizzas': num_pizzas,
                'subtotal': subtotal, 'dia': dia, 'mes': mes, 'anio': anio, 'diaN': diaN})
    
   

        for index, pedido in enumerate(pedidos):
            print(f"Índice: {index}, Pedido: {pedido}")

    
    
        return redirect('/Pedidos')
        




@app.route('/guardar_cambios', methods=['POST', 'GET'])
def guardar_cambios():
    pedido_index = int(request.form.get('pedido_index'))
    print(f"Indice a modificar: {pedido_index}")
    if 0 <= pedido_index < len(pedidos):
        
        nombre = request.form.get('nombre')
        direccion = request.form.get('direccion')
        telefono = request.form.get('telefono')
        tamanio = request.form.get('tamanio')
        ingredientes = request.form.getlist('ingredientes')
        numPizzas =request.form.get('num_pizzas')
        dia = request.form.get('dia')
        mes = request.form.get('mes')
        anio = request.form.get('anio')
        
        
        tamanio = request.form.get('tamanio')
        ingredientes = request.form.getlist('ingredientes')
        #num_pizzas = request.form.get('numPizzas')
        print(numPizzas)
        subtotal = 0
        
        if tamanio == "Chica":
            subtotal = ((len(ingredientes) * 10) + 40) * int(numPizzas)
        elif tamanio == "Mediana":
            subtotal = ((len(ingredientes) * 10) + 80) * int(numPizzas)
        elif tamanio == "Grande":
            subtotal = ((len(ingredientes) * 10) + 120) * int(numPizzas)
        
        pedidos[pedido_index]['subtotal'] = subtotal


        pedidos[pedido_index]['nombre'] = nombre
        pedidos[pedido_index]['direccion'] = direccion
        pedidos[pedido_index]['telefono'] = telefono
        pedidos[pedido_index]['tamanio'] = tamanio
        pedidos[pedido_index]['ingredientes'] = ingredientes
        pedidos[pedido_index]['num_pizzas'] = numPizzas
        pedidos[pedido_index]['dia'] = dia
        pedidos[pedido_index]['mes'] = mes
        pedidos[pedido_index]['anio'] = anio
        pedidos[pedido_index]['diaN'] = diaN

        print(pedidos)
    
    return redirect('/Pedidos')




@app.route('/redirigir_modificar', methods=['POST', 'GET'])
def redirigir_modificar():
    pedido_index = int(request.form.get('pedido_index')) - 1  

    
    if 0 <= pedido_index < len(pedidos):
        pedido = pedidos[pedido_index]  
        
        print(pedido)
        print(pedido_index)
        return render_template('Modificar.html', pedido=pedido, pedido_index = pedido_index)

    
    return redirect(url_for('Pedido'))



@app.route('/filtro', methods=['POST', 'GET'])
def filtro():
    if request.method == 'POST':

        seleccion = request.form.get('seleccion')
        ventasFiltradas.clear()
        if seleccion == 'diaS':
            diaN = request.form.get('diaFiltro')
            ventas_filtradas = db.session.query( Pedidos.nombre,func.sum(Pedidos.total).label('total'),
                                            Pedidos.fecha,Pedidos.diaN).filter(
            Pedidos.diaN == diaN
            ).group_by(Pedidos.nombre, Pedidos.fecha).all()
            for v in ventas_filtradas:
                ventasT = {'nombre': v.nombre,
                                        'total': v.total,
                                        'diaN' : v.diaN,
                                        'fecha': v.fecha}
                ventasFiltradas.append(ventasT)
            print(f"VentaFiltro: {ventasFiltradas}")
        
        elif seleccion == 'mesS':
            mes = request.form.get('mesFiltro')
            ventas_filtradas = db.session.query(Pedidos.nombre,func.sum(Pedidos.total).label('total'),
                                            Pedidos.fecha,Pedidos.diaN).filter(
            func.month(Pedidos.fecha) == mes
            ).group_by(Pedidos.nombre, Pedidos.fecha).all() 


            for v in ventas_filtradas:
                ventasT = {'nombre': v.nombre,
                                        'total': v.total,
                                        'diaN' : v.diaN,
                                        'fecha':v.fecha}
                ventasFiltradas.append(ventasT)
            print(f"VentaFiltro: {ventasFiltradas}")
        return redirect('/Pedidos')



if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()