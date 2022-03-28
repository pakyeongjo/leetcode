import string


class ConvertToTitle:
    def solution(self, columnNumber: int) -> str:
        hashmap = {
            1: "A", 2: "B", 3: "C", 4: "D",
            5: "E", 6: "F", 7: "G", 8: "H",
            9: "I", 10: "J", 11: "K", 12: "L",
            13: "M", 14: "N", 15: "O", 16: "P",
            17: "Q", 18: "R", 19: "S", 20: "T",
            21: "U", 22: "V", 23: "W", 24: "X",
            25: "Y", 26: "Z",
        }
        if columnNumber in hashmap:
            return hashmap[columnNumber]
        answer = list()
        while columnNumber > 0:
            answer.append(columnNumber % 26)
            columnNumber = columnNumber // 26
            if columnNumber <= 26:
                answer.append(columnNumber)
                break
        answer = str(hashmap[columnNumber // 26]) + str(hashmap[columnNumber % 26])
        column = [hashmap[x] for x in answer]
        return ''.join(column[::-1])

    def solution_2(self, num):
        capitals = list(string.ascii_uppercase)
        result = []
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        return ''.join(result)

    # def solution_3(self, num):
