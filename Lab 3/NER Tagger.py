import nltk
from nltk import ne_chunk
from nltk.tokenize import word_tokenize

nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt')

new_sentence = "This is an example sentence."
tokens = word_tokenize(new_sentence)
pos_tags = nltk.pos_tag(tokens)
ner_tags = ne_chunk(pos_tags)
print("Named Entities:")
for entity in ner_tags:
    if isinstance(entity, tuple):
        print(entity)
    else:
        print(f"Entity: {' '.join([word for word, _ in entity.leaves()])}, Label: {entity.label()}")
