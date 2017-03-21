# Dumps image collection from CONTENTdm based on OAI-PMH harvested XML file

from sys import argv
from urllib2 import urlretrieve
import urlparse
import xml.etree.ElementTree as ET

xmlfile = argv[1]
collection_to_dump = argv[2]
outdir = argv[3] #### note: no error checking for if outdir exists; TODO

max_x = 10000
max_y = 10000

#Extract URLs

parsed = ET.parse(xmlfile)

for elem in parsed.iter(tag='identifier'):
  pathchunks = urlparse.urlparse(elem.text).path.rsplit(':')[1].split('/')
  if pathchunks[0] == collection_to_dump:
  url = str('http://server.domain.edu/utils/ajaxhelper/?CISOROOT='+ pathchunks[0] + '&CISOPTR=' + pathchunks[1] + '&action=2&DMSCALE=100&DMWIDTH='+ max_x + '&DMHEIGHT=' + max_y + '&DMX=0&DMY=0')
  urlretrieve(url, str(outdir + '/' + pathchunks[1] + '.jpg'))
  
  print 'Retrieved ' + pathchunks[1] + '.jpg'

