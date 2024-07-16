import nltk
from nltk.tag import UnigramTagger, BigramTagger, TrigramTagger
from nltk.corpus import treebank

nltk.download('treebank')

treebank_data = treebank.tagged_sents()
train_size = int(0.8 * len(treebank_data))
train_data = treebank_data[:train_size]
test_data = treebank_data[train_size:]

unigram_tagger = UnigramTagger(train_data)
accuracy_unigram = unigram_tagger.evaluate(test_data)
print(f'Unigram Tagger Accuracy: {accuracy_unigram * 100:.2f}%')

bigram_tagger = BigramTagger(train_data, backoff=unigram_tagger)
accuracy_bigram = bigram_tagger.evaluate(test_data)
print(f'Bigram Tagger Accuracy: {accuracy_bigram * 100:.2f}%')

trigram_tagger = TrigramTagger(train_data, backoff=bigram_tagger)
accuracy_trigram = trigram_tagger.evaluate(test_data)
print(f'Trigram Tagger Accuracy: {accuracy_trigram * 100:.2f}%')
