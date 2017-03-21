import internetarchive
import json
import sys
import csv

argv = sys.argv
outfile = argv[2]
csv_out = csv.writer(open(outfile, 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

def main(argv, csv_out):
  rowheaders = ('url', 'identifier', 'title', 'creator', 'description', 'subject', 'date', 'type', 'format', 'source', 'rights')
  collection = argv[1]
  search_collection = internetarchive.search_items('collection:' + collection)
  csv_out.writerow(rowheaders)
  getMetadata(collection, outfile, csv_out, search_collection)

def writeout(csv_out, dl_url, item_identifier, collection, title, creator, description, subjects, date, itemtype, itemformat, source, rights):
  if type(subjects) is list:
    subject_field = ''
    for subject in subjects:
  if subject_field != '':
      subject_field = subject_field + '; ' + subject
    else:
      subject_field = subject
    else:
      subject_field = subjects
  rowdata = (dl_url, item_identifier, title, creator, description, subject_field, date, itemtype, itemformat, source, rights)
  csv_out.writerow(rowdata)
    

def getMetadata(collection, outfile, csv_out, search_collection):
  print str(search_collection.num_found) + " items in collection"
  for result in search_collection:
    title = subjects = creator = description = date = itemtype = itemformat = source = rights = ''
    item_identifier = result['identifier']
    item = internetarchive.get_item(item_identifier)
    metadata = item.item_metadata['metadata']
    print "Downloading " + item_identifier + " ..."
    
    if 'title' in metadata:
      title = metadata['title']
    if 'subject' in metadata: 
      subjects = metadata['subject']
    if 'creator' in metadata:
      creator = metadata['creator']
    if 'description' in metadata:
      description = metadata['description']
    if 'date' in metadata:
      date = metadata['date']
    if 'type' in metadata:
      itemtype = metadata['type']
    if 'format' in metadata:
      itemformat = metadata['format']
    if 'rights' in metadata:
      rights = metadata['rights']
    if 'source' in metadata:
      source = metadata['source']
    fnames = [f.name for f in internetarchive.get_files(item_identifier, glob_pattern='*jpg')]
    imageid = fnames[0]
    dl_url = str('https://archive.org/download/' + item_identifier + '/' + imageid)
    writeout(csv_out, dl_url, item_identifier, collection, title, creator, description, subjects, date, itemtype, itemformat, source, rights)

main(argv, csv_out)
