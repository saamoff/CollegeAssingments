from Venda import Venda

class Produto:

    def __init__(self, nome, qtndEstoque, precoUnit, estoqueMin, estoqueMax):
        self.nome = nome
        self.qntdEstoque = qtndEstoque
        self.precoUnit = precoUnit
        self.estoqueMin = estoqueMin
        self.estoqueMax = estoqueMax
        self.historico = []

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setQntdEstoque(self, qntdEstoque):
        self.qntdEstoque = qntdEstoque

    def getQntdEstoque(self):
        return self.qntdEstoque

    def setPrecoUnit(self, precoUnit):
        self.precoUnit = precoUnit

    def getPrecoUnit(self):
        return self.precoUnit

    def setEstoqueMax(self, estoqueMax):
        self.estoqueMax = estoqueMax

    def getEstoqueMax(self):
        return self.estoqueMax

    def setEstoqueMin(self, estoqueMin):
        self.estoqueMin = estoqueMin

    def getEstoqueMin(self):
        return self.estoqueMin

    def debitarEstoque(self, qntdEstoque):
        self.qntdEstoque = self.qntdEstoque - qntdEstoque

    def creditarEstoque(self, qntdEstoque):
        self.qntdEstoque = self.qntdEstoque + qntdEstoque

    def verificarEstoqueBaixo(self, qntdEstoque):
        if qntdEstoque <= self.estoqueMin:
            print("Estoque Baixo.")
        else:
            return False

    def verificarEstoqueInsuficiente(self, qntdEstoque):
        if qntdEstoque < self.estoqueMin:
            print("Estoque Insuficiente.")
        else:
            return False

    def verificarEstoqueExcedente(self, qntdEstoque):
        if qntdEstoque + self.estoqueMax > self.estoqueMax:
            print("Estoque Excedente.")
        else:
            return False

    def vender(self, dataVenda, cliente, qntdVenda):
        venda = Venda(dataVenda, cliente, qntdVenda)
        if venda.vender(self, qntdVenda) == True:
            self.registrarHistorico(venda)

    def registrarHistorico(self, evento):
        self.historico.append(evento)

    def exibirHistorico(self):
        for historico in self.historico:
            print(historico)