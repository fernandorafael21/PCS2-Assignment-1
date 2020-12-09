if __name__ == '__main__':
    lst = []
    ordered_names=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst = lst+[[name,score]]
    scores = []
    for i in lst:
        scores = scores+[i[1]]
    scores.sort()
    no_repetitions = list(dict.fromkeys(scores))
    ind_min = scores.index(min(no_repetitions))
    for j in lst:
        if j[1] == no_repetitions[ind_min+1]:
            ordered_names = ordered_names+[j[0]]
    ordered_names.sort()
    for name in ordered_names:
        print(name)
