def multiplication_table(m, n):
    for i in range(1,10):
        for j in range(m,n+1):
            product = i*j
            print ("%d X %d = %-2d\t" %(i,j,product), end="")
        print("")
    print("\n")

def pyramid(n):
    for i in range (n):
        print (" "*(n-i)+"*"*(i)*2+"*")
