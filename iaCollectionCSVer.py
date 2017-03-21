import internetarchive
import json
import sys
import csv

argv = sys.argv
outfile = argv[4]
csv_out = csv.writer(open(outfile, 'w'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

def main(argv, csv_out):
	search_string = argv[1]
  collection = argv[2]
  new_collection = argv[3]
  search_collection = internetarchive.search_items('collection:' + collection)
  getMetadata(search_string, collection, new_collection, outfile, csv_out, search_collection)

def searchAndWrite(csv_out, search_string, item_identifier, collection, new_collection, title, description,subjects):
  if any([search_string in title]):
    addLineForNewCollection(item_identifier, collection, new_collection)
  elif any([search_string in description]):
    addLineForNewCollection(item_identifier, collection, new_collection)
  else:
    if type(subjects) is list:
      for subject in subjects:
        if any([search_string in subject]): 
          addLineForNewCollection(item_identifier, collection, new_collection)
    else:
      if any([search_string in subjects]): 
        addLineForNewCollection(item_identifier,collection,new_collection)

def getMetadata(search_string, collection, new_collection, outfile, csv_out, search_collection):
  print str(search_collection.num_found) + " items in collection"
  for result in search_collection:
    item_identifier = result['identifier']
    item = internetarchive.get_item(item_identifier)
    metadata = item.item_metadata['metadata']
    print "Downloading " + item_identifier + " ..."
    if 'title' in metadata:
      title = metadata['title']
    if 'subject' in metadata: 
      subjects = metadata['subject']
    if 'description' in metadata:
      description = metadata['description']
    searchAndWrite(csv_out, search_string, item_identifier, collection, new_collection, title, description, subjects)

def addLineForNewCollection(item_identifier, collection, new_collection):
  rowdata = ''
  print('Added ' + item_identifier + ' to CSV')
  rowdata = [item_identifier]
  rowdata.append(collection)
  rowdata.append(new_collection)
  csv_out.writerow(rowdata)

main(argv, csv_out)
