from objects import Contributeur, Skill, Projet, Skill_global, Skills_globaux

"""
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
"""







def parseur(filename) :
    file = open(filename, "r")
    line = file.readline()
    line = line[:-1]
    entete = line.split(" ")
    contribs = []
    skills_globaux = Skills_globaux()
    for i in range(int(entete[0])) :
        line = file.readline()
        line = line[:-1]
        contrib_info = line.split(" ")
        contrib = Contributeur(contrib_info[0])
        for j in range(int(contrib_info[1])) :
            line = file.readline()
            line = line[:-1]
            skill_info = line.split(" ")
            skill = Skill(skill_info[0], skill_info[1])
            contrib.addSkill(skill)
            skill_global = Skill_global(skill_info[0])
            skill_global = skills_globaux.addSkill(skill_global)
            skill_global.addContrib(contrib)
            
            
        contribs.append(contrib)
            
    projets = []
    for i in range(int(entete[1])) :
        line = file.readline()
        line = line[:-1]
        projet_info = line.split(" ")
        projet = Projet(projet_info[0], projet_info[1], projet_info[2], projet_info[3])
        for j in range(int(projet_info[4])) :
            line = file.readline()
            line = line[:-1]
            skill_info = line.split(" ")
            skill = Skill(skill_info[0], skill_info[1])
            projet.addRole(skill)
        projets.append(projet)
    return((contribs, projets, skills_globaux.getSkills_globaux()))