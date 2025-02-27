def print_star(n):
    for i in range(1,n+1):
        print(" "*((n-i)//2),end="")
        for j in range(1,i+1):
            print(j,end='')
        print()

n=4
print_star(n)