import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')


def extract_words_and_frequency(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    text_content = soup.get_text()
    tokens = word_tokenize(text_content)
    words = [word.lower() for word in tokens if word.isalpha()]
    freq_dist = FreqDist(words)

    return freq_dist


url = 'https://www.google.co.in/'
word_frequency = extract_words_and_frequency(url)

for word, frequency in word_frequency.items():
    print(f'{word}: {frequency}')
