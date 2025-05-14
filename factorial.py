# Print the factorial of a number using a while loop. 
# Input: 5 
# Output: 120 

n=int(input("enter"))
f=1
i=1
while i<=n:
    f=i*f
    i=i+1
print("factorial",f)