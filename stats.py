from typing import TypedDict

class CountInfo(TypedDict):
    char: str
    num: int

def get_num_words(text: str):
    return len(text.split())

def get_character_counts(path: str) -> dict[str, int]:
    char_dict = {}
    with open(path) as f:
        text = f.read()
    for word in text.split():
        for char in word:
            lowered_char = char.lower()
            if char_dict.get(lowered_char):
                char_dict[lowered_char] += 1
            else:
                char_dict[lowered_char] = 1
    return char_dict

def get_count_from_dict(d: CountInfo) -> int:
    return d.get("num")

def sort_character_counts(counts:dict[str, int]) -> list[CountInfo]:
    count_list = [CountInfo(char=char, num=count) for char,count in counts.items()]
    count_list.sort(key=get_count_from_dict, reverse=True)
    return count_list


