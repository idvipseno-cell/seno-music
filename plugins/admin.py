from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import OWNER_ID, SUPPORT_CHANNEL
import asyncio

# Mock database for demonstration (In production, use MongoDB)
users_db = set()
groups_db = set()

@Client.on_message(filters.command("panel") & filters.user(OWNER_ID))
async def admin_panel(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("📊 الإحصائيات", callback_data="stats_callback"),
            InlineKeyboardButton("📢 إذاعة", callback_data="broadcast_callback")
        ],
        [
            InlineKeyboardButton("🔐 الاشتراك الإجباري", callback_data="fsub_callback"),
            InlineKeyboardButton("📝 تغيير الكلايش", callback_data="strings_callback")
        ],
        [InlineKeyboardButton("إغلاق اللوحة ❌", callback_data="close_admin")]
    ]
    await message.reply_text(
        "🛠 **أهلاً بك يا مطورنا سينو في لوحة التحكم**\n\nاختر من الأزرار أدناه لإدارة البوت:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

@Client.on_callback_query(filters.regex("stats_callback") & filters.user(OWNER_ID))
async def stats_call(client, callback_query):
    text = f"📊 **إحصائيات سورس ميوزك سينو:**\n\n"
    text += f"👤 عدد المستخدمين: {len(users_db)}\n"
    text += f"👥 عدد المجموعات: {len(groups_db)}\n"
    text += f"📡 حالة المساعد: متصل ✅"
    await callback_query.answer("تم تحديث الإحصائيات", show_alert=True)
    await callback_query.edit_message_text(text, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("رجوع 🔙", callback_data="back_to_admin")]]))

@Client.on_callback_query(filters.regex("broadcast_callback") & filters.user(OWNER_ID))
async def broadcast_call(client, callback_query):
    await callback_query.answer("أرسل الرسالة التي تريد إذاعتها الآن", show_alert=True)
    # Logic to wait for next message and broadcast it
    # This is a simplified version
    
@Client.on_callback_query(filters.regex("back_to_admin") & filters.user(OWNER_ID))
async def back_to_admin(client, callback_query):
    await admin_panel(client, callback_query.message)
    await callback_query.message.delete()

@Client.on_message(filters.new_chat_members)
async def auto_join_db(client, message):
    groups_db.add(message.chat.id)

@Client.on_message(filters.private)
async def auto_user_db(client, message):
    users_db.add(message.from_user.id)
