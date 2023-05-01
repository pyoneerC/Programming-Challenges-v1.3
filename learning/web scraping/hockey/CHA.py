import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.scrapethissite.com/pages/forms/?page_num=24'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with the class 'table'
table = soup.find('table', {'class': 'table'})

# Get all the rows in the table
rows = table.find_all('tr')

# Open the existing CSV file in append mode
with open('C:\\Users\\user\\Desktop\\prog chall py\\learning\\web scrapping\\hockey.csv', mode='a', newline='') as file:
    writer = csv.writer(file)

    # Loop through each row and extract the data from the columns
    for row in rows[1:]:
        columns = row.find_all('td')
        data = [column.get_text(strip=True) for column in columns]
        writer.writerow(data)