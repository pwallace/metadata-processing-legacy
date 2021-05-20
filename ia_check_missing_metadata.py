# Program to fetch metadata from IA item list and check for missing metadata elements

import internetarchive as ia
import sys

# Takes plaintext, line-delimited list of IA identifiers

infile = sys.argv[1]

# Takes element label (e.g., "title", "creator", etc)

element = sys.argv[2]

# Checks each item to see if it has a "transcription" field in metadata.
# If no "transcription" element is found, prints the item's identifier

with open(infile, 'r') as read_obj:
	Ialist = read_obj.readlines()
	for iaobject in Ialist:
		item = ia.get_item(iaobject)
		metadata = item.item_metadata['metadata']
		try:
			transcription = metadata[element]
		except KeyError:
			print(metadata['identifier'])
