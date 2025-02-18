import sys

# Решается методом двух указателей
# Сортируем список по убыванию
# Смотрим, если data[0] > option -> error
# Иначе выкидываем все data[i] == option
# И методом двух указателей проходимся по списку


def search_min_platforms_count(data: list, option: int):
    sort_data = sorted(data, reversed = True)
    result_count = 0
    if sort_data[0] > option:
        return "error"
    for i in range(sort_data):
        if sort_data[i] == option:
            result_count += 1
            sort_data[i] = [None]
    i = 0
    j = len(sort_data-1)
    while i < j:
        if sort_data[i] + sort_data[j] == option:
            result_count += 1
			j-=1
        elif sort_data[i] + sort_data[j] > option:
            i += 1
        elif sort_data[i] + sort_data[j] < option:
            j -= 1


def get() -> tuple[list, int]:
    data = map(int, sys.stdin.readline().lstrip().split(' '))
    option = int(sys.stdin.readline().lstrip())
    return data, option


search_min_platforms_count(*get())
