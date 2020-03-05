from bs4 import BeautifulSoup
import requests
import pandas as pd

source = requests.get('https://www.marketwatch.com/tools/marketsummary').text

soup = BeautifulSoup(source, 'lxml')

Market_summary = soup.find('table', {'id':'marketsummaryindexes'})


"""
infolines = Market_summary.findAll('title')
for names in infolines:
	names.append(infolines.findAll('title'))
"""

#print(Market_summary)

hegemons = []
important_names = Market_summary.findAll('a')

#numbers = Market_summary.findAll('td')

#print(numbers)

#print(important_names)
"""
for hegemon in important_names:
	hegemons.append(hegemon.get('title'))
print(hegemons)
"""

Last = Market_summary.findAll('td', class_='aright bottomborder negativearrow bgLast')
Change = Market_summary.findAll('td', class_='aright bottomborder chg-col negative bgChange')
Percent_Change = Market_summary.findAll('td', class_='aright bottomborder perc-col negative bgPercentChange')

#print(first_numbers)
#for numberss in first_numbers:
#	print(numberss.text)

"""
Indicies = []
Last = []
Change = []
Percent_Change = []

for index in Tablelines:
	Indicies.append(index.get('title'))
"""
print(Market_summary)