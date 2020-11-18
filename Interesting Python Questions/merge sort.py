def merge(lefthalf, righthalf):
    answerList = []
    while len(lefthalf) > 0 and len(righthalf) > 0:
        if lefthalf[0] < righthalf[0]:
            answerList += [lefthalf[0]]
            lefthalf = lefthalf[1:]
        else:
            answerList += [righthalf[0]]
            righthalf = righthalf[1:]
    for i in lefthalf:
        answerList += [i]
    for j in righthalf:
        answerList += [j]
    return answerList


def mergesort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = int(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

def main():
    aList = [10, 5, 2, 9, 6, 3, 4, 8, 1, 7]
    print(mergesort(aList))

    list1 = [1, 4, 6, 10]
    list2 = [5, 7, 8, 11, 12]
    print(merge(list1, list2))

main()

