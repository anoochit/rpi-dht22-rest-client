#!/usr/bin/env python
 
import requests
from time import gmtime, strftime

rest_server="http://localhost:3000/api/Temperatures"
ctime=strftime("%a, %d %b %Y %X +0000", gmtime())

payload = {'timestamp': ctime, 'temp': '30.00', 'humid': '60.00'}
r = requests.post(rest_server, data=payload)

print r.text
