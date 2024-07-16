import nltk
from nltk.corpus import treebank
from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize

nltk.download('treebank')
nltk.download('punkt')


def regex_tagger(train_data, test_data):
    patterns = [
        (r'.*ing$', 'VBG'),
        (r'.*ed$', 'VBD'),
        (r'\b(?:is|am|are)\b', 'VB'),
        (r'\b(?:a|an|the)\b', 'DT'),
        (r'\b(?:\d+\.\d+|\d+)\b', 'CD'),
    ]

    regex_tagger = RegexpTagger(patterns)
    accuracy_regex = regex_tagger.evaluate(test_data)
    print(f'Regex Tagger Accuracy: {accuracy_regex * 100:.2f}%')

    return regex_tagger


treebank_data = treebank.tagged_sents()
train_size = int(0.8 * len(treebank_data))
train_data = treebank_data[:train_size]
test_data = treebank_data[train_size:]
regex_tagger_model = regex_tagger(train_data, test_data)
new_text = "This is an example sentence."
tokens = word_tokenize(new_text)
regex_tags = regex_tagger_model.tag(tokens)
print('\nTagged Words (Regex Tagger):', regex_tags)
