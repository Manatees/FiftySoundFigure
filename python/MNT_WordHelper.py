#code=utf-8
import codecs
import MNT_Word

class WordHelper:
	'''Helper object for word'''

	dicHToK = {}
	dicKToH = {}
	dicRToH = {}
	dicRToK = {}
	#wordList = []
	
	def load(self):
		fobj = codecs.open("../data/word50.dat", "r", "utf-8")
		#allContent = fobj.readlines()
		for line in fobj.readlines():
			line = line.strip()
			lines = line.split(":")
			aWord = MNT_Word.Word(lines)
			self.wordList.append(aWord)
		
	def showSome(self):
		print self.wordList[0]