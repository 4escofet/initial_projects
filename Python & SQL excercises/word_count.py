
#If manually input string
#line = input('Enter a line of text: ')

#print('Words: ', words)
#print('Counting')
name = input('Enter file: ')
handle = open(name)

counts = dict()

for word in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
#print('Counts', counts)
#Up to here we have construct an histogram
#Next steps identify the max word-count
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = words
        bigcount = counts
print(bigword, bigcount)
