if __name__ == '__main__':
    L = []
    ScoreL = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        inner_list = []
        inner_list.append(name)
        inner_list.append(score)
        
        L.append(inner_list)
        ScoreL.append(score)

    ScoreL.sort()
    L.sort(key = lambda x: x[0])
    
    for i in L:
        if i[1] == ScoreL[1]:
            print (i[0])
