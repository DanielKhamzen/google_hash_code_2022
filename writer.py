def writeData(nameInputFile, listProject):
    with open(nameInputFile+'.txt', 'w+') as f:
        f.write(str(len(listProject)) + '\n')
        for project in listProject:
            f.write(project.name + '\n' + ("".join([project.contribs[i].name + ' ' for i in range(len(project.contribs))]) + "\n"))
