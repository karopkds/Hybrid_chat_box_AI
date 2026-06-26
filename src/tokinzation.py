import nltk
from nltk.tokenize import word_tokenize

def tokenizer(user_response):
    user_response = user_response.lower()

    tokens = word_tokenize(user_response)

    return tokens