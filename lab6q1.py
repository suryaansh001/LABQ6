

n=str(input())
vowels="AEIOUaeiou"
space=" "
count_v=0
count_c=0
count_w=1
for char in n:
    if char in vowels:
        count_v+=1
    elif char in space:
        count_w+=1
    else:
        count_c+=1
print(count_v)
print(count_c)
print(count_w)