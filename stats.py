def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)


def sort_on(t: tuple[str, int]) -> int:
    return t[1]


def chars_dict_to_sorted_list(chars: dict[str, int]) -> list[tuple[str, int]]:
    # return sorted(chars.items(), reverse=True, key=sort_on)
    l = []
    for key, value in chars.items():
        l.append((key, value))
    sort_chars = sorted(l, reverse=True, key=sort_on)
    return sort_chars


def get_chars_dict(text: str) -> dict[str, int]:
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
