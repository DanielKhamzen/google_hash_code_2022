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
    









def parseur(filename) :
    file = open(filename, "r")
    line = file.readline()
    line = line[:-1]
    entete = line.split(" ")
    contribs = []
    for i in range(int(entete[0])) :
        line = file.readline()
        line = line[:-1]
        contib_info = line.split(" ")
        contrib = Contributeur(contrib_info[0])
        for j in range(int(contrib_info[1])) :
            line = file.readline()
            line = line[:-1]
            skill_info = line.split(" ")
            skill = Skill(skill_info[0], skill_info[1])
            contrib.addSkill(skill)
            
            # caca
            
            
    cars = []
    for i in range(int(entete[3])) :
        line = file.readline()
        line = line[:-1]
        cars.append(line.split(" "))
    donnees = Data(entete, rues, cars)
    return(donnees)