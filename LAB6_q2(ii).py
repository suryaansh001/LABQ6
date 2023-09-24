#1/1! + 1/2! + 1/3! + 1/4! + ... + 1/N!
n=int(input("enter a number :"))
i=1
fact=1
sum=0
while i<=n:
    s=1/(fact)
    i+=1
    fact=fact*i
    sum+=s
    
print((round(sum,9)))