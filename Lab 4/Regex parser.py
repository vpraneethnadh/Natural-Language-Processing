import re

sentence = "This is an example sentence."
noun_pattern = re.compile(r'\b[A-Z][a-z]*\b')
nouns = noun_pattern.findall(sentence)
print("Nouns:", nouns)
