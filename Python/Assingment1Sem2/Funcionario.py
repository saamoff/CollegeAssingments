from trabalho1.Pessoa import Pessoa

class Funcionario(Pessoa):

    def __init__(self, nome):
        Pessoa.__init__(self, nome)

    def setAlocacao(self, alocacao):
        self.alocacao = alocacao

    def getAlocacao(self):
        return self.alocacao

    def getAlocacaoFuncionario(self):
        if self.alocacao == None:
            return "Funcionario nao alocado."
        else:
            return self.alocacao.getPais()