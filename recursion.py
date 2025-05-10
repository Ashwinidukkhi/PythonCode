# recursion :  call itself
# note : $ no base condition
# $ infinite recursion
# $ no return value
def factorial(a,b):
    if  a==0 or b==1:
        return  1
    else:
        return (2*factorial())
    