import urllib
import xml.etree.ElementTree as ET
from random import Random
random=Random()
try:
		urlopen=urllib.urlopen
		urlquote=urllib.quote
except:
		urlopen=urllib.request.urlopen
		urlquote=urllib.parse.quote

def getWikimediaImageSearchResults(word, categories=None):
		if not categories:
				categories=["black+and+white+illustrations", "engraved+illustrations"]
		category=random.choice(categories)
		url="https://commons.wikimedia.org/w/index.php?sort=relevance&search=incategory%3A%22"+category+"%22+"+urlquote(word)+"&title=Special%3ASearch&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"
		return ET.fromstring(urlopen(url).read())
def getImageItems(tree):
		return list(map(lambda x: x.getchildren()[0].attrib["src"], list(tree.findall(".//*[@class='image']"))))
def getRandomImage(word):
		try:
				return random.choice(getImageItems(getWikimediaImageSearchResults(word)))
		except:
				return None

