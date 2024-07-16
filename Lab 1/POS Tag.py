import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


def pos_tag_sentence(sentence):
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)
    return pos_tags


input_sentence = input("Enter a sentence: ")
pos_tags = pos_tag_sentence(input_sentence)

print("Word\t\tPOS Tag")
print("------------------------")
for word, pos_tag in pos_tags:
    print(f"{word}\t\t{pos_tag}")
