import spacy.en
from spacy.parts_of_speech import ADV

nlp = spacy.en.English()
tokens = nlp(u"'Give it back,' he pleaded abjectly, 'it's mine.'", tag=True, parse=False)
for tok in tokens:
	if tok.pos == ADV:
		print(tok)
	else:
		pass

