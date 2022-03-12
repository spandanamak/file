f=open("sandy.txt","r")
c=0
for line in f:
    if f!="\n":
        c+=1
f.close()
print(c)
    
    