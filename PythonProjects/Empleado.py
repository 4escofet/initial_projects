from Persona import Persona

class Empleado(Persona):
    def __init__(self,nombre, apellido, dni, telefono, salario):
        super().__init__(nombre, apellido, dni, telefono)
        self.salario = salario

