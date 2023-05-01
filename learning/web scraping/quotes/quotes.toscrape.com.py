import requests
from bs4 import BeautifulSoup
import csv

# Get the page
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# Parse the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the quotes
quotes = soup.find_all('div', class_='quote')

# Write the quotes to a CSV file
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'author', 'quote', 'tags'])
    
    for i, quote in enumerate(quotes):
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        
        # Extract the tags
        tags = quote.find('div', class_='tags').find_all('a', class_='tag')
        tag_list = [tag.text for tag in tags]
        
        # Append a dot to the last tag
        if len(tag_list) > 0:
            tag_list[-1] += "."
        
        # Write the quote to the CSV file
        writer.writerow([i+1, author, text, ", ".join(tag_list)])