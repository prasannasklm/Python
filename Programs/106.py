#import nltk
#from nltk.corpus import stopwords
s="hello the here the program is about @removing the stopwords by importing the library"
word=s.split()
word=word.split('@')
print(word)
