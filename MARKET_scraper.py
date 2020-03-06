from bs4 import BeautifulSoup #using beautiful soup 4 to scrape
import requests	#used to access/ge the website

source = requests.get('https://www.marketwatch.com/tools/marketsummary').text #grabbing the text of the entire website

soup = BeautifulSoup(source, 'lxml') #chose the lxml parser

table = soup.tbody #acessing the table tag gives acess to market summary

with open('OUTput.text', 'w') as f:		 #choose to write to txt file, could have dones various formattings: csv, excel...
	for strin in table.stripped_strings: #.stripped_strings removes the excess white spaces 
		if (strin[0] != '/'):			 #removes this bogus information string "/zigman2/quotes...""
			f.write("%s\n" % strin)		 #executed at 7:08 pm est




