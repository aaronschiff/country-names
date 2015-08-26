# Country disambiguation

These scripts assist with the construction of a list to disambiguate the names of countries. The list of ISO 3166 countries from Wikipedia is used as the list of "standard" country names (https://en.wikipedia.org/wiki/ISO_3166). 

The script get3166.py scrapes the list of ISO 3166 country names and other information from Wikipedia and saves it in countries.csv.

The script disambiguate.py generates a lookup table of alternative names for each of the ISO 3166 country names. It does this by parsing the list of transitive redirects on Wikipedia constructed by the DBpedia project (http://downloads.dbpedia.org/2015-04/core-i18n/en/transitive-redirects_en.ttl.bz2). 

The end result is a CSV file with two columns: alternative country names, and standardised (ISO 3166) names. 

The code is quite fragile and slow, but it should not be necessary to run it frequently. 