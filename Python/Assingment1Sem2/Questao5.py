## Qual o nome do diretor da Empresa de uma Filial

from trabalho1.Diretor import Diretor
from trabalho1.Empresa import Empresa
from trabalho1.Filial import Filial

diretor = Diretor("James")
empresa = Empresa("Feel Good Inc")
filial = Filial("Filial 1")

empresa.setDiretor(diretor)

print()
print(empresa.getNomeDiretor())