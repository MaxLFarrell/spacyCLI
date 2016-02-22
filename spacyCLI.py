import urllib.request as urllib2
import urllib

url = 'http://127.0.0.1:9663/?'
sentence = ""
while sentence != "//":
	sentence = input("Input sentence: ")
	url = url+"sentence="+sentence
	print(url)
	content = urllib2.urlopen(url=url).read()
	tokens = int(content.decode('utf-8'))
	print (tokens)