import sys


def search_min_platforms_count(data: list, option: int):
    ...


def get() -> tuple[list, int]:
    data = map(int, sys.stdin.readline().lstrip().split(' '))
    option = int(sys.stdin.readline().lstrip())
    return data, option


data, option = get()
