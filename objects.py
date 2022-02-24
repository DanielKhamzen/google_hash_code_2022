class Contributeur :
    
    def __init__(self, name) :
        self.name = name
        self.skills = []
    
    def addSkill(self, skill) :
        self.skills.append(skill)
    

class Skill :
    
    def __init__(self, name, lvl) :
        self.name = name
        self.lvl = lvl
    
    def lvlup(self) :
        self.lvl = self.lvl + 1
    

class Projet :
    
    def __init__(self, name, duration, score, limite) :
        self.name = name
        self.duration = duration
        self.score = score
        self.limite = limite
        self.roles = []
        self.contribs = []
    
    def addRole(self, role) :
        self.roles.append(role)
    