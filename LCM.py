def lcm1(a,b):
    n=max(a,b)
    lcm=n
    while True:
        if lcm%a==0 and lcm%b==0:
            return lcm
        lcm+=n
n1=int(input("enter no.:") )
n2=int(input("enter no.:") )
result=lcm1(n1,n2)
print("LCM:",result)
