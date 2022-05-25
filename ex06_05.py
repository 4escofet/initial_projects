str = 'X-DSPAM-Confidence: 0.8475 '
print(str)
ipos = str.find(':')
print(ipos)
piece = str[ipos+1:]
piece = piece.strip()
value = float(piece)
print(value)
