from nltk import word_tokenize
from nltk.probability import FreqDist

Sentence = """Whenever you feel like criticizing anyone,” he told me, “just
remember that all the people in this world haven’t had the advantages
that you’ve had."""

words = word_tokenize(Sentence)
print("Total Number of words in the sentence is: ",len(Sentence))
Freq = FreqDist(words)
print(Freq.most_common(10))
