import string


def get_int(place, index):
    return 26 ** (place - 1) * index


class TitleToNumber:
    def solution(self, columnTitle: str) -> int:
        answer, column_len = 0, len(columnTitle)
        for letter in columnTitle:
            letter_index = string.ascii_uppercase.index(letter) + 1
            answer += get_int(column_len, letter_index)
            column_len -= 1
        return answer
