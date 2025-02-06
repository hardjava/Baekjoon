enter = list(map(int, input().split()))

def printValue(l=list):
    if l[0] == 8:
        for i in range(1, 8):
            if l[i] != l[i - 1] - 1:
                print('mixed')
                return
        print('descending')
        return
    
    elif l[0] == 1:
        for i in range(1, 8):
            if l[i] != l[i - 1] + 1:
                print('mixed')
                return
        print('ascending')
        return
    
    else:
        print('mixed')
        return

printValue(enter)