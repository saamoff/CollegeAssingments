## Qual o Estado da Filial que um Funcionario coordena?

from trabalho1.Estado import Estado
from trabalho1.Filial import Filial
from trabalho1.Funcionario import Funcionario

estado = Estado("Parana")
filial = Filial("Exemplo")
funcionario = Funcionario("Joao")

filial.setLocalizacao(estado)

print()
print(filial.getLocalizacaoFilial())