class Contributeur :
    
    def __init__(self, name) :
        self.name = name
        self.skills = []
    
    def addSkill(self, skill) :
        self.skills.append(skill)
    
    def getName(self) :
        return self.name
    
    def getSkills(self) :
        return self.skills
    

class Skill :
    
    def __init__(self, name, lvl) :
        self.name = name
        self.lvl = lvl
    
    def lvlup(self) :
        self.lvl = self.lvl + 1
        
    def getName(self) :
        return self.name
    
    def getLvl(self) :
        return self.lvl
    

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
        self.contribs.append("")
    
    def getRoles(self) :
        return self.roles
    
    def getName(self) :
        return self.name
    
    def getDuration(self) :
        return self.score
    
    def getLimite(self) :
        return self.limite
    
    def getContribs(self) :
        return self.contribs
    
    def addContrib(self, contrib, index_role) :
        self.contribs[index_role] = contrib

        
    