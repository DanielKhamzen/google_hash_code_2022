def parseur(filename) :
    file = open(filename, "r")
    line = file.readline()
    line = line[:-1]
    entete = line.split(" ")
    rues = []
    for i in range(int(entete[2])) :
        line = file.readline()
        line = line[:-1]
        rues.append(line.split(" "))
    cars = []
    for i in range(int(entete[3])) :
        line = file.readline()
        line = line[:-1]
        cars.append(line.split(" "))
    donnees = Data(entete, rues, cars)
    return(donnees)