#  Q2(3)1 + x/1 + x2/2 + x3/3 + x4/4 + ..... + N terms 

x=int(input("enter a number"))
n=int(input("enter a number"))
i=0
sum=0
while i<=n:
    s=(x**i)//(i+1)
    sum+=s
    i+=1
print(round(sum,9))
    