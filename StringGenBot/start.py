from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""⦿ 𝐓𝐇𝐄 𝐁𝐎𝐓 𝐖𝐀𝐒 𝐂𝐑𝐄𝐀𝐓𝐄𝐃 𝐁𝐘 [ 𝘼𝘽𝙊𝘿┋🇮🇶₂₀₀₇ ](https://t.me/u0uu0)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="‹ 𝐜𝐥𝐢𝐜𝐤 𝐭𝐨 𝐜𝐫𝐞𝐚𝐭𝐞 𝐚 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 ›", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("‹ 𝘼𝘽𝙊𝘿┋🇮🇶₂₀₀₇ ›", url="https://t.me/u0uu0"),
                    InlineKeyboardButton("‹ 𝘼𝘽𝙊𝘿┋🇮🇶₂₀₀₇ ›", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
