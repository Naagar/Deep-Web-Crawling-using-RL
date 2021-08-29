# !pip install sentence-transformers
# !pip install huggingface-hub==0.0.12

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))
nltk.download("words")

import requests #for making HTTP requests in Python
from bs4 import BeautifulSoup # pulling data from HTML or XML files


def get_urls(url):
  r = requests.get(url)

  soup = BeautifulSoup(r.text, "html.parser") # Using BeautifulSoup we will parse the web page to extraxt the liks from the page
  # soup
  # print(soup.prettify())

  # Extract the useful liks from list of links
  links = []
  for item1 in soup.find_all('li'):
    for item2 in soup.find_all('a'):
      links.append(item2.get('href'))
  # links </li>
  print(links)


  # Finding the indexed links for Web crawling
  final = []
  for item in links:
    if item != None :
      if len(item) >= 120:
        # stri = item[0:11]
        # if stri == "/vuln/search/":
        final.append(item)
  return final

urls_list = get_urls(initial_url)