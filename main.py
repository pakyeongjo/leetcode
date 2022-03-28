from problems.pn0009_isPalindrome import IsPalindrome
from problems.pn0171_titleToNumber import TitleToNumber
from problems.pn0001_twoSum import TwoSum
from utils import duration_decorator


loop = 10000


@duration_decorator(loop=loop)
def run():
    # column = "AAEEAAXCACX"
    # module = TitleToNumber()

    target = 151
    module = IsPalindrome()
    module.solution(target)


if __name__ == '__main__':
    run()
