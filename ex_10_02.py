import string

name = input('Enter file: ')
try:
    handle = open(name)
except:
    handle = open('mbox-short.txt')

hours = dict()
for line in handle:
    line = line.strip()
    if line.startswith("From "):
        wds = line.split()
        print(wds)
        hour = wds[5].split(":")[0] #take fifth item in list, split it in :, and take the first
        hours[hour] = hours.get(hour,0)+1 #Create/ update in the dictionary and count it

lst=list()
for k,v in hours.items():
    new=(k,v)
    lst.append(new)

lst = sorted(lst,reverse=False)
for k,v in lst:
    print(k,v)
