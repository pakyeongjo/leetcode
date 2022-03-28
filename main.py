from problems.titleToNumber_171 import TitleToNumber
from utils import duration_decorator


loop = 1


@duration_decorator(loop=loop)
def run():
    column = "AAEEAAXCACX"
    module = TitleToNumber()
    module.solution(column)


if __name__ == '__main__':
    run()
