while True:
    myList = list(map(int, input().split()))
    if sum(myList) == 0:
        break
    
    myList = sorted(myList)
    if myList[2] ** 2 == myList[0] ** 2 + myList[1] ** 2:
        print('right')
    else:
        print('wrong')