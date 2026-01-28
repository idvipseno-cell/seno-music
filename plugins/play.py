from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import PLAY_IMG, API_KEY, API_URL
import requests

# Helper to get language
def get_lang(user_id):
    from plugins.start import user_langs
    return user_langs.get(user_id, "ar")

@Client.on_message(filters.command(["شغل", "play", "تشغيل", "ابدي"]) & filters.group)
async def play_cmd(client: Client, message: Message):
    lang = get_lang(message.from_user.id)
    query = " ".join(message.command[1:])
    
    if not query:
        return await message.reply_text("يرجى كتابة اسم الأغنية أو رابط / Please provide a song name or link")

    m = await message.reply_text("🔎 جاري البحث... / Searching...")
    
    # Here we would use NexGenBots API or yt-dlp to get the stream link
    # For this example, we'll simulate the process
    
    # UI with transparent buttons (Icons)
    buttons = [
        [
            InlineKeyboardButton("⏸", callback_data="pause_cb"),
            InlineKeyboardButton("▶️", callback_data="resume_cb"),
            InlineKeyboardButton("⏭", callback_data="skip_cb"),
            InlineKeyboardButton("⏹", callback_data="stop_cb")
        ],
        [InlineKeyboardButton("إغلاق ❌", callback_data="close_cb")]
    ]
    
    await m.delete()
    await message.reply_photo(
        photo=PLAY_IMG,
        caption=f"🎶 **جاري التشغيل / Now Playing**\n\n📌 **العنوان:** {query}\n👤 **بواسطة:** {message.from_user.mention}",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_message(filters.command(["يوت", "تنزيل", "نزل", "انطيني", "download"]))
async def download_cmd(client: Client, message: Message):
    query = " ".join(message.command[1:])
    if not query:
        return await message.reply_text("يرجى كتابة اسم الأغنية للتحميل")
    
    # Simulate NexGenBots API call
    # response = requests.get(f"{API_URL}/download?key={API_KEY}&q={query}")
    
    await message.reply_text(f"📥 جاري تحميل: {query}...")
    # Logic to send the file with custom thumbnail and buttons as requested
