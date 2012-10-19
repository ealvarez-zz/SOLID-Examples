from AudioFile import *

class WMAFile(AudioFile):
    def __init__(self, filename):
        AudioFile.__init__(self, filename, 'WMA')

    def play(self):
        print 'Playing WMA file'