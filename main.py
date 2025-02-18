# id: 133631944


def get_min_platforms_count(robots_weight: list[int], limit: int) -> int:
    """
    Получает значение минимального количества платформ для перевозки роботов.
        Параметры:
        robots_weight: list[int] - содержит веса роботов.
        option: int - предельный вес платформы.
    """
    robots_weight = sorted(robots_weight)
    platforms_count = 0
    min_element = 0
    max_element = len(robots_weight)-1

    while min_element <= max_element:
        if robots_weight[min_element] + robots_weight[max_element] <= limit:
            min_element += 1
        max_element -= 1
        platforms_count += 1
    return platforms_count


if __name__ == '__main__':

    def get() -> tuple[list, int]:
        robots_weight = map(int, input().split(' '))
        limit = int(input())
        return list(robots_weight), limit

    print(get_min_platforms_count(*get()))



# import sys

# MAX_ROBOTS_ON_PLATFORM = 2


# def search_min_platforms_count(data: list, limit: int) -> int:
#     """
#     Ищет минимальное число платформ для перевозки роботов.
#         Параметры:
#         data: list - размер роботов.
#         option: int
#     """
#     result_count = 0
#     index_left = 0
#     index_right = len(data)-1

#     def eliminate_robots():
#         """Выделяет платформу для роботов помещающихся на одной платформе."""
#         nonlocal result_count, index_left, index_right
#         robots_on_platform = 0
#         total_count = 0

#         while (index_left <= index_right
#                and robots_on_platform < MAX_ROBOTS_ON_PLATFORM):
#             if total_count + data[index_right] <= limit:
#                 total_count += data[index_right]
#                 robots_on_platform += 1
#                 index_right -= 1
#             elif total_count + data[index_left] <= limit:
#                 total_count += data[index_left]
#                 robots_on_platform += 1
#                 index_left += 1
#             else:
#                 break

#         result_count += 1

#     data.sort()
#     if data[-1] > limit:
#         return None

#     while index_left <= index_right:
#         if data[index_left] + data[index_right] == limit:
#             result_count += 1
#             index_left += 1
#             index_right -= 1
#         elif data[index_left] + data[index_right] < limit:
#             eliminate_robots()
#         else:
#             result_count += 1
#             index_right -= 1

#     return result_count


# def get() -> tuple[list, int]:
#     data = map(int, sys.stdin.readline().lstrip().split(' '))
#     limit = int(sys.stdin.readline().lstrip())
#     return list(data), limit


# if __name__ == '__main__':
#     print(search_min_platforms_count(*get()))
