from parseur import parseur
from objects import Contributeur, Skill, Projet

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
    roles = getRoles(projects)
    assignUsersToProjects(projects, contributeurs, roles, skills)
    
    return 0


def assignUsersToProjects(projects, contributeurs, roles, skillList):
    print_list(skillList)
    for role in roles:
        for skill in skillList:
            if skill.name == role.name:
                contribs = skill.getContribs()
                for contrib in contribs:
                    if contrib.isDisponible:
                        return 0
        contributeur = role.name in contributeurs.name
        print(contributeur)
        ## trouver le premier utilisateur qui a un skill === au role.name et qui a un skillLevel === role.skillLevel
    return 0

def getRoles(projects):
    roles = []
    for project in projects:
        roles += project.getRoles()
    return roles

def print_list(list):
    for i in list:
        print(i.name)
    print("\n")

main()
