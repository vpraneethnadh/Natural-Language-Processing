import nltk

sentence = "The quick brown fox jumps over the lazy dog."
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)
grammar = r"""
    NP: {<DT>?<JJ>*<NN>}  # Noun Phrase
    VP: {<VB.*><NP|PP|CLAUSE>+$}  # Verb Phrase
    PP: {<IN><NP>}  # Prepositional Phrase
    CLAUSE: {<NP><VP>}  # Clause
"""

chunk_parser = nltk.RegexpParser(grammar)
chunks = chunk_parser.parse(pos_tags)
print(chunks)
chunks.draw()
