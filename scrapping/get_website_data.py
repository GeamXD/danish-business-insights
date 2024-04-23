import requests
from bs4 import BeautifulSoup
import json

# Function to scrape data from a given URL
def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract relevant data from the webpage
        # Example: Extract all text from <p> tags
        paragraphs = soup.find_all('p')
        data = [p.get_text(strip=True) for p in paragraphs]
        
        # Create a dictionary to store the data
        result = {
            "url": url,
            "data": data
        }
        
        return result
    else:
        print("Failed to retrieve data from:", url)
        return None

# List of URLs to scrape
urls = [
    "https://ampliqon.com/en/contact/general-contact-info/",
    "https://ampliqon.com/en/contact/technical-support/",
    "https://ampliqon.com/en/contact/where-to-find-us/",
    "https://ampliqon.com/en/ampliqon/our-mission-and-vision/",
    "https://ampliqon.com/en/ampliqon/about-us/"
]

# List to store scraped data
scraped_data = []

# Iterate over each URL and scrape data
for url in urls:
    data = scrape_data(url)
    if data:
        scraped_data.append(data)

# Write the scraped data to a JSON file
with open("scraped_data.json", "w") as json_file:
    json.dump(scraped_data, json_file, indent=4)

print("Data saved to scraped_data.json")