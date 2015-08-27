from bs4 import BeautifulSoup
import urllib2
import string
import csv

url = "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"
page = urllib2.urlopen(url)

soup = BeautifulSoup(page.read(), 'html.parser')

countriesTable = None 	# Will store the table after we find it
maxRows = 0				# For finding table with the most rows

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
		items.append(td.get_text().encode('utf8'))
		for link in td.findAll('a'):
			items.append(urllib2.unquote(link.get('href').encode('utf8')))		# Contortions required here to handle special characters
	report.append(items)
	
header = ['Code', 'Name', 'Country-link', 'Year', 'TLD', 'TLD-link', 'Group', 'Group-link', 'Notes']

with open('countries.csv', 'wb') as f:
	writer = csv.writer(f)
	writer.writerow(header)
	for row in report:
		writer.writerow(row[0:9])		# Write first 9 columns only

	
