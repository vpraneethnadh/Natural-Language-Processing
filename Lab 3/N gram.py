import nltk
from nltk.corpus import treebank
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger
from nltk.tokenize import word_tokenize

nltk.download('treebank')
nltk.download('punkt')


def ngram_tagger(train_data, test_data):
    unigram_tagger = UnigramTagger(train_data)
    accuracy_unigram = unigram_tagger.evaluate(test_data)
    print(f'Unigram Tagger Accuracy: {accuracy_unigram * 100:.2f}%')

    bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
    accuracy_bigram = bigram_tagger.evaluate(test_data)
    print(f'Bigram Tagger Accuracy: {accuracy_bigram * 100:.2f}%')

    trigram_tagger = TrigramTagger(train_data, backoff=bigram_tagger)
    accuracy_trigram = trigram_tagger.evaluate(test_data)
    print(f'Trigram Tagger Accuracy: {accuracy_trigram * 100:.2f}%')

    return trigram_tagger


treebank_data = treebank.tagged_sents()

train_size = int(0.8 * len(treebank_data))
train_data = treebank_data[:train_size]
test_data = treebank_data[train_size:]

ngram_tagger_model = ngram_tagger(train_data, test_data)

new_text = "This is an example sentence for N-gram tagging."
tokens = word_tokenize(new_text)
tags = ngram_tagger_model.tag(tokens)
print('\nTagged Words:', tags)
