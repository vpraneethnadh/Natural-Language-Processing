import nltk
from nltk.corpus import treebank
from nltk.tag import RegexpTagger
from nltk.tokenize import word_tokenize
from nltk.classify import MaxentClassifier
import random

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

def document_features(document):
    document_words = set(document.split())
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

treebank_data = treebank.tagged_sents()
train_size = int(0.8 * len(treebank_data))
train_data = treebank_data[:train_size]
test_data = treebank_data[train_size:]
regex_tagger_model = regex_tagger(train_data, test_data)

new_text = "This is an example sentence."
tokens = word_tokenize(new_text)
regex_tags = regex_tagger_model.tag(tokens)
print('\nTagged Words (Regex Tagger):', regex_tags)

sentences = [
    ("This is a positive sentence", "positive"),
    ("I don't like this negative statement", "negative"),
]

random_sentence, random_label = random.choice(sentences)
all_words = set(word.lower() for sentence, _ in sentences for word in sentence.split())
word_features = list(all_words)
featuresets = [(document_features(random_sentence), random_label)]
classifier = MaxentClassifier.train(featuresets, algorithm='gis', max_iter=10)
predicted_label = classifier.classify(document_features(random_sentence))
print("Random Sentence:", random_sentence)
print("True Label:", random_label)
print("Predicted Label:", predicted_label)
