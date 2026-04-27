from telethon.tl.types import MessageEntityCustomEmoji
from core.offsets import get_utf16_offset

def build_custom_emoji_entities(text, start_index, emoji_ids):
    entities = []

    utf16_offset = get_utf16_offset(text, start_index)

    offset = utf16_offset
    for emoji_id in emoji_ids:
        entities.append(
            MessageEntityCustomEmoji(
                offset=offset,
                length=2,
                document_id=emoji_id
            )
        )
        offset += 2

    return entities
