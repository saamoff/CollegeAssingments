## Qual o Pais de alocacao de um Funcionario?

from trabalho1.Pais import Pais
from trabalho1.Funcionario import Funcionario

pais = Pais("Cazaquistao")
funcionario = Funcionario("Roberto")

funcionario.setAlocacao(pais)

print()
print(funcionario.getAlocacaoFuncionario())