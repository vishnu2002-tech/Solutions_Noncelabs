def ltr(s,l):
    if ((type(s)==str) and (type(l)==str)):
            if((int(ord(s)) >= 65 and int(ord(s)) <= 90) and (int(ord(l)) >= 65 and int(ord(l)) <= 90)):
                return 1
            elif((int(ord(s)) >= 97 and int(ord(s)) <= 122) and (int(ord(l)) >= 97 and int(ord(l)) <= 122)):
                return 1
            elif((int(ord(s)) >= 65 and int(ord(s)) <= 90) and (int(ord(l)) >= 97 and int(ord(l)) <= 122)):
                return 0
            elif((int(ord(l)) >= 65 and int(ord(l)) <= 90) and (int(ord(s)) >= 97 and int(ord(s)) <= 122)):
                return 0
            else:
                return -1
    
    else:
        return -1
    

s = str(input('Enter letter: '))
l = str(input('Enter letter: '))
print(ltr(s,l))
