from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from config import START_IMG, OWNER_USERNAME, SUPPORT_CHANNEL
from utils.strings import STRINGS

# Simple in-memory language storage (In production, use MongoDB)
user_langs = {}

@Client.on_message(filters.command("start") & filters.private)
async def start(client: Client, message: Message):
    user_id = message.from_user.id
    if user_id not in user_langs:
        # Ask for language on first start
        buttons = [
            [
                InlineKeyboardButton("العربية 🇮🇶", callback_data="set_lang_ar"),
                InlineKeyboardButton("English 🇺🇸", callback_data="set_lang_en")
            ]
        ]
        await message.reply_photo(
            photo=START_IMG,
            caption=STRINGS["ar"]["choose_lang"],
            reply_markup=InlineKeyboardMarkup(buttons)
        )
        return

    lang = user_langs.get(user_id, "ar")
    text = STRINGS[lang]["start_msg"].format(name=message.from_user.mention)
    
    buttons = [
        [InlineKeyboardButton(STRINGS[lang]["add_me"], url=f"https://t.me/{client.me.username}?startgroup=true")],
        [
            InlineKeyboardButton(STRINGS[lang]["help_btn"], callback_data="help_cmds"),
            InlineKeyboardButton(STRINGS[lang]["developer"], url=f"https://t.me/{OWNER_USERNAME}")
        ],
        [
            InlineKeyboardButton(STRINGS[lang]["channel"], url=f"https://t.me/{SUPPORT_CHANNEL}"),
            InlineKeyboardButton(STRINGS[lang]["lang_btn"], callback_data="choose_lang")
        ]
    ]
    
    await message.reply_photo(
        photo=START_IMG,
        caption=text,
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex(r"^set_lang_"))
async def set_language(client, callback_query):
    lang = callback_query.data.split("_")[-1]
    user_langs[callback_query.from_user.id] = lang
    await callback_query.answer("تم ضبط اللغة / Language Set")
    # Trigger start again to show the welcome message
    await start(client, callback_query.message)
    await callback_query.message.delete()
