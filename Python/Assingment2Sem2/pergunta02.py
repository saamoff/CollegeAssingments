## Remova 1 produto do estoque que foi comprado.

from Produto import Produto
from Cliente import Cliente

cliente = Cliente("Marco", "123")
produto = Produto("Caneta", 100, 1.2, 5, 150)

produto.vender("03/04/2002", cliente, 10)
