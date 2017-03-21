# Dumps PDFs from CONTENTdm. xmlfile is an XML document retrieved via OAI-PMH harvesting of a CONTENTdm collection.

from sys import argv
from urllib2 import urlretrieve
import urlparse
import xml.etree.ElementTree as ET

xmlfile = argv[1]
collection_to_dump = argv[2]
outdir = argv[3] #### note: no error checking for if outdir exists; TODO

#Extract URLsparsed = ET.parse(xmlfile)

for elem in parsed.iter(tag='identifier'):
  pathchunks = urlparse.urlparse(elem.text).path.rsplit(':')[1].split('/')
  if pathchunks[0] == collection_to_dump:
  url = str('http://server.domain.edu/utils/getfile/' + pathchunks[0 + '/id/' + pathchunks[1] + '/')
  urlretrieve(url, str(outdir + '/' + pathchunks[1] + '.pdf'))
  print 'Retrieved ' + pathchunks[1] + '.pdf'

