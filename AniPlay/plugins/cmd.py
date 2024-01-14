from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.ErrorHandler import CMDErrorHandler  


@app.on_message(filters.command(["start", "ping", "help", "alive"]))
@CMDErrorHandler
async def start(_, message: Message):
    try:
        await message.reply_photo("https://graph.org/file/d2d4bec6d5a46b27724af.jpg",caption=
            "Bot Is Online...\n\nSearch Animes Using /search animename or /s animename"
        )
    except:
        return

QUERY = "**Search Results:** `{}`"


@app.on_message(filters.group)
@CMDErrorHandler
async def searchCMD(_, message: Message):
    try:
        group_id = message.chat.id
        user = message.from_user.id
        query=""
        # query = " ".join(message.command[1:])
        # if query == "":
        #     return await message.reply_text("Give me something to search ^_^")
        data = AnimeDex.search(query)
        button = BTN.searchCMD(user, data, query)
        await message.reply_text(
            f"{QUERY.format(query)}\n\n© {message.from_user.mention}",
            reply_markup=button,
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
