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
    parseurs = parseur("a.txt")
    contributeurs = parseurs[0]
    projects = parseurs[1]
    skills = parseurs[2]
    for project in projects :
        assignUsersToProjects(project, contributeurs, skills)
    writeData("out.a", projects)
    return 0


def assignUsersToProjects(project, contributeurs, skillList):
    print_list(skillList)
    roles = project.getRoles()
    for i in range(len(roles)):
        role = roles[i]
        for skill in skillList:
            if skill.name == role.name:
                contribs = skill.getContribs()
                for contrib in contribs:
                    if (contrib.isDisponible() and contrib.getSkill(skill.name)):
                        project.addContrib(contrib, i)
    return 0


def print_list(list):
    for i in list:
        print(i.name)
    print("\n")

main()
