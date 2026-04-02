n=int(input("Enter ur fucking no. aniket "))
fact=[]
for i in range(2,n//2):
    if(n%i==0):
        fact.append(i)
print(fact)
p=n
for element in fact:
    for el in fact:
        if((el*element)==n):
            t=abs(el-element)    
            if(t<p):
                p=t
                l1=el
                l2=element
print(l1,l2)      
            
        