# metadata-processing

------- iaCollectionCSVer.py -------

Depends on https://github.com/jjjake/internetarchive

Purpose: to facilitate bulk update of extant Internet Archive items to a include a new collection.

Performs the following tasks:
1. Searches an existing IA collection for items with matching [search_string] in "title", "description", or "subject" fields.
2. Fetches object metadata and appends a new collection field
3. Outputs a CSV intended for re-upload with the internetarchive command line tool.

Usage iaCollectionCSVer.py [search_string] [name_of-collection_to_search] [name_of_new_collection] [outfile.csv]
