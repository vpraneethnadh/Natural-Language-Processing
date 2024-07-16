import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')


def remove_stopwords_and_rarewords_from_file():
    with open('TextFile.txt', 'r', encoding='utf-8') as file:
        document = file.read()
    tokens = word_tokenize(document)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    freq_dist = FreqDist(filtered_tokens)
    rare_word_threshold = 1
    filtered_tokens = [token for token in filtered_tokens if freq_dist[token] > rare_word_threshold]
    return filtered_tokens


processed_tokens = remove_stopwords_and_rarewords_from_file()
print('Processed Tokens:', processed_tokens)
