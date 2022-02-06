from pyrogram import Client, filter
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram.types import CallbackQuery
import randam
import os

PHOTO_LINK = [
 "Photo Link",
 "photo Link"
 ]

Muhammed = Client(
    "Pyrogram Bot",
    bot_token ="5205686953:AAG3r6PYveX9LGLlF_JgWvYVSFUzqeDRcWI",
    api_id ="19143782",
    api_hash ="43176648b57c393328f832939efb72da"
)


@Muhammed.on_message(filters.command("start")) 
async def start_message(bot, message)
    button = [[
      InlineKeyboardButton("Mo Tech YT", callback_data="start")
      ]]
    await messages.reply_photo(
        photo=random.choice(https://telegra.ph/file/36e4ef0d26671be24cbc7.jpg),
        text="Hello {message.from_user.mention}   Bro Sugamano",
        reply_markup=InlineKeyboardMarkup(buttons)
    )



@Muhammad.on_callback_query()
async def callback(bot, msg: CallbackQuery)
    if msg.data == "start":
        await message.message.edit(
            text=" hello {msg.from_user.mention}  Start Text"
        )



 Muhammed.run()

