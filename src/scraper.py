# %% [markdown]
# # Imports

# %%
from bs4 import BeautifulSoup
from time import sleep
import requests
import time
import json
from random import randint
from html.parser import HTMLParser
USER_AGENT = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

# %% [markdown]
# # Search Class

# %%
class SearchEngine:
    @staticmethod
    def search(query, sleep=True):
        if sleep: # Prevents loading too many pages too soon
            time.sleep(randint(10, 100))
        temp_url = '+'.join(query.split()) #for adding + between words for the query
        url = 'http://www.ask.com/web?q=' + temp_url
        soup = BeautifulSoup(requests.get(url, headers=USER_AGENT).text,"html.parser")
        new_results = SearchEngine.scrape_search_result(soup)
        return new_results
    
    @staticmethod
    def scrape_search_result(soup):
        raw_results = soup.find_all("a", attrs={"class": "PartialSearchResults-item-title-link result-link"})
        results = []

        for result in raw_results:
            link = result.get('href')
            results.append(link)
        return list(set(results))[:10]

# %% [markdown]
# # Queries

# %%
with open("100QueriesSet3.txt") as file:
    queries = [line.strip() for line in file.readlines()]

# %%
query_data = dict()
task = SearchEngine()

for itr, query in enumerate(queries):
    query_data[query] = task.search(query)
    print(itr)

# %%
len(query_data)

# %%
with open("results.json", "w") as file:
    json.dump(query_data, file, indent=2)


