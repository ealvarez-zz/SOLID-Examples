from AudioFile import *

class MP3File(AudioFile):
    def __init__(self, filename):
        AudioFile.__init__(self, filename, 'MP3')

    def play(self):
        print 'Playing MP3 file'