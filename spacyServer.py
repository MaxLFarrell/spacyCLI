import spacy.en
from spacy.parts_of_speech import *

def main(sentence)
	nlp = spacy.en.English()
	tokens = nlp(u"{0}".format(sentence), tag=True, parse=False)
	tokList = []
	tokPosList = []
	for tok in tokens:
		print(tok.string)
		tokList.append(tok.string)
		print(tok.pos_)
		tokPosList.append(tok.pos_)
	return (''.join(tokPosList))
