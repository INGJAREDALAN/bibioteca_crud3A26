class Usuario:

    # Constructor 
    def __init__(self, id, nombre, matricula, correo, carrera):
        self.id= id
        self.nombre = nombre
        self.matricula = matricula
        self.correo = correo
        self.carrera = carrera
        self.activo = True

    def activo(self):
        self.activo = True

    def desactivar(self):
        self.activo = False

    def mostar_info(self):
        return f"Usuario ID: {self.id}, Nombre: {self.nombre}, Matricula: {self.matricula}, Email: {self.correo}, Carrera: {self.carrera}, Activo: {'Si' if self.activo else 'No'}"
