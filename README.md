# metadata-processing

------- iaCollectionCSVer.py -------

DEPENDS ON: https://github.com/jjjake/internetarchive

PURPOSE: to facilitate bulk update of extant Internet Archive items to a include a new collection.

PERFORMS THE FOLLOWING:
1. Searches an existing IA collection for items with matching [search_string] in "title", "description", or "subject" fields.
2. Fetches object metadata and appends a new collection field
3. Outputs a CSV intended for re-upload with the internetarchive command line tool.

USAGE: iaCollectionCSVer.py [search_string] [name_of-collection_to_search] [name_of_new_collection] [outfile.csv]
