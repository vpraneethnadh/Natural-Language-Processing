import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> 'Mary' | Det N | Det N PP
    VP -> V | V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'park' | 'dog'
    V -> 'saw'
    P -> 'in'
""")

sentence = ['Mary', 'saw', 'a', 'dog', 'in', 'the', 'park']


def leftmost_derivation(grammar, sentence):
    for production in nltk.ChartParser(grammar).parse(sentence):
        print(production)


def rightmost_derivation(grammar, sentence):
    for production in nltk.RecursiveDescentParser(grammar).parse(sentence):
        print(production)


print("Left Most Derivation:")
leftmost_derivation(grammar, sentence)
print()

print("Right Most Derivation:")
rightmost_derivation(grammar, sentence)
