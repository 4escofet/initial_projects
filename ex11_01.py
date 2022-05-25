import re

hand = open('regex_sum_1484224.txt')
numlist= list()

for line in hand:
    line = line.rstrip()
    #print(line)
    num = re.findall('([0-9]+)', line)

    if len(num) >0:
        #print(num)
        for element in num:
            numlist.append(int(element))

print(numlist)
print('Sum: ', sum(numlist))

#[expression for item in iterable if condition == True]
