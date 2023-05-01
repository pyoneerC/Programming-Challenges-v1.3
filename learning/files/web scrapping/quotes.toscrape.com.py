import requests
from bs4 import BeautifulSoup

# Get the page
url = 'http://quotes.toscrape.com/'
response = requests.get(url)

# Parse the page
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the quotes
quotes = soup.find_all('div', class_='quote')[:3]

# Print the quotes and tags
for i, quote in enumerate(quotes):
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    
    # Extract the tags
    tags = quote.find('div', class_='tags').find_all('a', class_='tag')
    tag_list = [tag.text for tag in tags]
    
    # Print the quote, author, and tags
    print(str(i+1) + ". " + author + ": " + text)
    print("   Tags: " + ", ".join(tag_list))