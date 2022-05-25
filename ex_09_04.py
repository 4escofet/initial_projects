
#If manually input string
#line = input('Enter a line of text: ')

#print('Words: ', words)
#print('Counting')
name = input('Enter file: ')
try:
    handle = open(name)
except:
    handle = open('mbox-short.txt')

from_lines = dict()
for line in handle:
    if not line.startswith('From:'):
        continue
    else:
        line = line.rstrip()
        words = line.split()
        word = words[1]
        #print(words)
        from_lines[word] = from_lines.get(word,0)+1
#At this point we have a dic whit emails per user
bigcount = None
frecuent_user = None
for user, count in from_lines.items():
    if bigcount is None or count > bigcount:
        frecuent_user = user
        bigcount = count

print(frecuent_user, bigcount)
