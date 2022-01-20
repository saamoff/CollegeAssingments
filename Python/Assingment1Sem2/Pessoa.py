class Pessoa:

    def __init__(self, nome):
        self.nome = nome
        self.escolaridade = None

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setEscolaridade(self, escolaridade):
        self.escolaridade = escolaridade

    def getEscolaridade(self):
        return self.escolaridade

    def getDescricaoEscolaridade(self):
        if self.escolaridade == None:
            return "Pessoa sem escolaridade"
        else:
            return self.escolaridade.getDescricao()