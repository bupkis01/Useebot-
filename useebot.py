from telethon import TelegramClient, events
from config import api_id, api_hash, session_name, group

from features.header import process_header
from features.leagues import replace_league_emojis
from utils.text import safe_text

client = TelegramClient(session_name, api_id, api_hash)


@client.on(events.NewMessage(chats=group))
async def handle_message(event):
    text = safe_text(event.raw_text)

    if not text:
        return

    all_entities = []

    # 🔥 Step 1: Header → replace with premium emojis
    text, header_entities = process_header(text)
    all_entities.extend(header_entities)

    # 🔥 Step 2: League emojis → replace with premium versions
    text, league_entities = replace_league_emojis(text)
    all_entities.extend(league_entities)

    # ❌ If nothing changed, skip sending
    if not all_entities:
        return

    # ✅ Send updated message with all premium emoji entities
    await client.send_message(
        event.chat_id,
        text,
        formatting_entities=all_entities
    )


client.start()
print("Userbot running... ✅")
client.run_until_disconnected()
