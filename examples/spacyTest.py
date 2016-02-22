import spacy.en
from spacy.parts_of_speech import ADV

nlp = spacy.en.English()
tokens = nlp(u"'Give it back,' he pleaded abjectly, 'it's mine.'", tag=True, parse=False)
print (u''.join(tok.string.upper() if tok.pos == ADV else tok.string for tok in tokens))
