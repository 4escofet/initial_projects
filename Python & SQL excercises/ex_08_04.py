#fname = input("Enter file name: ")
han = open('romeo.txt')
wl = list()
for line in han:
    line = line.rstrip()
    wds = line.split()
    for word in wds:
        if word not in wl:
            wl.append(word)
wl.sort()
print(wl)
