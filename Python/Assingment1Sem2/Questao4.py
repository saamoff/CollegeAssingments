## Qual a Escolaridade do chefe de um Departamento

from trabalho1.Escolaridade import Escolaridade
from trabalho1.Chefe import Chefe
from trabalho1.Departamento import Departamento

escolaridade = Escolaridade("Pos-Graduacao")
chefe = Chefe("Marcelo")
departamento = Departamento("Grupo 1")

chefe.setEscolaridade(escolaridade)
departamento.setChefe(chefe)

print()
print(departamento.getDescricaoEscolaridadeChefe())