# filename: search_engine_api_query.py
import requests

def search_using_api(search_query, api_key):
    api_endpoint = 'https://api.example.com/search'
    headers = {'Authorization': f'Bearer {api_key}'}
    params = {'q': search_query, 'format': 'json'}
    
    response = requests.get(api_endpoint, headers=headers, params=params)
    response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
    
    return response.json()

# Replace 'your_api_key' with the actual API key provided by the search engine
api_key = 'your_api_key'
search_query = 'SEL 810A'

# Perform the search and print the results
search_results = search_using_api(search_query, api_key)
print(f"Search results for '{search_query}':")
for result in search_results.get('items', []):
    print(result.get('title'), result.get('link'))