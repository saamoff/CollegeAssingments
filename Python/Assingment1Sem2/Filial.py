class Filial:

    def __init__(self, nome):
        self.nome = nome

    def getNomeFilial(self):
        return self.nome

    def setNomeFilial(self, nome):
        self.nome = nome

    def getLocalizacao(self):
        return self.localizacao

    def setLocalizacao(self, localizacao):
        self.localizacao = localizacao

    def getLocalizacaoFilial(self):
        if self.localizacao == None:
            return "Filial nao tem Estado."
        else:
            return self.localizacao.getEstado()

