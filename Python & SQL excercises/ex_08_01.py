#fname = input("Enter file name: ")
han = open('mbox-short.txt')
count = 0
for line in han:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 3 or wds[0] != 'From': continue
    print(wds[1])
    count +=1
print("There were", count, "lines in the file with From as the first word")
