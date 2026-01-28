import asyncio
from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN, STRING_SESSION
from utils.strings import STRINGS

# Initialize Bot Client
app = Client(
    "SenoMusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# Initialize Assistant Client
assistant = Client(
    "SenoAssistant",
    api_id=API_ID,
    api_hash=API_HASH,
    session_string=STRING_SESSION
)

# Initialize Py-TgCalls
call_py = PyTgCalls(assistant)

async def main():
    await app.start()
    print("Bot Started!")
    await assistant.start()
    print("Assistant Started!")
    await call_py.start()
    print("Py-TgCalls Started!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
