from AudioFile import *

class OGGFile(AudioFile):
	def __init__(self, filename):
		AudioFile.__init__(self, filename, 'OGG')

	def play(self):
		print 'Playing OGG file'