## Qual a escolaridade do Presidente de um Grupo?

from trabalho1.Escolaridade import Escolaridade
from trabalho1.Presidente import Presidente
from trabalho1.Grupo import Grupo


escolaridade = Escolaridade("Mestrado")
presidente = Presidente("Marcelo")
grupo = Grupo("Grupo 1")

presidente.setEscolaridade(escolaridade)
grupo.setPresidente(presidente)

print()
print(grupo.getDescricaoEscolaridadePresidente())