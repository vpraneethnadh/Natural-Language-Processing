import nltk
from nltk.parse.generate import generate

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> Det N | Det N PP
  VP -> V | V NP
  PP -> P NP
  Det -> 'the' | 'a'
  N -> 'cat' | 'dog' | 'bird' | 'ball'
  V -> 'chases' | 'eats' | 'loves' | 'hates'
  P -> 'with' | 'on'
""")

sentences = [' '.join(sentence) for sentence in generate(grammar, n=5)]
print("Generated sentences:", sentences)
