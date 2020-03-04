if __name__ == '__main__':
    s = input('Enter string:')
    counter=0
    for i in range(len(s)):
        if(s[i].isalnum() == True):
            print('True')
            break
        counter += 1
        if(counter == len(s)):
            print('false')
    counter=0
    for i in range(len(s)):
        if(s[i].isalpha() == True):
            print('True')
            break
        counter += 1
        if(counter == len(s)):
            print('false')
    counter=0
    for i in range(len(s)):
        if(s[i].isdigit() == True):
            print('True')
            break
        counter += 1
        if(counter == len(s)):
            print('false')
    counter=0
    for i in range(len(s)):
        if(s[i].islower() == True):
            print('True')
            break
        counter += 1
        if(counter == len(s)):
            print('false')
    counter=0
    for i in range(len(s)):
        if(s[i].isupper() == True):
            print('True')
            break
        counter += 1
        if(counter == len(s)):
            print('false')
