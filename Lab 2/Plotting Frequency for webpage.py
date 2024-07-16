import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import matplotlib.pyplot as plt

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


def plot_word_frequency(freq_dist):
    plt.figure(figsize=(12, 6))
    freq_dist.plot(20, cumulative=False)
    plt.title('Word Frequency Distribution')
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    plt.show()


url = 'https://www.google.co.in/'
word_frequency = extract_words_and_frequency(url)
plot_word_frequency(word_frequency)
