f=open("shalini.txt","r")
f1=open("delhi.txt","r")
f2=open("shimla.txt","r")
f3=open("others.txt","r")
b=f.read()
d=b.split("\n")
i=0
while i<len(d):
    if "delhi" in d[i]:
        f1.write(d[i])
        f1.write("\n")
    elif "shimla" in d[i]:
        f2.write(d[i])
        f2.write("\n")
    else:
        f3.write(d[i])
        f3.write("\n") 
    i=i+1
f.close()



