import urllib.request, urllib.parse, urllib.error

url: 'http://py4e-data.dr-chuck.net/comments_42.xml'
fhand = urllib.request.urlopen(url)
for line in fhand:
    print(line.decode().strip())
