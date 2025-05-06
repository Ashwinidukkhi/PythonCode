n1,n2,n3=map(int,input("enter:").split())
if n1>n2 and n1>n3:
    num=n1
elif n2>n1 and n2>n3:
    num=n2
else:
    num=n3
print("greater number",num)
