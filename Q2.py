data = {"mouse":[5,7,6],"keyboard":[3,2,4],"monitor":[2,1,3]}
itemmax = ""
summax = 0
for k,v in data.items():
    sumitem = sum(v)
    print(k,sumitem)
    if(sumitem>summax):
        summax=sumitem
        itemmax=k

print(itemmax)