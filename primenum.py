# Write a function to check if a number is prime. 
# Return: True or False
def is_prime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
             return False
    return True
num=int(input("enter no:"))
if is_prime(num):
    print( f"{num} number is prime")
else:
    print(f"{num} number is not prime")
