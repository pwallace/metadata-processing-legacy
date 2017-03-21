# Searches for a string in identifier, returns first filename associated with identifier.

import internetarchive
import json
import sys
import csv

argv = sys.argv
collection = argv[1]
search_key = argv[2]

search_collection = internetarchive.search_items('collection:' + argv[1])

print str(search_collection.num_found) + " items in collection"
count = 0
csv_out = csv.writer(open('filelist.csv', 'wb'), delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for result in search_collection:
  item_identifier = result['identifier']
  if any([search_key in item_identifier]):
    print item_identifier
    count = count+1
    fnames = [f.name for f in internetarchive.get_files(item_identifier, glob_pattern='*')]
    csv_out.writerow([item_identifier, fnames[0]])
print(str(count) + ' items found.')
