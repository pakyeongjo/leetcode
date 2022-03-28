import time


def print_duration(message, duration):
    if duration > 1:
        if duration > 60:
            minute, second = int(duration) // 60, int(duration) % 60
            print(f"{message}: {minute}m {second}s")
        else:
            print(f"{message}: {int(duration):,}s")
    elif duration * 1000 > 1:
        print(f"{message}: {int(duration * 1000):,}ms")
    elif duration * 1000000 > 1:
        print(f"{message}: {int(duration * 1000000):,}us")
    else:
        print(f"{message}: < 1us")


def print_avg_duration(duration):
    message = "평균 실행 시간"
    print_duration(message, duration)


def print_total_duration(duration):
    message = "전체 실행 시간"
    print_duration(message, duration)


def duration_decorator(loop=None):
    def deco(func):
        def wrapper(*args, **kwargs):
            duration_list = []
            for _ in range(loop):
                start_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                duration = end_time - start_time
                duration_list.append(duration)

            avg_duration = sum(duration_list) / loop
            total_duration = sum(duration_list)

            print_avg_duration(avg_duration)
            print_total_duration(total_duration)

        return wrapper
    return deco
