# Dumps JSON to textfile for items within an IA collection

import internetarchive
import json
import sys
import os

argv = sys.argv
collection = argv[1] # Collection name to scrape
output_file = argv[2] # Name of outfile for JSON dump

search_collection = internetarchive.search_items('collection:' + argv[1])

print str(search_collection.num_found) + " items in collection"
with open(output_file, 'w') as outfile:
  outfile.write('{"collection_items" : [')
  for result in search_collection:
    item_identifier = result['identifier']
    item = internetarchive.get_item(item_identifier)

    print "Downloading " + item_identifier + " ..."

    jdata = item.item_metadata['metadata']
    json_record = json.dumps(jdata)

    outfile.write(str(json_record) + ",")
  outfile.seek(-1, os.SEEK_END)
  outfile.truncate()
  outfile.write(']}')
