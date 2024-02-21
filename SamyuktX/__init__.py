from SamyuktX.core.bot import SamyuktX
from SamyuktX.core.dir import dirr
from SamyuktX.core.git import git
from SamyuktX.core.userbot import Userbot
from SamyuktX.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SamyuktX()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
