from pprint import pprint
import sys

if len(sys.argv) == 1:
    print('whatever is chosen answer is bad')
else:

    def findTruthTable(lengthT):
        if lengthT < 1:
            return [[]]
        return [ row + [binary] for row in findTruthTable(lengthT - 1) for binary in [0, 1]]

    tableoftruth = findTruthTable(4)
    for i in range(2,len(tableoftruth),4):
        tableoftruth[i], tableoftruth[i+1] = tableoftruth[i+1], tableoftruth[i]

    pprint("TRUTH TABLE DONT KNOW IF NEEDED")
    tableoftruth = [[tableoftruth[i], tableoftruth[i+1], tableoftruth[i+2], tableoftruth[i+3]] for i in range(0,len(tableoftruth), 4)]


    tableoftruth[2], tableoftruth[3] = tableoftruth[3], tableoftruth[2]
    pprint(tableoftruth)


    # FIRST COL is A, SECOND COL is B, THIRD COL is C, FOURTH COL is D
    def decimal_to_binary(x):
        return bin(int(x))[2:]


    listSolution = [[0, 0, 0, 0] for i in range(0, 4)]
    # print(listSolution)
    # testList = [[0] for i in range(0, 16)]

    binaryInputList = []
    sys.argv[1:len(sys.argv)] = sorted(sys.argv[1:len(sys.argv)],key=int)

    # pprint(sys.argv)
    def findBinaryList():
        for i in range(1,len(sys.argv)):
            binaryInputList.append(list(map(int,decimal_to_binary(sys.argv[i]))))
        for ba in binaryInputList:
            while len(ba) < 4:
                ba.insert(0, 0)

    findBinaryList()
    print()
    # print("THIS IS THE BINARY TABLE")
    # pprint(binaryInputList)
    print()
    # pprint(listSolution)


    # KEEP IT IN CASE YOU NEED IT
    # print(int(str(binaryInputList[0:2])))
    # def findTestList():
    #     for item in binaryInputList:
    #         x = int(str(''.join(map(str, item[2:4]))), 2)
    #         print(x)
    #         y = int(str(''.join(map(str,item[0:2]))),2)
    #         print(y)
    #         print()
    #         listSolution[x][y] = 1
    #
    # findTestList()

    def findFromTruthTable():
        for whichRow,item in enumerate(tableoftruth):
            for whichColumn,eachList in enumerate(item):
                for eachPosition in binaryInputList:
                    # print(str(''.join(map(str, eachList[2:4]))),str(''.join(map(str, eachPosition[2:4]))))
                    if str(''.join(map(str, eachList[0:2]))) == str(''.join(map(str, eachPosition[2:4]))) and str(''.join(map(str, eachList[2:4]))) == str(''.join(map(str, eachPosition[0:2]))):
                        # print(whichColumn,whichRow)
                        listSolution[whichRow][whichColumn] = 1


    findFromTruthTable()
    pprint("THIS ARRAY OF THE SOLUTIOn")
    pprint(listSolution)
    print()


    def ifInSixteen():
        isSixteen = []
        for item in listSolution:
            count = len([i for i in item if i == 1])

            if count != 4:
                return
            else:
                isSixteen.append(item)
        print(1)
        sys.exit()

    ifInSixteen()


    # for indexOfArray in range(len(array)):
    #     col.append([int(row[indexOfArray]) for row in array])

    #THIS IS THE SOLUTION
    sol = []

    testsol = []
    colifInEight = []
    rowifInEight = []
    def ifInEight(testsol):

        for indexOfArray,item in enumerate(listSolution):
            countCol = len([i for i in [int(row[indexOfArray]) for row in listSolution] if i == 1])
            # print([int(row[indexOfArray]) for row in listSolution])
            countRow = len([i for i in item if i == 1])
            if countRow == 4:
                rowifInEight.append(indexOfArray)
                # print(rowifInEight)
            if countCol == 4:
                colifInEight.append(indexOfArray)
                # print(colifInEight)

        print('lenOfCol,', len(colifInEight), 'lenofRows,', len(rowifInEight))
        if len(colifInEight) >= 2 and len(colifInEight) >= len(rowifInEight):
            pprint(colifInEight)
            sol.append(colifInEight)
            for eachCol in colifInEight:
                # print([row[eachCol] for row in tableoftruth])
                # for index in range(len([row[eachCol] for row in tableoftruth])):
                #     print([row[eachCol] for row in tableoftruth][index])
                #     for fq in [row[eachCol] for row in tableoftruth][index]:
                #         print(fq)
                testsol = testsol + tableoftruth[eachCol]
            # testsol = [testsol]
            # for i in range(len(colifInEight) - 1):
            #     for a,b in zip(tableoftruth[colifInEight[i]],tableoftruth[colifInEight[i+1]]):
            #         print('This is each row in truthTable',a,b)
                    # testSol.ap
                #
                # for indexOfArray in range(len(tableoftruth[colifInEight[i]])):
                #    print('columnwise,', [row[indexOfArray] for row in tableoftruth[colifInEight[i]]],
                #           [row[indexOfArray] for row in tableoftruth[colifInEight[i + 1]]])
                #     # testsol.append(a)
                #     # testsol.append(b)
                # print()
                # for j in range(i+1,len(colifInEight)):
                #     print(tableoftruth[colifInEight[i]][0],tableoftruth[colifInEight[j]][0])
                #     if (tableoftruth[colifInEight[i]][0][0] == tableoftruth[colifInEight[j]][0][0]) or (tableoftruth[colifInEight[i]][0][1] == tableoftruth[colifInEight[j]][0][1]):
                #         testsol.append([i,i+1])

            print()
                    # if tableoftruth[colifInEight[i][0]] == tableoftruth[colifInEight[j][0]]
        elif len(rowifInEight) >= 2 and len(colifInEight) <= len(rowifInEight):
            print(rowifInEight)
            for eachRow in rowifInEight:
                print(tableoftruth[eachRow])
                testsol = testsol + tableoftruth[eachRow]
            sol.append(rowifInEight)
            # for i in range(len(rowifInEight) - 1):
            #     for a,b in zip(tableoftruth[rowifInEight[i]],tableoftruth[rowifInEight[i+1]]):
            #         print('This is each row in truthTable',a,b)
            #     print()
            # for i in range(len(colifInEight)-1):
            #     print()
                # for indexOfArray in range(len(tableoftruth[colifInEight[i]])):
                #     print([row[indexOfArray] for row in tableoftruth[colifInEight[i]]],[row[indexOfArray] for row in tableoftruth[colifInEight[i+1]]])
                #     countColumn = len([j for j in [row[indexOfArray] for row in tableoftruth[colifInEight[i]]] if j == 1])


                # if colifInEight[i] == 0 and colifInEight[i+1] == 1:
                #     print('A')
                #     sol.append('A')
                # if colifInEight[i] == 1 and colifInEight[i + 1] == 2:
                #     print('B')
                #     sol.append('B')
                # if colifInEight[i] == 2 and colifInEight[i + 1] == 3:
                #     print('B')
                #     sol.append('B')
                # if colifInEight[i] == 1 and colifInEight[i + 1] == 2:
                #     print('B')
                #     sol.append('B')



                # for a,b in zip(tableoftruth[colifInEight[i]],tableoftruth[colifInEight[i+1]]):
                #     print(a,b)
                # print(i)
                # print([row[i] for row in list(zip(tableoftruth[colifInEight[i]],tableoftruth[colifInEight[i+1]]))])

                    # print([x == y and x == 1 for x,y in zip(a,b)])
                    # bool.append(first+second)


                    # print(set.intersection(*map(set, bool)))

            print()
        return testsol

    testsol = ifInEight(testsol)
    listAfterEights = []
    aad = []
    if testsol == [] or len(testsol) == 8:
        listAfterEights.append(testsol)
    else:
        for index in range(2):
            print([row[index] for row in testsol])
            tempArray = []
            if [row[index] for row in testsol].count(0) == 8:
                for indexCol,j in enumerate([row[index] for row in testsol]):
                    if j == 0:
                        tempArray.append(indexCol)
                temp2 = []
                for t in tempArray:
                    temp2.append(testsol[t])
                listAfterEights.append(temp2)


            elif [row[index] for row in testsol].count(1) == 8:
                for indexCol, j in enumerate([row[index] for row in testsol]):
                    if j == 1:
                        tempArray.append(indexCol)
                temp2 = []
                for t in tempArray:
                    temp2.append(testsol[t])
                listAfterEights.append(temp2)
            # for j in range(0,len([row[index] for row in testsol]),4):
            #     aad.append([row[index] for row in testsol][j:j+4])

                # if len(colifInEight) >= len(rowifInEight):
                #     # print(testsol[index][qf][0:2])
                #
                #     # for j in [row for row in testsol[index][qf][0:2]]:
                #     #     print(j)
                # else:
                #     print('ROWS')
        # for index in range(0,len(testsol),4):
        #     print()
        #     print(testsol[index:index+4])
        #     for j in [row for row in testsol]:
        #         print(j)
        # for index in range(0, 4):
        #     print(testsol[index:index + 4])
        #     for indexa, j in enumerate([row[index] for row in testsol]):
        #         print(indexa,j)
        #         if [row[index] for row in testsol].count(j) == 8:
        #             print('found', testsol[index:index+7])
    print('THIS IS THE SOLUTION FOR EIGHTS', sol)
    pprint('This is the test solution from truthTable')
    pprint(testsol)
    print('THIS IS THE listAfterEights')
    pprint(listAfterEights)
    print('DONE WITH OCTAVES NOW WITH FOURS')
    #DONE WITH OCTAVES NOW WITH FOURS

    def all_same(items):
        return all(x == 0 for x in items)

    def neighbours(i, j, list):
        vals = sum((row[j - (j > 0):j + 2] for row in list[i - (i > 0):i + 2]), [])
        vals.remove(list[i][j])
        return set(vals)


    actualFours = []

    listOfFoursCheckAlpabet = []
    def ifInFour(listOfFoursCheckAlpabet):
        arrayRem = []
        arrayForFours = []
        for indexOfArray, item in enumerate(listSolution):
            # print(item)
            if sol == []:
                print('no octaves')
                arrayRem = arrayRem + [0,1,2,3]
                break
            for s in sol:
                if indexOfArray not in s:
                    arrayRem.append(indexOfArray)
                    break
        print('Remaining Array', arrayRem)
        print()
        print('lenOfCol,', len(colifInEight), 'lenofRows,', len(rowifInEight))
        if len(colifInEight) >= len(rowifInEight):
            print('this is for COLUMNS')
            for index,eleList in enumerate(tableoftruth):
            # print(eleList)

                for indexOfArray,list in enumerate([(row[index]) for row in tableoftruth]):
                    if (list in testsol) == False and listSolution[index][indexOfArray] == 1:
                        print('THIS IS THE LIST', list)
                        arrayForFours.append(list)
        else:
            for index,eleList in enumerate(tableoftruth):
            # print(eleList)

                for indexOfArray,list in enumerate(eleList):
                    if (list in testsol) == False and listSolution[index][indexOfArray] == 1:
                        print('THIS IS THE LIST', list, eleList)
                        arrayForFours.append(list)


        print('THIS IS THE ARRAY OF FOURS REMAINING')
        pprint(arrayForFours)
        print('The length of fours,',len(arrayForFours))



        remList = [arrayForFours[i] for i in range(len(arrayForFours)) if arrayForFours[i] not in actualFours]
        if len(remList) <= 1:

            return remList
        print('remaining list of 1s', remList)
        f = []

        countf = []
        for r in remList:
            print()
            for index in range(len(tableoftruth)):

                    for indexOfRow,arrayRow, in enumerate([row[index] for row in tableoftruth]):
                        if arrayRow != r:
                                if arrayRow[2:4] == r[2:4]:
                                    print('row    ', arrayRow, r)
                                    if (arrayRow in remList):
                                        print('row in remList   ', arrayRow, r,)
                                        f.append(arrayRow)
            print(f)
            af = []
            if len(f) == 4:
                for ia in range(0,4):
                    for a in [[row[ia] for row in f]]:
                        countf.append(a.count(a[ia]))
                        if a.count(a[ia]) == 4:
                            af.append([ia,a[ia]])
                print(countf)
                if countf.count(4) >= 2:
                    # for c in range(len(countf)):
                    #     print(countf[c])
                    #     if countf[c] == 4:
                    #         listOfFoursCheckAlpabet.append([f[c][c], c])

                    print('print accepted', f)
                    listOfFoursCheckAlpabet.append(af)
                    print(listOfFoursCheckAlpabet)
                    actualFours.append(f)
                    f = []
                    countf = []
                else:
                    f = []
                    countf = []
        print(remList, f )
        f = []
        if actualFours != []:

            for ia in range(len(actualFours)):
                # print(actualFours[ia])
                for aq in range(len(actualFours[ia])):

                    del remList[remList.index(actualFours[ia][aq])]
        if remList != []:
            print('have to do also something more, check in existion solution')
            for r in remList:

                for index in range(len(tableoftruth)):

                    # print(tableoftruth[index])
                    # if (r not in actualFours) or index == 0:
                    for indexOfRow, arrayRow, in enumerate([row[index] for row in tableoftruth]):
                        if arrayRow != r:
                            # if (arrayRow in remList):
                            #WHEN COLUMNS CHECK ROWS
                            # ArrayRow is list for f
                            if arrayRow[2:4] == r[2:4]:
                                print('row    ', arrayRow, r)
                                if (arrayRow in testsol):
                                    print('row in remList   ', arrayRow, r, )
                                    countR = 0
                                    for go in range(len(arrayRow)):
                                        if arrayRow[go] == r[go]:
                                            countR = countR + 1
                                    if countR >= 3:
                                        f.append(r)
                                        f.append(arrayRow)
                print(f)
                af = []
                if len(f) == 4 and f not in testsol:
                    for ia in range(0, 4):
                        for a in [[row[ia] for row in f]]:
                            countf.append(a.count(a[ia]))
                            if a.count(a[ia]) == 4:
                                af.append([ia, a[ia]])
                    print(countf)
                    if countf.count(4) >= 2:
                        # for c in countf:
                        #     print(c)
                        #     if c == 4:
                        #         listOfFoursCheckAlpabet.append([c, countf.index(c)])
                        print('print accepted')
                        listOfFoursCheckAlpabet.append(af)
                        print(listOfFoursCheckAlpabet)
                        actualFours.append(f)

                        f = []
                        countf = []
                    else:
                        f = []
                        countf = []

            for ia in range(len(actualFours)):
                print(actualFours[ia], remList)
                for aq in range(len(actualFours[ia])):
                    # del remList[remList.index(actualFours[ia][aq])]
                    if actualFours[ia][aq] in remList:
                        print(actualFours[ia][aq], remList)
                        del remList[remList.index(actualFours[ia][aq])]
            # print(remList)

            return remList
        else:
            return []








            # print(neighbours(arrayForFours[i][1], arrayForFours[i][0], listSolution))
            # if len(colifInEight) >= 2:
            #     if index in arrayRem:
            #         print([int(row[index]) for row in listSolution])
            #         isZeroColumn = len([i for i in [int(row[index]) for row in listSolution] if i == 0])
            #
            # elif len(rowifInEight) >= 2:
            #     if index in arrayRem:
            #         print(eachList)
            # if index in arrayRem:
            #     print([int(row[index]) for row in listSolution])
            #     print(eachList)
            #
            #
            #     for indexOfEachList,each in enumerate(eachList):
            #         if each == 1 and indexOfEachList in arrayRem:
            #             # if (all_same([int(row[index]) for row in listSolution])):
            #             #
            #             # print(a)
            #             print(each, eachList, [int(row[index]) for row in listSolution],  indexOfEachList, index)

    listAfterFours = ifInFour(listOfFoursCheckAlpabet)

    print('This is the actual Fours ALMOST WORKS')
    pprint(actualFours)
    pprint(listAfterFours)
    pprint(listOfFoursCheckAlpabet)
    def findOnes():
        print('HERE GOES THE ONES if ANY')


    actualTwos = []
    def findTwos():
        print('a')



    if listAfterFours == []:
        findOnes()
    else:
        print('Find the diades')
        findTwos()




















    #MIN SVISEIS
    # if len(arrayForFours) >= 4:
    #     countCola = []
    #     print('Check first if they make themselves a square')
    #     for index,list in enumerate(arrayForFours):
    #         # if len(arrayForFours[len(actualFours):len(arrayForFours)-1]) < 4:
    #         #     print('i broke')
    #         #     break
    #         if len(arrayForFours[index:4+index]) == 4:
    #             for indexOfEachList in range(len(arrayForFours[index:4+index])):
    #                 countCola = countCola + [len([i for i in [int(row[indexOfEachList]) for row in arrayForFours[index:4+index]] if i == 1])]
    #             print(countCola)
    #             if countCola.count(0) == 2 or countCola.count(4) == 2 or (countCola.count(0) == 1 and countCola.count(4) == 1):
    #                 print('MIA TETRADA',arrayForFours[index:4 + index])
    #                 # testsol.append(arrayForFours[index:4 + index])
    #                 for l in arrayForFours[index:4 + index]:
    #                     actualFours.append(l)
    #                 # del arrayForFours[index:4 + index]
    #                 # print('Array Remaining',arrayForFours)
    #             countCola = []
    #
    #     print(arrayForFours, len(arrayForFours))


