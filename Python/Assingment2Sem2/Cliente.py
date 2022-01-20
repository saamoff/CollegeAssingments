from Pessoa import Pessoa

class Cliente(Pessoa):

    def __init__(self, nome, cpf):
        Pessoa.__init__(self, nome)
        self.cpf = cpf

    def setCpf(self, cpf):
        self.cpf = cpf

    def getCpf(self):
        return self.cpf