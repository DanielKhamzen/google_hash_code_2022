class Contributeur :
    
    def __init__(self, name) :
        self.name = name
        self.skills = []
        self.disponible = True
    
    def addSkill(self, skill) :
        self.skills.append(skill)
    
    def getName(self) :
        return self.name
    
    def getSkills(self) :
        return self.skills
    
    def isDisponible(self) :
        return self.disponible
    
    def setIndisponible(self) :
        self.disponible = False
        
    def setDisponible(self) :
        self.disponible = True
        
    def getSkill(self, skill_name) :
        for skill in self.skills :
            if skill.getName() == skill_name :
                return skill
        
    
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

class Skill_global :
    
    def __init__(self, name):
        self.name = name
        self.contribs = []
    
    def addContrib(self, contrib) :
        self.contribs.append(contrib)
    
    def getContribs(self) :
        return self.contribs
    
    def getName(self) :
        return self.name

class Skills_globaux :
    def __init__(self):
        self.skills = []
        self.skills_names = []
    
    def addSkill(self, skill_global) :
        for i in range(len(self.skills)) :
            
            if skill_global.getName() == self.skills_names[i] :
                return self.skills[i]
            
 #       else :
        self.skills.append(skill_global)
        self.skills_names.append(skill_global.getName())
        return skill_global
            
    
    def getSkills_globaux(self) :
        return self.skills
        
    

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

        
    