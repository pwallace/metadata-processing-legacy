# Outputs a CSV containing [IDENTIFIER, TITLE, SUBJECT[0], SUBJECT[1], etc...]

import internetarchive
from sys import argv
import csv

collection = argv[1]
outfile = argv[2]

search_collection = internetarchive.search_items('collection:' + collection)

#searches collection, spits out csv with id, title, subjects

print str(search_collection.num_found) + " items in collection"

data = []
rowcount = 0

for result in search_collection:
  item_identifier = result['identifier']
  item = internetarchive.get_item(item_identifier)

  print "Downloading " + item_identifier + " ..."


  title = item.item_metadata['metadata']['title']
  subjects = item.item_metadata['metadata']['subject']
  rowdata = [item_identifier]
  rowdata.append(title)
  
  if len(subjects) > rowcount:
    rowcount = len(subjects)
  
  for i in subjects:
    rowdata.append(i)
  data.append(rowdata)
  
with open(outfile, 'wb') as csv_out:
  csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

  header = ['identifier','title']
  n = 0
  while n < rowcount:
    header.append('subject[' + str(n) + ']')
    n += 1

  csv_writer.writerow(header)
  for row in data:
    csv_writer.writerow(row)
