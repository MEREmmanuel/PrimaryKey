class Dueno():
    def __init__(self, id, apellidos, nombres, ciudad):
        self.id = id
        self.apellidos = apellidos
        self.nombres = nombres
        self.ciudad = ciudad

    def nombre_completo(self):
        return "{0}, {1}".format(self.apellidos, self.nombres)
