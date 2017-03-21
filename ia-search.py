# Returns a list of item identifiers in a collection

import internetarchive
import json
import sys

argv = sys.argv
collection = argv[1]

search_collection = internetarchive.search_items('collection:' + argv[1])

print str(search_collection.num_found) + " items in collection"
for result in search_collection:
  item_identifier = result['identifier']
  item = internetarchive.get_item(item_identifier)
  print item_identifier
