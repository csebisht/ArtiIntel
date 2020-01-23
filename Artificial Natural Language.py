import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

#https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_nltk_package.htm
larger = "We use the method word_tokenize() to split a sentence into words. "
print(sent_tokenize(larger))
print(word_tokenize(larger))
sentence=[("a","DT"),("clever","JJ"),("fox","NN"),("was","VBP"),
          ("jumping","VBP"),("over","IN"),("the","DT"),("wall","NN")]
grammar = "NP:{<DT>?<JJ>*<NN>}"
parser_chunking = nltk.RegexpParser(grammar)
parser_chunking.parse(sentence)
Output_chunk = parser_chunking.parse(sentence)
Output_chunk.draw()