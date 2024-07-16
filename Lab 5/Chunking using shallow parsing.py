import nltk

sentence = "The brown fox is quick and he is jumping over the lazy dog"
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

chunk_grammar = r"""
    NP: {<DT>?<JJ>*<NN>}
    VP: {<VB.*><DT>?<JJ>*<NN|NNS>}
"""

chunk_parser = nltk.RegexpParser(chunk_grammar)
chunked = chunk_parser.parse(pos_tags)
print(chunked)
