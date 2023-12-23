# filename: web_scraping_search.py
import requests
from bs4 import BeautifulSoup

def search_web_for_info(search_query, search_url):
    response = requests.get(search_url)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    
    # Assuming the website uses UTF-8 encoding; adjust if necessary
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # The following line is a placeholder. The actual search will depend on the structure of the website and the HTML tags.
    search_results = soup.find_all(text=lambda text: search_query in text)
    
    return search_results

# Replace 'http://example.com/search' with the actual URL of the search page
search_url = 'http://example.com/search'
search_query = 'SEL 810A'

# Perform the search and print the results
search_results = search_web_for_info(search_query, search_url)
print(f"Information related to '{search_query}' found on the web page:")
for result in search_results:
    print(result)