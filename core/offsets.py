def get_utf16_offset(text, index):
    return len(text[:index].encode("utf-16-le")) // 2
