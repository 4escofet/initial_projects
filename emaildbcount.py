import sqlite3 #import library

conn = sqlite3.connect('emaildb.sqlite') #create DB and handle file
cur = conn.cursor() #Create cursor to DB

cur.execute('DROP TABLE IF EXISTS Counts') #If exists drop DB

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''') #Create schema

fname = input('Enter file name: ') #Ask to input file name
if (len(fname) < 1): fname = 'mbox.txt' #Set default input if no empty
fh = open(fname) #handle file open
for line in fh: #loop iteratin thrue file
    if not line.startswith('From: '): continue #Skip line if not "From:""
    pieces = line.split() #split line by spaces
    email = pieces[1] #take second word
    email = email.split('@')[1] #split email and take domain
    cur.execute('SELECT org FROM Counts WHERE org = ? ', (email,))
    row = cur.fetchone() #make a SELECT whit email took it before
    if row is None: #If no results in SELECT, inser it
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (email,))
    else: #if there exists, its ads 1 to the email count
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
    conn.commit() #save changes in DB

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
# Select 1st 10 rows of emails and count columns ordering by count
for row in cur.execute(sqlstr): #iterate and printing the previous selection
    print(str(row[0]), row[1])

cur.close()#close connection to DB
