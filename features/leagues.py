from telethon.tl.types import MessageEntityCustomEmoji
from core.offsets import get_utf16_offset
from data.emoji_ids import LEAGUE_EMOJIS

def get_emoji_length(emoji: str) -> int:
    """Correct UTF-16 length for any emoji (flags, complex emojis, etc.)"""
    return len(emoji.encode("utf-16-le")) // 2

def replace_league_emojis(text: str):
    """
    Replace all league emojis with premium versions and return Telegram entities
    """
    # Normalize text (remove variation selectors, e.g., ⚽️ → ⚽)
    text = text.replace("\ufe0f", "")

    entities = []
    new_text = text

    for normal_emoji, (premium_emoji, emoji_id) in LEAGUE_EMOJIS.items():
        start = 0
        while True:
            index = new_text.find(normal_emoji, start)
            if index == -1:
                break

            # Replace emoji visually
            new_text = new_text[:index] + premium_emoji + new_text[index + len(normal_emoji):]

            # Correct UTF-16 offset
            utf16_offset = get_utf16_offset(new_text, index)
            length = get_emoji_length(premium_emoji)

            entities.append(
                MessageEntityCustomEmoji(
                    offset=utf16_offset,
                    length=length,
                    document_id=emoji_id
                )
            )

            start = index + len(premium_emoji)

    return new_text, entities
