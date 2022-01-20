class Venda:

    def __init__(self, dataVenda, cliente, qntdVenda):
        self.dataVenda = dataVenda
        self.qntdVenda = qntdVenda
        self.cliente = cliente

    def vender(self, produto, qntdVenda):
        if produto.verificarEstoqueInsuficiente(qntdVenda) == False:
            produto.debitarEstoque(qntdVenda)
            print(f"O preco da compra foi: {produto.precoUnit * qntdVenda}")
            return True


