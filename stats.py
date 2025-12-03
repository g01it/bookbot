from typing import Dict, List


def count_words(contents: str):
    num_words = len(contents.split())
    return f"Found {num_words} total words"


def count_chars(contents: str) -> Dict:
    res = {}

    for c in contents.lower():
        if c not in res:
            res[c] = 1
        else:
            res[c] += 1

    return res


def sorted_dict(d: Dict) -> List[Dict]:
    res = []

    for char, count in d.items():
        if char.isalpha():
            res.append({
                "char": char,
                "num": count,
            })

    def get_num(item):
        return item["num"]

    res.sort(key=get_num, reverse=True)

    return res
