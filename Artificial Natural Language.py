import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPuncttokenizer

larger = "We use the method word_tokenize() to split a sentence into words. "
print(sent_tokenize(larger))
print(word_tokenize(larger))
print(WordPuncttokenizer())