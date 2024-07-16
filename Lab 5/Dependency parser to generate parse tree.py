import spacy

nlp = spacy.load('en_core_web_sm')
sentence = "The quick brown fox jumps over the lazy dog."
doc = nlp(sentence)

print("Dependency Parsing:")
for token in doc:
    print(token.text, token.dep_, token.head.text)
