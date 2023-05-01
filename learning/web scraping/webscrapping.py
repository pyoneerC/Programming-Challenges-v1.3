import requests
import re
import json
from bs4 import BeautifulSoup


url = "https://www.example.com"
response = requests.get(url)

print(f'STATUS CODE: {response.status_code}')
print(f'SOURCE CODE:{response.text}')

# Make a GET request to the URL
response = requests.get(url)

# Use Beautiful Soup to parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find the title of the page
title = soup.find('title').get_text()
print(f'Title: {title}')

# Find all of the links on the page
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.get_text()
    print(f'{text}: {href}')

# Find all of the images on the page
images = soup.find_all('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    print(f'{alt}: {src}')

# Find all of the headings on the page
headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
for heading in headings:
    text = heading.get_text()
    print(f'Heading: {text}')

# Find all of the paragraphs on the page
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    text = paragraph.get_text()
    print(f'Paragraph: {text}')

# Send a GET request to the URL and get its content
url = 'https://www.example.com'
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Find the page title
title = soup.title.string
print('Page Title:', title)

# Find all links on the page and print their href attributes
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    print('Link:', href)

# Find all images on the page and print their src attributes
images = soup.find_all('img')
for image in images:
    src = image.get('src')
    print('Image:', src)

# Use regular expressions to find all email addresses on the page
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
emails = re.findall(email_regex, str(html_content))
print('Emails:', emails)

# Use regular expressions to find all phone numbers on the page
phone_regex = r'\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(phone_regex, str(html_content))
print('Phone Numbers:', phone_numbers)

# Use json module to parse JSON data on the page
json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print('JSON Data:', data)