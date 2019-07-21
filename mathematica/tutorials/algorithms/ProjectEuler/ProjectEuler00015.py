if __name__ == '__main__':
    import csv

    with open("D:\\Mathematica Files 4K\\fermibotAlgorithms\\ProjectEuler00015.txt", 'w') as textFile:
        maximum = 9
        paths = [[[1, 1]]]
        fullPaths = []
        while any(path[-1] != [maximum, maximum] for path in paths):
            tempFullPaths = []
            for path in paths:
                endPoint = path[-1]
                if endPoint == [maximum, maximum]:
                    fullPaths.append(path)
                    paths.remove(path)
                elif endPoint != [maximum, maximum]:
                    appendList = []
                    if endPoint[0] < maximum:
                        appendList.append([endPoint[0] + 1, endPoint[1]])
                    if endPoint[1] < maximum:
                        appendList.append([endPoint[0], endPoint[1] + 1])
                    for appendPoint in appendList:
                        tempFullPaths.append(path + [appendPoint])
                paths = tempFullPaths
            fullPaths += tempFullPaths

        for path in fullPaths:
            textFile.write(str(path).replace('[', '{').replace(']', '}'))
            textFile.write('\n')
