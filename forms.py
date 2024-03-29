from wtforms import validators,StringField, TelField, IntegerField, EmailField, Form, DecimalField


class UserFormEmp(Form):
    id = TelField('id', [validators.number_range(min = 1, max = 20, message = 'valor no valido')])
    nombre = StringField('nombre', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=4, max=10, message="ingresa nombre valido")
        ])
    telefono = IntegerField('telefono', [
        validators.DataRequired(message = "El campo es requerido y debe tener 10 digitos"),
        validators.length(min=10, max=10, message="ingresa Telefono valido")
        ])
    email = EmailField('email', [validators.Email(message="Ingrese un correo Valido")])
    direccion = StringField('direccion', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=4, max=50, message="ingresa direccion valida")
        ])
    sueldo = IntegerField('sueldo', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=4, max=15, message="ingresa sueldo valido")
        ])

class PedidosForm(Form):
    id = TelField('id', [validators.number_range(min = 1, max = 20, message = 'valor no valido')])
    nombre = StringField('nombre', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=4, max=30, message="ingresa nombre valido")
        ])
    direccion = StringField('direccion')
    telefono = StringField('telefono', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=10, max=10, message="ingresa Telefono valido")
        ])
    ingredientes = StringField('ingredientes')
    numPizzas = IntegerField('num Pizzas', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=1, message="ingresa Cantidad valido")
        ])
    tamanio = StringField('tamanio')
    subtotal = IntegerField('subtotal')
    dia = IntegerField('dia')
    mes = IntegerField('mes')
    anio = IntegerField('anio')

    
    