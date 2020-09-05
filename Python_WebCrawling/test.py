import requests
from bs4 import BeautifulSoup

# 1) request library brings HTML information
# 1-1) HTML data is saved in "res" object

res = requests.get('https://jobs.sap.com/go/SAP-Jobs-in-Korea/943101/') # THE WEB URL in ' '

# check res
#print(res.content)
# 2) HTML page parsing with BeautifulSuop(HTML data, Parsing)
# 2-1) soup = Beautiful(res.content, 'html.parser')
soup = BeautifulSoup(res.content, 'html.parser')

# 3) Search for the data that you want to search
table = soup.find('table')

# 4) get the data and print it
print(table.get_text())