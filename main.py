op=open('train.txt','r')
trainarr=[]
for x in op.readlines():
    print(x)
    x=x.replace('\n','')
    trainarr.append(x.replace('Images/',''))
print(trainarr)