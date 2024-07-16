import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
import re

nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')


def date_money_tagger(sentence):
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)

    date_pattern = r'\d{1,4}[-/]\d{1,2}[-/]\d{1,4}'
    money_pattern = r'\$?\d+(,\d{3})*(\.\d{2})?'

    date_matches = [(match.group(), 'DATE') for match in re.finditer(date_pattern, sentence)]
    money_matches = [(match.group(), 'MONEY') for match in re.finditer(money_pattern, sentence)]
    combined_tags = pos_tags + date_matches + money_matches
    ner_tags = ne_chunk(combined_tags)

    return ner_tags

example_sentence = "I have a meeting on 2022-02-20 and need $500 for it."
tagged_sentence = date_money_tagger(example_sentence)
print("Tagged Sentence:")
print(tagged_sentence)
