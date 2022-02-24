def writeData(nameInputFile, listProject):
    with open('{nameInputFile}.txt', 'w') as f:
        for i in listProject:
            f.write('{listProject[i]}')