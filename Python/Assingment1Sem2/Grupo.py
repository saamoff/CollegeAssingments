class Grupo:

    def __init__(self, grupo):
        self.grupo = grupo
        self.presidente = None

    def getGrupo(self):
        return self.grupo

    def setGrupo(self, grupo):
        self.grupo = grupo

    def setPresidente(self, presidente):
        self.presidente = presidente

    def getPresidente(self):
        return self.presidente

    def getDescricaoEscolaridadePresidente(self):
        if self.presidente == None:
            return "Grupo sem presidente."
        else:
            return self.presidente.getDescricaoEscolaridade()