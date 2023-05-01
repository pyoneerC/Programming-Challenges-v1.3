import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.scrapethissite.com/pages/forms/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table with the class 'table'
table = soup.find('table', {'class': 'table'})

# Get all the rows in the table
rows = table.find_all('tr')

# Create a new CSV file to write the data to
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)

    # Extract the column headers
    headers = [header.get_text(strip=True) for header in rows[0].find_all('th')]
    writer.writerow(headers)

    # Loop through each row and extract the data from the columns
    for row in rows[1:]:
        columns = row.find_all('td')
        data = [column.get_text(strip=True) for column in columns]
        writer.writerow(data)