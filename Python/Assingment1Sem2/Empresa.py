class Empresa:

    def __init__(self, diretor):
        self.diretor = diretor

    def getDiretor(self):
        return self.diretor

    def setDiretor(self, diretor):
        self.diretor = diretor

    def getNomeDiretor(self):
        if self.diretor == None:
            return "Empresa sem diretor."
        else:
            return self.diretor.getNome()