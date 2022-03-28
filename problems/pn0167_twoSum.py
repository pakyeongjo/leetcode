class TwoSum:
    def solution(self, numbers, target):
        curs_1, curs_2, end = 0, 0, len(numbers) - 1
        for item in numbers:
            curs_1 += 1
            left, right = curs_1, end
            while left <= right:
                mid = curs_2 = (left + right) // 2
                if item + numbers[mid] > target:
                    right = mid - 1
                elif item + numbers[mid] < target:
                    left = mid + 1
                else:
                    return [curs_1, curs_2 + 1]
        return -1

    def two_pointer(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left <= right:
            sum = numbers[left] + numbers[right]
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return -1
