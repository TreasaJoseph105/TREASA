import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt_tab')
text = "tokns using genai"
tokens = word_tokenize(text)
print("Length of tokens:", len(tokens))
print("num of tokens:", tokens)