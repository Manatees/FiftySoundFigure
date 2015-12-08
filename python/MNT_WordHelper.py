#coding=utf-8
import codecs
import MNT_Word
import random


class WordHelper:
	'''Helper object for word'''

	dicHToK = {}
	dicKToH = {}
	dicIToH = {}
	dicIToK = {}
	dicIToR = {}
	wordList = []
	
	#清音
	aLine = ("A", "I", "U", "E", "O")
	kaLine = ("KA", "KI", "KU", "KE", "KO")
	saLine = ("SA", "SI", "SU", "SE", "SO")
	taLine = ("TA", "CHI", "TU", "TE", "TO")
	naLine = ("NA", "NI", "NU", "NE", "NO")
	haLine = ("HA", "HI", "FU", "HE", "HO")
	maLine = ("MA", "MI", "MU", "ME", "MO")
	yaLine = ("YA", "I", "YU", "E", "YO")
	raLine = ("RA", "RI", "RU", "RE", "RO")
	waLine = ("WA", "I", "U", "E", "WO")
	
	#拨音
	nLine = ("N")
	#浊音
	gaLine = ("GA", "GI", "GU", "GE", "GO")
	zaLine = ("ZA", "JI", "ZU", "ZE", "ZO")
	daLine = ("DA", "DI", "DU", "DE", "DO")
	baLine = ("BA", "BI", "BU", "BE", "BO")
	#半浊音
	paLine = ("PA", "PI", "PU", "PE", "PO")
	#拗音
	kyaLine = ("KYA", "KYU", "KYO")
	shaLine = ("SHA", "SHU", "SHO")
	chaLine = ("CHA", "CHU", "CHO")
	nyaLine = ("NYA", "NYU", "NYO")
	hyaLine = ("HYA", "HYU", "HYO")
	myaLine = ("MYA", "MYU", "MYO")
	ryaLine = ("RYA", "RYU", "RYO")
	gyaLine = ("GYA", "GYU", "GYO")
	jaLine = ("JA", "JU", "JO")
	byaLine = ("BYA", "BYU", "BYO")
	pyaLine = ("PYA", "PYU", "PYO")
	
	wordTable = (aLine, kaLine, saLine, taLine, naLine, haLine, maLine, yaLine, raLine, waLine, nLine, gaLine, zaLine, daLine, baLine, paLine, kyaLine, shaLine, chaLine, nyaLine, hyaLine, myaLine, ryaLine, gyaLine, jaLine, byaLine, pyaLine)
	
	def load(self):
		fobj = codecs.open("../data/word50.dat", "r", "utf-8")
		#allContent = fobj.readlines()
		for line in fobj.readlines():
			line = line.strip()
			lines = line.split(":")
			aWord = MNT_Word.Word(lines)
			self.wordList.append(aWord)
			H = lines[0]
			K = lines[1]
			R = lines[2]
			keyCode = lines[3]
			self.dicHToK[H] = K
			self.dicKToH[K] = H
			self.dicIToH[keyCode] = H
			self.dicIToK[keyCode] = K
			self.dicIToR[keyCode] = R
		
	def wordTable50(self):
		for row in self.wordTable:
			self.out_p([self.dicIToH[i] for i in row])
			print
	
	def wordTable50_Katakana(self):
		for row in self.wordTable:
			self.out_p([self.dicIToK[i] for i in row])
			print
	
	def wordTable50_HK(self):
		for row in self.wordTable:
			self.out_p(["%s[%s]"%(self.dicIToH[i], self.dicIToK[i]) for i in row])
			print
	
	QA = {}
	def question(self):
		self.QA = {}
		for i in range(5):
			rnd  = random.choice(self.wordList)
			if random.randint(0, 1) == 1:
				self.QA[rnd.katakana] = rnd
			else:
				self.QA[rnd.hiragana] = rnd
		self.out_p(self.QA.keys())
	
	def answer(self):
		for i in self.QA:
			word = self.QA[i]
			print word.hiragana, word.katakana, word.roma
		
	
	def out_p(self, arr):
		for i in arr:
			print i,
	
	
