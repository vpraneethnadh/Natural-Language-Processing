import nltk
import random
from nltk.classify import MaxentClassifier


def document_features(document):
    document_words = set(document.split())
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features


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
