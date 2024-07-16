import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')


def tokenize_and_stem(input_text):
    tokens = word_tokenize(input_text)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return tokens, stemmed_tokens


input_text = "This is a sample input string. It contains multiple words that will be tokenized and stemmed."

tokens, stemmed_tokens = tokenize_and_stem(input_text)
print('Original Tokens:', tokens)
print('\nStemmed Tokens:', stemmed_tokens)
