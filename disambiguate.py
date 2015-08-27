import csv

dbpediaPrefix = '<http://dbpedia.org/resource/'		# Prefix string for links in dbpedia redirects file

# Read in countries.csv created by get3166.py
countries = {}
with open('countries.csv', 'rb') as countriescsv:
	reader = csv.DictReader(countriescsv)
	
	for row in reader:
		link = dbpediaPrefix + row['Country-link'][6:] + '>'		# Remove '/wiki/' from link and create dbpedia link
		name = row['Name']
		countries[link] = {'name': name, 'alternatives': []}

# Parse transitive links file one line at a time
with open('transitive-redirects_en.ttl', 'rb') as linksfile:
	for line in linksfile:
		items = line.split()
		
		possibleCountry = items[2]		# Extract possible country link
		
		if possibleCountry in countries:
			alt = items[0][len(dbpediaPrefix):][:-1]
			alt = alt.replace("_", " ")
			countries[possibleCountry]['alternatives'].append(alt)
			
# Output csv file of countries and alternatives
with open('country-names-cross-ref.csv', 'wb') as f:
	writer = csv.writer(f)
	for country, info in sorted(countries.items()):
		for alt in info['alternatives']:
			row = [alt, info['name']]
			writer.writerow(row)

