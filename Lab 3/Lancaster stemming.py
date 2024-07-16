import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import LancasterStemmer

nltk.download('punkt')


def tokenize_and_lancaster_stem(input_text):
    tokens = word_tokenize(input_text)
    stemmer = LancasterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]

    return tokens, stemmed_tokens


input_text = "This is a sample input string. It contains multiple words that will be tokenized and Lancaster stemmed."

tokens, stemmed_tokens = tokenize_and_lancaster_stem(input_text)
print('Original Tokens:', tokens)
print('\nLancaster Stemmed Tokens:', stemmed_tokens)
