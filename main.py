import os

op=open('test.txt','r')
trainarr=[]
for x in op.readlines():
    print(x)
    x=x.replace('\n','')
    trainarr.append(x.replace('Images/',''))
print(trainarr)
for x in os.listdir('Images\\'):
    print(x)
    extension=os.path.splitext(x)[1]
    if x in trainarr:
        if extension =='.jpg':
            os.replace('Images\\' + x, 'image\\val\\' + x)
        if extension=='.txt':
            os.replace('Images\\' + x, 'labels\\val\\' + x)