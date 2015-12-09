import MNT_WordHelper
def main():
	aHelper = MNT_WordHelper.WordHelper()
	aHelper.load()
	print 'Question:'
	aHelper.question()
	print
	print 'Answer:'
	aHelper.answer()

if __name__ == '__main__':
	main()

