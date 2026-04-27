# header.py
from telethon.tl.types import MessageEntityCustomEmoji
from core.offsets import get_utf16_offset
from data.header_data import ORIGINAL_HEADERS, PREMIUM_HEADERS, HEADER_EMOJI_IDS_LIST

def process_header(text):
    """
    Replace any original header in a message with corresponding premium emojis.
    Supports multiple headers, repeated emojis, and multi-code-point emojis.
    """
    for idx, original in enumerate(ORIGINAL_HEADERS):
        if original in text:
            premium = PREMIUM_HEADERS[idx]
            emoji_ids = HEADER_EMOJI_IDS_LIST[idx]
            start_index = text.find(original)
            new_text = text.replace(original, premium, 1)

            entities = []
            offset = start_index
            # Iterate through each emoji ID and attach to the correct emoji in premium string
            for i, emoji_id in enumerate(emoji_ids):
                if i >= len(premium):
                    break  # safety check
                # Take the emoji character
                emoji_char = premium[i]
                # Calculate correct UTF-16 offset
                utf16_offset = get_utf16_offset(new_text, offset)
                # Calculate correct UTF-16 length of this emoji
                length = len(emoji_char.encode("utf-16-le")) // 2
                # Append the custom emoji entity
                entities.append(
                    MessageEntityCustomEmoji(
                        offset=utf16_offset,
                        length=length,
                        document_id=emoji_id
                    )
                )
                # Move offset by actual string length (Python chars)
                offset += len(emoji_char)

            return new_text, entities

    # If no headers matched
    return text, []
