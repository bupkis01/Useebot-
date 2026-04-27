from telethon import TelegramClient, functions
from config import api_id, api_hash

# 👇 use DIFFERENT session name (important)
client = TelegramClient("debug_session", api_id, api_hash)

async def main():
    await client.start()

    result = await client(functions.messages.GetCustomEmojiDocumentsRequest(
        document_id=[6231047418125753255]
    ))

    print("\n=== DEBUG RESULT ===\n")

    for doc in result:
        for attr in doc.attributes:
            if hasattr(attr, "alt"):
                print("👉 BASE EMOJI (alt):", attr.alt)

    print("\n====================\n")

    await client.disconnect()

with client:
    client.loop.run_until_complete(main())

