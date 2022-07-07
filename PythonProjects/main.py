from Empleado import Empleado
from Cliente import Cliente

#emp = Empleado('Lucas', 'Moy', '123123', '231424323', 1000)
#cli = Cliente('Jorge', 'Castro', '456456', '321235432', 'vip')

def cargar():
    respuesta = input('Cargara un empleado?: ')
    nombre = input('Ingrese el nombre: ')
    apellido = input('Ingrese el apellido: ')
    dni = input('Ingrese el dni: ')
    telefono = input('Ingrese el telefono: ')

    if (respuesta == 'si'):
        salario = input('Ingrese el salario: ')
        emp = Empleado(nombre, apellido, dni, telefono, int(salario))
        personas.append(emp)
    else:
        tipo = input('Ingrese el tipo de cliente: ')
        cli = Cliente(nombre, apellido, dni, telefono, tipo)
        personas.append(cli)

personas = []
cargar()