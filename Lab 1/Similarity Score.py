from difflib import ndiff
from nltk.metrics import jaccard_distance
from nltk import ngrams


def jaccard_index(sentence1, sentence2):
    set1 = set(ngrams(sentence1, 1))
    set2 = set(ngrams(sentence2, 1))
    return 1 - jaccard_distance(set1, set2)


def edit_distance(sentence1, sentence2):
    diff = list(ndiff(sentence1, sentence2))
    return diff.count(' ') / max(len(sentence1), len(sentence2))


sentence1 = input("Enter the first sentence: ").lower().split()
sentence2 = input("Enter the second sentence: ").lower().split()

jaccard_score = jaccard_index(sentence1, sentence2)
print(f"Jaccard Index: {jaccard_score}")

edit_distance_score = edit_distance(sentence1, sentence2)
print(f"Edit Distance: {edit_distance_score}")

if jaccard_score > edit_distance_score:
    print("Jaccard Index is more efficient for measuring similarity.")
elif jaccard_score < edit_distance_score:
    print("Edit Distance is more efficient for measuring similarity.")
else:
    print("Both methods provide the same level of efficiency for measuring similarity.")
