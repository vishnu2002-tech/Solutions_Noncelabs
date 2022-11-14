def table(n):
    for i in range(1,11):
        c=i*n
        print(i,"*",n,"=",c)
    

n = int(input('Enter number: '))
table(n)
