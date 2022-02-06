from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery
import random

Naruto=Client(
      "PYrogramBOT",
      bot_token="5224106219:AAEFXDy1csfqQi1opv0NFynQ28iBzMLbH8g",
      api_id="15316155",
      api_hash="c2340e29da60393bc3c96fa7c0870911"
)


ALL_PIC = [
 "https://telegra.ph/file/56af4fd2b077fceac4758.jpg",
 "https://telegra.ph/file/e212be20adfc3be542760.jpg",
 "https://telegra.ph/file/36e4ef0d26671be24cbc7.jpg",
 "https://telegra.ph/file/7cd3965af58c9be4cf627.jpg",
 "https://telegra.ph/file/e212be20adfc3be542760.jpg",
 "https://telegra.ph/file/36e4ef0d26671be24cbc7.jpg",
 "https://telegra.ph/file/01ec4f1acf418730370ec.jpg",
 "https://telegra.ph/file/1da61ef82de7ee74e618e.jpg"
]

@Naruto.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""𝙷𝙴𝚈 {message.from_user.mention} 𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 <a href=https://t.me/NewPythonWorkBot>𝔽𝕃𝕌𝔽𝔽𝕐 ℙ𝕐ℝ𝕆𝔾ℝ𝔸𝕄</a>, 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃 𝙶𝚁𝙾𝚄𝙿,𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝙰𝙳𝙼𝙸𝙽 𝙰𝙽𝙳 𝚂𝙴𝙴 𝙼𝚈 𝙿𝙾𝚆𝙴𝚁𝚂📌📌 """,
        reply_markup=InlineKeyboardMarkup( [[
          InlineKeyboardButton ("🧿𝐆𝐑𝐎𝐔𝐏🧿", url="https://t.me/ADHOLOKAMHD"),
          InlineKeyboardButton ("🔮𝗖𝗛𝗔𝗡𝗡𝗘𝗟🔮", url="https://t.me/+8WLTJKD-fH0zMzUx"),
          ],[
          InlineKeyboardButton ("🔰𝐄𝐃𝐈𝐓𝐄𝐑🔰", url="t.me/TEAM_KERALA"),
          InlineKeyboardButton ("📍𝗣𝗔𝗜𝗗 𝗣𝗥𝗢𝗠𝗢𝗧𝗜𝗢𝗡", url="t.me/TEAM_KERALA"),
          ],[
          InlineKeyboardButton ("🕵️‍♂️𝗕𝗢𝗧 𝗗𝗘𝗩🕵️‍♂️", url="t.me/TEAM_KERALA"),
          ],[
          InlineKeyboardButton ("🎀𝗟𝗘𝗧'𝗦 𝗥𝗢𝗟𝗟🎀", url="http://t.me/Fluffy_PythonPyroGram_bot?startgroup=true"),
          InlineKeyboardButton ("🤠𝗔𝗕𝗢𝗨𝗧🤠", callback_data="start"),
          ],[
          InlineKeyboardButton ("⚡️𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘⚡️", callback_data="help"),
          InlineKeyboardButton ("🎭𝗙𝗥𝗘𝗘 𝗣𝗥𝗢𝗠𝗢𝗧𝗜𝗢𝗡🎭", url="t.me/TEAM_KERALA_2")
          ]]
          )
          
        )


@Naruto.on_message(filters.command("info"))
async def id_message(bot, message):
    text = f"""
⭐ 𝙵𝙸𝚁𝚂𝚃 𝙽𝙰𝙼𝙴 - {message.from_user.first_name}
❗ 𝙻𝙰𝚂𝚃 𝙽𝙰𝙼𝙴 - {message.from_user.last_name}
📡 𝚄𝚂𝙴𝚁 𝙽𝙰𝙼𝙴 - {message.from_user.username}
📍 𝚄𝚂𝙴𝚁 𝙸𝙳 - {message.from_user.id}
🗃️ 𝚄𝚂𝙴𝚁 𝙼𝙴𝙽𝚃𝙸𝙾𝙽 - {message.from_user.mention}"""


    await message.reply_text(text=text)

@Naruto.on_message(filters.group & filters.command("id"))
async def id(bot, message):
    text = f"""
📀 𝙶𝚁𝙾𝚄𝙿 𝙽𝙰𝙼𝙴 : {message.chat.title}
⚡ 𝙶𝚁𝙾𝚄𝙿 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{message.chat.username}
🎗️ 𝙶𝚁𝙾𝚄𝙿 𝙸𝙳 : {message.chat.id}
📍 𝚄𝚂𝙴𝚁 𝙸𝙳 : {message.from_user.id}
🗃️ 𝚄𝚂𝙴𝚁 𝙼𝙴𝙽𝚃𝙸𝙾𝙽: {message.from_user.mention}"""

    await message.reply_text(text=text)


@Naruto.on_callback_query()
async def callback(bot, msg: CallbackQuery):
    if msg.data == "start":
     await msg.message.edit(
                text="""✯ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href="https://t.me/TEAM_KERALA_2">🚬𝗙𝗔𝗞𝗘 𝗙𝗟𝗨𝗙𝗙𝗬⚡</a>
✯ 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁: <a href="https://t.me/TEAM_KERALA">🖕𝗙𝗨𝗖𝗞 𝗢𝗙𝗙🖕</a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href="https://www.w3schools.com/python/">𝗣𝗬𝗧𝗛𝗢𝗡 𝗖𝗘𝗡𝗧𝗘𝗥</a>
✯ 𝙿𝚈𝚃𝙷𝙾𝙽 𝚃𝚄𝚃𝙾𝚁𝙸𝙰𝙻: <a href="https://www.w3schools.com/python/">𝗣𝗬𝗧𝗛𝗢𝗡 𝗖𝗘𝗡𝗧𝗘𝗥</a>
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴:<a href="https://www.MongoDb.com/">🌐𝗠𝗢𝗡𝗚𝗢 𝗗𝗕🌐</a>
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: <a href="https://dashboard.heroku.com/">⚡𝗛𝗘𝗥𝗢𝗞𝗨⚡</a>
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v2.01 [ 𝙱𝙴𝚃𝙰 ]
✯ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴:  <a href="https://github.com/TEAM-FLUFFY/FluffyV1">🎗️𝗖𝗟𝗜𝗖𝗞 𝗠𝗘🎗️</a>"""
     )

    elif msg.data == "help":
         await msg.message.edit(
             text="""<a href="https://github.com/TEAM-FLUFFY/FluffyV1">🎗️𝗖𝗟𝗜𝗖𝗞 𝗠𝗘🎗️</a>"""
         )


Naruto.run()
