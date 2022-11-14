def total(n,d,w):
    if(n>=1):
        t_width=(n-2)*w
        distance=(n-1)*d*100
        total=t_width+distance
        return(total)
        
n = int(input('Enter number of pillars: '))
d = float(input('Enter Distance between pillars: '))
w = int(input('Enter width of pillar: '))
print(total(n,d,w))
