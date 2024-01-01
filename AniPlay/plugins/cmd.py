import pyrogram
from pyrogram import Client
from pyrogram import filters, enums
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from pyrogram.types import Message
from pyrogram import filters
from AniPlay import app
from AniPlay.plugins.AnimeDex import AnimeDex
from AniPlay.plugins.button import BTN
from AniPlay.plugins.ErrorHandler import CMDErrorHandler
from config import API_ID,TOKEN,API_HASH
import os


bot_token = os.environ.get("TOKEN")
api_hash = os.environ.get("API_HASH") 
api_id = os.environ.get("API_ID")
OWNER_ID = os.environ.get("OWNER_ID", "945284066")
ADMIN_LIST = [int(ch) for ch in (os.environ.get("ADMIN_LIST", f"{OWNER_ID}")).split()]
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "FLIGHER")
PERMANENT_GROUP = os.environ.get("PERMANENT_GROUP", "-1002045115155")
GROUP_ID = [int(ch) for ch in (os.environ.get("GROUP_ID", f"{PERMANENT_GROUP}")).split()]
UPDATES_CHANNEL = str(os.environ.get("UPDATES_CHANNEL", "trumbots"))
app = Client("my_bot",api_id=api_id, api_hash=api_hash,bot_token=bot_token)  


@app.on_message(filters.command(["start", "ping", "help", "alive"]))
@CMDErrorHandler
async def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    if str(message.chat.id).startswith("-100") and message.chat.id not in GROUP_ID:
        return
    elif message.chat.id not in GROUP_ID:
        if UPDATES_CHANNEL != "None":
            try:
                user = await app.get_chat_member(UPDATES_CHANNEL, message.chat.id)
                if user.status == enums.ChatMemberStatus.BANNED:
                    await app.send_message(
                        chat_id=message.chat.id,
                        text=f"__Sorry, you are banned. Contact My [ Owner ](https://telegram.me/{OWNER_USERNAME})__",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                 await app.send_message(
                    chat_id=message.chat.id,
                    text="<i>🔐 Join Channel To Use Me 🔐</i>",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("🔓 Join Now 🔓", url=f"https://t.me/{UPDATES_CHANNEL}")
                            ]
                        ]
                    ),

                )
                 return
            except Exception:
                await app.send_message(
                    chat_id=message.chat.id,
                    text=f"<i>Something went wrong</i> <b> <a href='https://telegram.me/{OWNER_USERNAME}'>CLICK HERE FOR SUPPORT </a></b>",

                    disable_web_page_preview=True)
                return
    await app.send_message(message.chat.id, f"__👋 Hi **{message.from_user.mention}**, i am Link Bypasser Bot, just send me any supported links and i will you get you results.\nCheckout /help to Read More__",
                           reply_markup=InlineKeyboardMarkup([[ InlineKeyboardButton("🌐 Source Code 🌐", url="https://github.com/bipinkrish/Link-Bypasser-Bot")]]), reply_to_message_id=message.id)


QUERY = "**Search Results:** `{}`"


@app.on_message(filters.command(["search", "s"]))
@CMDErrorHandler
async def searchCMD(_, message: Message):
    try:
        user = message.from_user.id
        query = " ".join(message.command[1:])
        if query == "":
            return await message.reply_text("Give me something to search ^_^")
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
