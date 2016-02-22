import spacy.en
from spacy.parts_of_speech import *

sentence = input("Input sentence: ")
nlp = spacy.en.English()
tokens = nlp(u"{0}".format(sentence), tag=True, parse=False)
for tok in tokens:
	print(tok.string)
	print(tok.pos_)
