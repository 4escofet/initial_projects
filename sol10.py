fname = input("Enter a file name:")
if len(fname) < 1: fname="mbox-short.txt"
fhand = open(fname)

hours = dict()
for line in fhand:
    line = line.strip()
    if line.startswith("From "):
        wds = line.split()
        hour = wds[5].split(":")[0]
        hours[hour] = hours.get(hour,0)+1

lst=list()
for k,v in hours.items():
    new=(k,v)
    lst.append(new)

lst = sorted(lst,reverse=False)
for k,v in lst:
    print(k,v)
