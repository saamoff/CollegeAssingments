class Departamento:

    def __init__(self, departamento):
        self.departamento = departamento
        self.chefe = None

    def getDepartamento(self):
        return self.departamento

    def setDepartamento(self, departamento):
        self.departamento = departamento

    def setChefe(self, chefe):
        self.chefe = chefe

    def getChefe(self):
        return self.chefe

    def getDescricaoEscolaridadeChefe(self):
        if self.chefe == None:
            return "Departamento sem chefe."
        else:
            return self.chefe.getDescricaoEscolaridade()