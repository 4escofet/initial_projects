fname = input("Enter file name: ")
fh = open(fname)
count = 0
accum = 0
sval = 0

def str_val(str):
    ipos = str.find(':')
for line in fh:
    if not line.startwith('X-DSPAM-Confidence:'):
        continue
    else:
        count +=1
        sval =
        accum = accum + sval
