fname = input("Enter file name: ")
fh = open(fname)
count = 0
accum = 0
sval = 0

def str_val(str):
    ipos = str.find(':')
    return float(str[ipos+1:].strip())

for line in fh:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        count +=1
        sval = str_val(line)
        accum = accum + sval
print('Average spam confidence: ',accum/count)
