# Continuous Numbers in Triangle: 
# Input:10 
# Output: 
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10

n=int(input())
x=1
row=1
while x<=n:
    for i in range(row):
        if x>n:
            break
        print(x,end=' ')
        x+=1
    print()
    row+=1