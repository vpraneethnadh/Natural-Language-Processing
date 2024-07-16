import spacy

nlp = spacy.load("en_core_web_sm")

document = """
Barack Obama was born in Hawaii. He was the 44th President of the United States.
"""

doc = nlp(document)

named_entities_relations = []
for ent in doc.ents:
    named_entities_relations.append((ent.text, ent.root.dep_, ent.root.head.text, ent.root.head.pos_))

print("Named Entities and their Relations:")
for entity, dep, head, head_pos in named_entities_relations:
    print(f"{entity} -> Dependency: {dep}, Head: {head}, Head POS: {head_pos}")
