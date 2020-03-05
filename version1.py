import pandas as pd
from bs4 import BeautifulSoup
import requests
import re

source = requests.get('https://www.marketwatch.com/tools/marketsummary').text

soup = BeautifulSoup(source, 'lxml')

table = soup.tbody #.find('tr', {'class':'bgQuote'})

#info = table.find_all('tr', class_='bgQuote')
#see how the line number 10 works but not the above thats been commented out!!!
#unms_hope = table.find_all('td')

"""
print(table.prettify())
name = table.a['title']
print(name)
"""
#for nums in table.find_all(re.compile("^td")):
#	print(nums)

mega_list = []
for strin in table.stripped_strings:
	mega_list.append(strin)

#print(mega_list)
"""
exclude = re.compile(r'/zigman2/(.*)')
filtered = filter(lambda i: not exclude.search(i), mega_list)
"""
info = []

for exclude in mega_list:
	if exclude[0] != '/':
		info.append(exclude)

#print(info)
"""
Indicies = []
Last = []
Change = []
Percent_Change = []
"""

df = pd.DataFrame(info)

print(df)

"""
i = 0
while(i != len(info)):
	if i == 0:
		#add name
		Indicies.append(info[i])
		i+=1
	if i == 1:
		#add last
		Last.append(info[i])
		i+=1
	if i == 2:
		#add chang
		Change.append(info[i])
		i+=1
	if i == 3:
		#add perc_cha
		Percent_Change.append(info[i])
	i = 0

print(Indicies)
print(Last)
print(Change)
print(Percent_Change)
"""