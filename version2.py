from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.marketwatch.com/tools/marketsummary').text

soup = BeautifulSoup(source, 'lxml')

Market_summary = soup.find('table', {'id':'marketsummaryindexes'})

Indicies = []
Last = []
Change = []
Percent_Change = []

Tablelines = Market_summary.findAll('a')
Lasts = Market_summary.findAll('td', class_='aright bottomborder negativearrow bgLast', class_='aright bottomborder positivearrow bgLast')
Changes = Market_summary.findAll('td', class_='aright bottomborder chg-col negative bgChange', class_='aright bottomborder chg-col positive bgChange')
Percent_Changes = Market_summary.findAll('td', class_='aright bottomborder perc-col negative bgPercentChange', class_='aright bottomborder perc-col positive bgPercentChange')

for member0 in Tablelines:
	Indicies.append(member0.get('title'))

for member1 in Lasts:
	Last.append(member1.text)
	
for member2 in Changes:
	Change.append(member2.text)

for member3 in Percent_Changes:
	Percent_Change.append(member3.text)	


"""
print(Indicies)
print(Last)
print(len(Indicies))
print(len(Last))
print(len(Change))
print(len(Percent_Change))
"""