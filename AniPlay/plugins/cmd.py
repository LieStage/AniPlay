from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.ErrorHandler import CMDErrorHandler  
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button1 = InlineKeyboardButton(text="OWNER👨🏻‍💻", url="https://t.me/fligher") 
button2 = InlineKeyboardButton(text="CHANNEL🧿", url="https://t.me/movie_time_botonly") 
keyboard_inline = InlineKeyboardMarkup().add(button1, button2) 



@app.on_message(filters.command(["start", "ping", "help", "alive"]))
@CMDErrorHandler
async def start(_, message: Message):
    try:
        await message.reply_photo("https://graph.org/file/d2d4bec6d5a46b27724af.jpg",caption=
            "Bot Is Online...\n\nYou Can Search Animes\n Click /use ",reply_markup=keyboard_inline
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
            f"{QUERY.format(query)}\n\n© {message.from_user.mention}",
            reply_markup=button,reply_markup=keyboard_inline,
        )
    except Exception as e:
        print(e)
        try:
            return await message.reply_photo("https://graph.org/file/a818157c0c880e6863ef0.jpg",caption=
                "**Anime Not Found...**\n\nProbably Incorrect Name, Try again"
            )
        except:
            return


@app.on_message(filters.command(["report"]))
@CMDErrorHandler
async def reportCMD(_, message: Message):
    await message.reply_photo("https://graph.org/file/e93e046cdc24a803990d1.jpg",caption="Report Bugs Here: @TRUMBOTS")

@app.on_message(filters.command(["use"]))
@CMDErrorHandler
async def reportCMD(_, message: Message):
    await message.reply_photo("https://www.shutterstock.com/image-vector/young-man-anime-style-character-600nw-2313503433.jpg",caption="Hi i am Only Provide Animes Here \n 🕳️@animeonlyda")
