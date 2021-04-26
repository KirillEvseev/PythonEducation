#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
if __name__ == '__main__':
    L = []
    ScoreS = set()
    for i in range(int(input())):
        name = input()
        score = float(input())
        inner_list = []
        inner_list.append(name)
        inner_list.append(score)
        
        L.append(inner_list)
        ScoreS.add(score)

    ScoreL = list(ScoreS)
    ScoreL.sort()
    L.sort(key = lambda x: x[0])
    
    for i in L:
        if i[1] == ScoreL[1]:
            print (i[0])
