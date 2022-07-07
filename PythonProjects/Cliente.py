from Persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, dni, telefono, tipo):
        super().__init__(nombre, apellido, dni, telefono)
        self.tipo =tipo

