import nltk

grammar = r"""
    NP: {<Det>?<N>}
    PP: {<P><NP>}
    VP: {<V><NP>}
    S: {<NP><VP>}
"""

parser = nltk.RegexpParser(grammar)
sentence = [('the', 'Det'), ('cat', 'N'), ('eats', 'V'), ('a', 'Det'), ('dog', 'N')]
parsed_tree = parser.parse(sentence)

for tree in parsed_tree:
    print(tree)
