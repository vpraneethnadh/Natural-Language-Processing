import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')


def tokenize_and_stem_from_file():
    with open('TextFile.txt', 'r', encoding='utf-8') as file:
        document = file.read()
    tokens = word_tokenize(document)
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    return tokens, stemmed_tokens


tokens, stemmed_tokens = tokenize_and_stem_from_file()
print('Original Tokens:')
for tokens in tokens:
    print(tokens)

print('\nStemmed Tokens:')
for stemmed_tokens in stemmed_tokens:
    print(stemmed_tokens)
