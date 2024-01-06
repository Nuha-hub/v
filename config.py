from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os
APP_ID = 29936425
APP_HASH = '5f6899b4bd1018f935f1b9a088bbd0dd'
BOT_USERNAME = 'X4jbbot'
session = 'MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigv0/vBfyy7mx66W0/s0Fa7/1mAZtEoIokDP3ShoqF4fVNb6XeqgplUUI1PLTktZ9uW2WE23b+ixNwJjJGwBDJPQEQFBE+vfj25sIWeYPHYeOrFp/eXaqhISP6G+q2IeTaWTXpwZj4LzaHWfYmlEGepfaYR8Q0YqvvhYtMte3ITnuSJs171+GDqpqACJLZtS7QMgCGXJ6XIRQfaUHd8wJpDWHCR20FwvmH0JP503wr5INS1powg/Xq5YOpk4bYEQ6mvRq7D1dkcSwHnd6FudwG04pcC0j4WcDuXc2CTHgH8gFTNhp/Y8/SpD0hvn9QIDAQAB'
SESSION = 'MIIBCgKCAQEAyMEdY1aR+sCR3ZSJrtztKTKqigv0/vBfyy7mx66W0/s0Fa7/1mAZtEoIokDP3ShoqF4fVNb6XeqgplUUI1PLTktZ9uW2WE23b+ixNwJjJGwBDJPQEQFBE+vfj25sIWeYPHYeOrFp/eXaqhISP6G+q2IeTaWTXpwZj4LzaHWfYmlEGepfaYR8Q0YqvvhYtMte3ITnuSJs171+GDqpqACJLZtS7QMgCGXJ6XIRQfaUHd8wJpDWHCR20FwvmH0JP503wr5INS1powg/Xq5YOpk4bYEQ6mvRq7D1dkcSwHnd6FudwG04pcC0j4WcDuXc2CTHgH8gFTNhp/Y8/SpD0hvn9QIDAQAB'
token = '6634930535:AAHTM6VQQuZZTZ9mQfWgb-0qSmm-DePQqOI'
Dasthon = TelegramClient(StringSession(session), APP_ID, APP_HASH)
bot = TelegramClient("bot", APP_ID, APP_HASH).start(bot_token=token)
ispay = ['yes']
ispay2 = ['yes']
bot.start()
