import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')


def split_sentences_from_file():
    with open('TextFile.txt', 'r', encoding='utf-8') as file:
        document = file.read()

    sentences = sent_tokenize(document)
    return sentences


result = split_sentences_from_file()
for i, sentence in enumerate(result, 1):
    print(f'Sentence {i}: {sentence}')
