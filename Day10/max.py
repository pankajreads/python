a=[1,6,8,2,9,0,22]
b=max(a)
maxi=a[0]
for n in a:
    if n>maxi:
        maxi=n
print(maxi==b)