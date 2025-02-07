def isPalindrome(s=str):
    start = 0
    end=len(s) - 1

    while(start < end):
        if s[start] != s[end]:
            print('no')
            return
        start += 1
        end -= 1
    
    print('yes')

while True:
    enter = input()
    if enter == '0':
        break

    isPalindrome(enter)