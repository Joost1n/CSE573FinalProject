import csv

def main():
    
    # readFirstFile()

    # readSecondFile()

    # readLastFile()

    cleanUp()


def readFirstFile():
    lastFileName = 'data/race_tw_2023-05-01_2023-05-14.csv'
    lastCSVFile = open(lastFileName)
    allRows = csv.reader(lastCSVFile, delimiter=',')
    lastFileOutput = open("clean_race_tw_01.txt", "w")
    
    counter = 0
    linePLease = 0
    map3 = []

    for row in allRows:
        print(linePLease)
        if linePLease == 2161356 or linePLease == 2161357 or linePLease == 3831989 or linePLease == 3831990 or linePLease == 3831991 or linePLease == 3831992 or \
            linePLease == 4057246 or linePLease == 4057247 or linePLease == 4160924 or linePLease == 4160925 or linePLease == 5950078 or linePLease == 5950079 or linePLease == 5950080:
            print(row)
            linePLease += 1
            continue
            

        if row[3] == "retweet":
            map3.append([row[6], row[8]])
            lastFileOutput.write(",".join(map3[counter]))
            lastFileOutput.write("\n")
            counter += 1
        linePLease += 1
        # if counter == 10:
        #     break
    # print(str(map3))

    lastFileOutput.close()
    lastCSVFile.close()

def readSecondFile():
    lastFileName = 'data/race_tw_2023-05-15_2023-05-23.csv'
    lastCSVFile = open(lastFileName)
    allRows = csv.reader(lastCSVFile, delimiter=',')
    lastFileOutput = open("clean_race_tw_15.txt", "w")
    
    counter = 0
    linePLease = 0
    map3 = []

    for row in allRows:
        print(linePLease)
        # if linePLease == 1237942:
        #     print(row)

        if row[3] == "retweet":
            map3.append([row[6], row[8]])
            lastFileOutput.write(",".join(map3[counter]))
            lastFileOutput.write("\n")
            counter += 1
        linePLease += 1
        # if counter == 10:
        #     break
    # print(str(map3))

    lastFileOutput.close()
    lastCSVFile.close()

def readLastFile():
    lastFileName = 'data/race_tw_2023-05-24_2023-05-31.csv'
    lastCSVFile = open(lastFileName)
    allRows = csv.reader(lastCSVFile, delimiter=',')
    lastFileOutput = open("clean_race_tw_24.txt", "w")
    
    counter = 0
    linePLease = 0
    map3 = []

    for row in allRows:
        print(linePLease)
        if linePLease == 1237942:
            print(row)

        if row[3] == "retweet":
            map3.append([row[6], row[8]])
            lastFileOutput.write(",".join(map3[counter]))
            lastFileOutput.write("\n")
            counter += 1
        linePLease += 1
        # if counter == 10:
        #     break
    # print(str(map3))

    lastFileOutput.close()
    lastCSVFile.close()

def cleanUp():

    count = 0

    with open("clean_race_tw_24.txt", "r") as f:
        lines = f.readlines()
    with open("clean_race_tw_24_clean.txt", "w") as f:
        for line in lines:
            # print(line[len(line)-2])
            if line[len(line)-2] != ',':
                f.write(line)
            count += 1


def readFile():
    
    fileName1 = "clean_race_tw_01.txt"
    fileToRead1 = open(fileName1)

    fileName2 = "clean_race_tw_15.txt"
    fileToRead2 = open(fileName2)

    fileName3 = "clean_race_tw_24.txt"
    fileToRead3 = open(fileName3)

    edges = []
    
    for line in fileToRead1:
        u,p = [int(x) for x in line.split(",")]
        edges.append((u,p))

    for line in fileToRead2:
        u,p = [int(x) for x in line.split(",")]
        edges.append((u,p))

    for line in fileToRead3:
        u,p = [int(x) for x in line.split(",")]
        edges.append((u,p))



main()
