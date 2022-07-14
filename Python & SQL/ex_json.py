import json
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_1484229.json'
lista = list()
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)

for item in info['comments']:
    #print(item['count'])
    lista.append(item["count"])

print('Retrieved', len(data), 'characters')
print('Count:', len(lista))
print('Sum:', sum(lista))
