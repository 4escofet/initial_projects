#import string library to make translate string operation
import string

#Open file, separate words taking out spaces, characters and upper cases
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    #count words
    for word in words:
        counts[word]= counts.get(word,0)+1

#Create a list and input dict values in reverse order
lst = list()
for key, val in counts.items():
    lst.append( val,key)
#Sort dict within the list descending
lst = sorted(lst, reverse= True)
#Print top 10 values-key pairs
for val, key in lst[:10]:
    print(key, val)
#All previous code in one line:
c = counts
print(sorted( [ (v,k) for k,v in c.items() ] ) )
