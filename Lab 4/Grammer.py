import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N | Det N PP
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat' | 'man' | 'woman' | 'park' | 'hill'
    V -> 'chased' | 'saw'
    P -> 'in' | 'on'
""")

parser = nltk.ChartParser(grammar)
for tree in parser.parse(['the', 'dog', 'chased', 'a', 'cat', 'in', 'the', 'park']):
    print(tree)

for tree in parser.parse(['a', 'man', 'saw', 'the', 'woman', 'on', 'the', 'hill']):
    print(tree)
