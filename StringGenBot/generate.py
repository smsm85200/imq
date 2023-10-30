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



ask_ques = " **• 𝖼𝗁𝗈𝗈𝗌𝖾 𝗍𝗁𝖾 𝗌𝖾𝗌𝗌𝗂𝗈𝗇 𝗍ʏ𝗉𝖾** \n\n**✓**"
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
    await msg.reply(f" ⚡ ¦ بـدء إنـشـاء جـلسـة **{ty}** ...")
    user_id = msg.chat.id
    api_id_msg = await bot.ask(user_id, "✨ حسنـا قم بأرسال الـ API_ID\n\nاضغط /skip عشان تستخرج بالرقم فقط.", filters=filters.text)
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
        api_hash_msg = await bot.ask(user_id, " ✨ حسنـا قم بأرسال الـ API_HASH", filters=filters.text)
        if await cancelled(api_hash_msg):
            return
        api_hash = api_hash_msg.text
    if not is_bot:
        t = "• الان ارسل رقمك مع رمز دولتك \n\n • مثال : +201287585064"
    else:
        t = "ᴩʟᴇᴀsᴇ sᴇɴᴅ ʏᴏᴜʀ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ.\nᴇxᴀᴍᴩʟᴇ : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = await bot.ask(user_id, t, filters=filters.text)
    if await cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        await msg.reply("** انتظر سـوف نـرسـل كـود لحسابك بالتليجـرام .**")
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
        await msg.reply(" عذرا  ! **ᴀᴩɪ_ɪᴅ** و **ᴀᴩɪ_ʜᴀsʜ** بتوع اك محذوف. \n\n • اضغط  /start وابدا من جديد .", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        await msg.reply("عذرا  ! **الرقم** مش معمول بيه اكونت علي التلي.\n\nاضغط  /start وابدا من جديد . ", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = await bot.ask(user_id, "[ارسل الكود زي اللي في الصوره](https://telegra.ph/file/da1af082c6b754959ab47.jpg) » 🔍من فضلك افحص حسابك بالتليجرام وتفقد الكود من حساب اشعارات التليجرام. إذا كان\n  هناك تحقق بخطوتين( المرور ) ، أرسل كلمة المرور هنا بعد ارسال كود الدخول بالتنسيق أدناه.- اذا كانت كلمة المرور او الكود  هي\n 12345 يرجى ارسالها بالشكل التالي 1 2 3 4 5 مع وجود مسـافـات بين الارقام اذا احتجت مساعدة @u0uu0.", filters=filters.text, timeout=600)
            if await cancelled(phone_code_msg):
                return
    except TimeoutError:
        await msg.reply("• انتهت آلمـدهہ‏‏\n\n• اضغط  /start\n\n• وابدا من جديد", reply_markup=InlineKeyboardMarkup(gen_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                await client.sign_in(phone_number, phone_code, password=None)
            else:
                await client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            await msg.reply("• انتهت آلمـدهہ‏‏\n\n• اضغط  /start\n\n• وابدا من جديد", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            await msg.reply("• انتهت آلمـدهہ‏‏\n\n• اضغط  /start\n\n• وابدا من جديد", reply_markup=InlineKeyboardMarkup(gen_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = await bot.ask(user_id, "**• آبعت الباسورد الخاص بحسابڪ .** ", filters=filters.text, timeout=300)
            except TimeoutError:
                await msg.reply("• انتهت آلمـدهہ‏‏\n\n• اضغط  /start\n\n• وابدا من جديد", reply_markup=InlineKeyboardMarkup(gen_button))
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
                await two_step_msg.reply("• الباسـورد غير صحيح\\• إضغط  /start  !\n\n• وجرب تآني وآتاكد من الباسورد ", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
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
    text = f"** {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n** ʙʏ :** @u0uu0 \n @i_m_q"
    try:
        if not is_bot:
            await client.send_message("me", text)
        else:
            await bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    await client.disconnect()
    await bot.send_message(msg.chat.id, " ✅تم استخراج الجلسه بنجاح ️ {} .\n\n🔍من فضلك اذهب الي الرسايل المحفوظه بحسابك!  ! \n\n**ᴀ sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ** @u0uu0  ".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


async def cancelled(msg):
    if "/cancel" in msg.text:
        await msg.reply("** تم انهاء آلعمـليـهہ‏‏ **", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/restart" in msg.text:
        await msg.reply("** تمـ آعآد‏‏هہ تشـغيـل آلبوت !**", quote=True, reply_markup=InlineKeyboardMarkup(gen_button))
        return True
    elif "/skip" in msg.text:
        return False
    elif msg.text.startswith("/"):  # Bot Commands
        await msg.reply("** تم آنهآء آلعمـليـهہ‏‏ !**", quote=True)
        return True
    else:
        return False
