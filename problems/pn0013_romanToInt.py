class RomanToInt:
    def solution(self, s):
        roman_value = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        answer = 0
        for index in range(len(s) - 1):
            if roman_value[s[index]] < roman_value[s[index + 1]]:
                answer -= roman_value[s[index]]
            else:
                answer += roman_value[s[index]]
        return answer + roman_value[s[-1]]
