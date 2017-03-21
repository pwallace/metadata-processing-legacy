# metadata-processing

***
SCRIPT: ia-search.py

DEPENDS ON: https://github.com/jjjake/internetarchive

PURPOSE: Returns a list of item identifiers in an Internet Archive collection.

USAGE: python ia-search.py [collection_to_search]

*** 
SCRIPT: ia-file-list.py

DEPENDS ON: https://github.com/jjjake/internetarchive

PURPOSE: Searches an Internet Archive collection for a string in identifier, returns first filename associated with identifier.

USAGE: python ia-file-list.py [collection_to_search] [search_string]

***
SCRIPT: ia-json.py

DEPENDS ON: https://github.com/jjjake/internetarchive

PURPOSE: Dumps JSON to for items within an Internet Archive collection

USAGE: python ia-json.py [collection_to_scrape] [outfile.json]

***
SCRIPT: iaCollectionCSVer.py

DEPENDS ON: https://github.com/jjjake/internetarchive

PURPOSE: to facilitate bulk update of extant Internet Archive items to a include a new collection.

PERFORMS THE FOLLOWING:
1. Searches an existing IA collection for items with matching [search_string] in "title", "description", or "subject" fields.
2. Fetches object metadata and appends a new collection field
3. Outputs a CSV intended for re-upload with the internetarchive command line tool.

USAGE: python iaCollectionCSVer.py [search_string] [name_of-collection_to_search] [name_of_new_collection] [outfile.csv]
***

SCRIPT: ia-fetch-subjects.py

DEPENDS ON: https://github.com/jjjake/internetarchive

PURPOSE: Outputs a CSV containing [IDENTIFIER, TITLE, SUBJECT[0], SUBJECT[1], etc...]

USAGE: python ia-fetch-subjects.py [collection_to_search] [outfile.csv]
***
