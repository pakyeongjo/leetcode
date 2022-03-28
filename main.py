from convertToTitle_168 import ConvertToTitle
from fibonacci import Fibonacci
from isIsomorphic_205 import IsIsomorphic
from maxProfit_121 import MaxProfit
from maxSubArray_53 import MaxSubArray
from random import randint

from titleToNumber_171 import TitleToNumber
from twoSum_167 import TwoSum
from utils import duration_decorator


loop = 1


@duration_decorator(loop=loop)
def run():
    column = "AAEEAAXCACX"
    module = TitleToNumber()
    module.solution(column)


if __name__ == '__main__':
    run()
