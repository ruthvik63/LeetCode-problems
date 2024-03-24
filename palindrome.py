x=int(input("x:"))
x=str(x)
n=len(x)
a=True

for i in range(n):
    if x[i]!=x[n-i-1]:
        a= False

print(a)