class AudioFile(object):
	def __init__(self, filename, filetype):
		self.filename = filename
		self.filetype = filetype

	def play(self):
		if self.filetype == 'MP3':
			self.play_mp3_file()
		elif self.filetype == 'WMA':
			self.play_wma_file()
		elif self.filetype == 'OGG':
			self.play_ogg_file()
	
	def play_mp3_file(self):
		print 'Playing MP3 file'
	
	def play_wma_file(self):
		print 'Playing WMA file'
	
	def play_ogg_file(self):
		print 'Playing OGG file'