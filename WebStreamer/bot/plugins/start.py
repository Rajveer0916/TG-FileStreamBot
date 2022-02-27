# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
 
@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'Hi {m.from_user.mention(style="md")}, Send me a file to get a direct download / stream link. Made with love❤️ by [Adarsh Goel](https://t.me/dc4noob)',
        disable_web_page_preview=True
    )
    
    
@StreamBot.on_message(filters.command(["tos", "report"]))
async def start(_, m: Message):
    await m.reply(
        text='''<b><u>TERMS OF SERVICE / FAIR USE POLICY</u></b> @filetolinkprobot
files sent to bot  are  neither related to this bot nor bot supports the spread. We do not own any of the file available through this bot/website.  unknown users generate the links for  unknown files . If you find the file is inappropriate (porn or copyrighted), please report the file to @dc4noob. Please attach the link and state the reason.
\n <u>Appropriate action will be taken as soon as possible.
We don't tolerate copyright violation of any kind.\n\n
At the end we don't know what people are doing  and we will appreciate if you report so we can take down such unacceptable content.</u>❤️ ''',
        parse_mode="HTML"
    )
