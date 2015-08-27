from bs4 import BeautifulSoup
import urllib2
import string
import csv

url = "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

countriesTable = None 	# Will store the table after we find it
maxRows = 0				# For finding table with the most rows

# Find the right table on the ISO 3166 page
for table in soup.findAll('table', {'class' : 'wikitable'}):
	rows = table.findAll('tr')
	
	# The table we want is the longest one on the page
	if len(rows) > maxRows:
		maxRows = len(rows)
		countriesTable = table
		
# Extract data from the table of countries
report = []
for row in countriesTable.findAll('tr'):
	items = []
	for td in row.findAll('td'): 
		tdtext = td.get_text().encode('utf8')
		
		# For country names with special characters, Wikipedia includes a hidden version with plain characters followed by an !. We ignore the plain version.
		if '!' in tdtext:
			tdtext = tdtext[(tdtext.find('!') + 1):]		
			
		items.append(tdtext)
		for link in td.findAll('a'):
			print(link.get('href'))
			items.append(urllib2.unquote(link.get('href').encode('utf8')))		# Contortions required here to handle special characters
	report.append(items)

# Write output CSV file	
header = ['Code', 'Name', 'Country-link', 'Year', 'TLD', 'TLD-link', 'Group', 'Group-link', 'Notes']
with open('countries.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for row in report:
		writer.writerow(row[0:9])		# Write first 9 columns only

	
