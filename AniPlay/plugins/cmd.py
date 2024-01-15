from pyrogram.types import Message,InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
import time
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.ErrorHandler import CMDErrorHandler  


@app.on_message(filters.private & filters.command(["start", "ping", "help", "alive"]))
@CMDErrorHandler
async def start(_, message: Message):
    buttons = [
            [
                InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇꜱ', url='https://t.me/movie_time_botonly'),
                InlineKeyboardButton('👁️ ᴀɴɪᴍᴇꜱ', url='https://t.me/animeonlyda')
            ],
            [
                InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', url='https://t.me/fligher'),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    try:
        await message.reply_photo("https://graph.org/file/d2d4bec6d5a46b27724af.jpg",caption=
            """𝑯𝒊 𝑰 𝒂𝒎 𝑨𝑵𝑰𝑴𝑬♨︎_♨︎ 𝑺𝒆𝒂𝒓𝒄𝒉 𝑩𝒐𝒕  \n𝑰 𝑪𝒂𝒏 𝑷𝒓𝒐𝒗𝒊𝒅𝒆 𝑨𝒏𝒊𝒎𝒆𝒔 𝒘𝒊𝒕𝒉 𝑺𝒕𝒓𝒆𝒂𝒎😄 𝒂𝒏𝒅 𝑫𝒐𝒘𝒏𝒍𝒂𝒐𝒅📥 𝑶𝒑𝒕𝒊𝒐𝒏 \n 𝑪𝒍𝒊𝒄𝒌 /use""",reply_markup=reply_markup
        )
    except:
        return

QUERY = "**Search Results:** `{}`"


@app.on_message(filters.group & filters.command(["search", "s"]))
@CMDErrorHandler
async def searchCMD(_, message: Message):
    try:
        group_id = message.chat.id
        user = message.from_user.id
        # query=message.command
        query = " ".join(message.command[1:])
        if query == "":
            return await message.reply_text("Give me something to search ^_^ like /search animename")
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(
            f"{QUERY.format(query)}\n\n ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ © {message.from_user.mention}",
            reply_markup=button,
        )
        
    except Exception as e:
        print(e)
        try:
            return await message.reply_photo("https://graph.org/file/a818157c0c880e6863ef0.jpg",caption=
                "**Anime Not Found...**\n\nProbably Incorrect Name, Try again \n\n Try like One Piece not onepiece"
            )
        except:
            return

#without command '/search' modified by @fligher
@app.on_message(filters.group & filters.incoming & filters.text)
@CMDErrorHandler
async def searchCMD(_, message: Message):
    try:
        group_id = message.chat.id
        user = message.from_user.id
        query = "".join(message.text)
        if query == "":
            return await message.reply_text("Give me something to search ^_^ like one piece,jujutsu kaisen,naruto")
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        res = await message.reply_text(
            f"{QUERY.format(query)}\n\n ʀᴇQᴜᴇꜱᴛᴇᴅ ʙʏ © {message.from_user.mention}",
            reply_markup=button,
        )
        time.sleep(5)
        await res.delete()
    except Exception as e:
        print(e)
        try:
            err= await message.reply_photo("https://graph.org/file/a818157c0c880e6863ef0.jpg",caption=
                "**Anime Not Found...**\n\nProbably Incorrect Name, Try again \n\n Try like One Piece not onepiece"
            )
            await err.delete(5)
        except:
            return


#private search restricted
@app.on_message(filters.private & filters.incoming & filters.text)
@CMDErrorHandler
async def searchCMD(_, message: Message):
    await message.reply_text("Ask Animes Only Here @animeonlyda\nDon't Be Silly Bro!!")



#report command
@app.on_message(filters.command(["report"]))
@CMDErrorHandler
async def reportCMD(_, message: Message):
    await message.reply_photo("https://graph.org/file/e93e046cdc24a803990d1.jpg",caption="Report Bugs Here: @TRUMBOTS")

#use command
@app.on_message(filters.command(["use"]))
@CMDErrorHandler
async def reportCMD(_, message: Message):
    buttons = [
            [
                InlineKeyboardButton('👁️ ᴀɴɪᴍᴇꜱ', url='https://t.me/animeonlyda')
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo("https://www.shutterstock.com/image-vector/young-man-anime-style-character-600nw-2313503433.jpg",caption="""𝑰 𝒂𝒎 𝑶𝒏𝒍𝒚 𝑾𝒐𝒓𝒌𝒊𝒏𝒈 𝑶𝒏𝒍𝒚 𝑩𝒆𝒍𝒐𝒘 𝑴𝒆𝒏𝒕𝒊𝒐𝒏𝒆𝒅 𝑮𝒓𝒐𝒖𝒑 📀
    """,reply_markup=reply_markup)


@app.on_message(filters.private & filters.command(["search", "s"]))
@CMDErrorHandler
async def searchCMD(_, message: Message):
    await message.reply_text("Ask Animes Only Here @animeonlyda\nDon't Be Silly Bro!!")


@app.on_message(filters.group & filters.command(["start", "ping", "help", "alive"]))
@CMDErrorHandler
async def start(_, message: Message):
    buttons = [
            [
                InlineKeyboardButton('🤖 ᴜᴘᴅᴀᴛᴇꜱ', url='https://t.me/movie_time_botonly'),
                InlineKeyboardButton('👁️ ᴀɴɪᴍᴇꜱ', url='https://t.me/animeonlyda')
            ],
            [
                InlineKeyboardButton('ℹ️ ʜᴇʟᴘ', url='https://t.me/fligher'),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    try:
        await message.reply_photo("https://graph.org/file/d2d4bec6d5a46b27724af.jpg",caption=
            """𝑯𝒊 𝑰 𝒂𝒎 𝑨𝑵𝑰𝑴𝑬♨︎_♨︎ 𝑺𝒆𝒂𝒓𝒄𝒉 𝑩𝒐𝒕\n 𝑪𝒍𝒊𝒄𝒌 /search animename or /s animename""",reply_markup=reply_markup
        )
    except:
        return
