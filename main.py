from parseur import parseur
from objects import Contributeur, Skill, Projet
from writer import writeData

def main():
    ## j'ai un liste de contributeurs
    ## chaque contributeur à n skills de i niveau
    ## une liste de projets
    ## chaque projet à x job/skills de k niveau (requis)
    # 
    # algo:
    # récuperer la liste entière des roles et l'id du projet qui est lié
    # rolesList = liste des roles
    # pour chaque j in rolesList
    #   find user (u) where u.skills.contains(j) and where u.available == true
    #   project.contributeurs.add(user)
    #
    parseurs = parseur("f.txt")
    contributeurs = parseurs[0]
    projects = parseurs[1]
    skills = parseurs[2]
    print(len(contributeurs), len(projects), len(skills))
    temps = 0
    projects_done = []
    while len(projects)!=0 :
        for project in projects :
            if(project.getLimite()-temps+project.getScore()<=0) :
                projects.remove(project)
                continue
            res = assignUsersToProjects(project, contributeurs, skills, temps)    
            if(res == 0) :
                projects.remove(project)
                projects_done.append(project)
            if(res == 1) :
                for i in range(len(project.contribs)) :
                    if(project.contribs[i] != None) :
                        project.contribs[i].setDisponible()
                        project.contribs[i] = None
            if(res == 2) :
                projects.remove(project)
        temps += 100
                    
                
    writeData("out.f", projects_done)
    return 0


def assignUsersToProjects(project, contributeurs, skillList, temps):
    roles = project.getRoles()
    for i in range(len(roles)):
        role = roles[i]
        k = 0
        while k<len(skillList) :
            skill = skillList[k]
            if skill.name == role.name:
                contribs = skill.getContribs()
                j = 0
                while j<len(contribs) :
                    contrib = contribs[j]
                    if (contrib.isDisponible(temps) and contrib.getSkill(role)):
                        project.addContrib(contrib, i)
                        contrib.setIndisponible(temps + project.duration)
                        break
                    j+=1
                if(j==len(contribs)) :
                    return 1
                break
            k+=1
        if(k==len(skillList)):
            return 2
        
    return 0


def print_list(list):
    for i in list:
        print(i.name)
    print("\n")

main()
