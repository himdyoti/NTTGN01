import re

patt = re.compile(r'.*?interface')
#ptxt = r'.*?(?P<inf>interface)\s*(?P<iname>[a-zA-Z0-9\/]+)\s*?(description)\s*(?P<desc>[a-zA-Z0-9]+)\s*(ip address)\s*(?P<ips>[0-9\.\s]+)(duplex)\s*(?P<duplx>[a-z]+)\s*(speed)\s*(?P<speedv>[a-z]+)'
ptxt = r'^.*(?P<key>interface|description|ip address|duplex|speed)(?P<val>.+)$'
patt2 = re.compile(ptxt,re.MULTILINE)