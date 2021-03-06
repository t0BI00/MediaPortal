#	-*-	coding:	utf-8	-*-

from Plugins.Extensions.MediaPortal.resources.simpleplayer import SimplePlayer
from Plugins.Extensions.MediaPortal.resources.youtubelink import YoutubeLink

class YoutubePlayer(SimplePlayer):

	def __init__(self, session, playList, playIdx=0, playAll=False, listTitle=None, plType='local', title_inr=0):
		print "YoutubePlayer:"
		
		SimplePlayer.__init__(self, session, playList, playIdx=playIdx, playAll=playAll, listTitle=listTitle, plType=plType, title_inr=title_inr, ltype='youtube')
		
	def getVideo(self):
		print "getVideo:"
		dhTitle = self.playList[self.playIdx][self.title_inr]
		dhVideoId = self.playList[self.playIdx][2]
		YoutubeLink(self.session).getLink(self.playStream, self.dataError, dhTitle, dhVideoId)
		
