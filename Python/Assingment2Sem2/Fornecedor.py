from trabalho02 import Pessoa

class Fornecedor(Pessoa):

    def __init__(self, nome, cnpj):
        Pessoa.__init__(self, nome)
        self.cpnj = cnpj

    def setCnpj(self, cnpj):
        self.cnpj = cnpj

    def getCnpj(self):
        return self.cnpj