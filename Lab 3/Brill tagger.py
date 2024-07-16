import nltk
from nltk.tag import BrillTaggerTrainer

nltk.download('treebank')
nltk.download('punkt')

treebank_data = nltk.corpus.treebank.tagged_sents()

train_size = int(0.8 * len(treebank_data))
train_data = treebank_data[:train_size]
test_data = treebank_data[train_size:]

baseline_tagger = nltk.UnigramTagger(train_data)

brill_trainer = BrillTaggerTrainer(baseline_tagger, templates=nltk.tag.brill.nltkdemo18())
brill_tagger = brill_trainer.train(train_data, max_rules=10)

new_sentence = "This is an example sentence."
tokens = nltk.word_tokenize(new_sentence)
brill_tags = brill_tagger.tag(tokens)

print('\nTagged Words (Brill Tagger):', brill_tags)
