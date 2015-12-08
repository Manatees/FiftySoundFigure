#coding=utf-8


class Word:
	'''
	平假名hiragana
	片假名katakana
	罗马音roma
	类型type=(清音、拨音、浊音、半浊音、拗音)
	音频audio
	输入法inputCode
	'''
	hiragana = ""
	katakana = ""
	roma = ""
	type = ""
	audio = ""
	inputCode = ""


	def __init__(self, param):
		self.hiragana = param[0]
		self.katakana = param[1]
		self.roma = param[2]
		self.type = ""
		self.audio = ""
		self.inputCode = param[3]

	def detail(self):
		return (self.hiragana, self.katakana, self.roma, self.inputCode)