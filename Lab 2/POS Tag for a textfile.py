import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def identify_parts_of_speech():
    with open('TextFile.txt', 'r', encoding='utf-8') as file:
        document = file.read()
    tokens = word_tokenize(document)
    pos_tags = pos_tag(tokens)
    return pos_tags


pos_tags = identify_parts_of_speech()
for token, pos_tag in pos_tags:
    print(f'Token: {token}, POS Tag: {pos_tag}')
