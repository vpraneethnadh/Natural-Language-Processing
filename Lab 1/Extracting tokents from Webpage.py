import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')


def extract_tokens_from_webpage(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()
    tokens = word_tokenize(text_content)
    return tokens


url = 'https://www.google.co.in/'
tokens = extract_tokens_from_webpage(url)
for token in tokens:
    print(token)
