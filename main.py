# id: 133641462


from typing import Iterable


def get_min_platforms_count(
        robots_weights: Iterable[int], 
        limit: int
        ) -> int:
    """
    Получает значение минимального количества платформ для перевозки роботов.
        Параметры:
        robots_weight: tuple[int] - содержит веса роботов.
        limit: int - предельный вес платформы.
    """
    weights = sorted(robots_weights)
    platforms_count = 0
    min_index = 0
    max_index = len(weights)-1

    while min_index <= max_index:
        if weights[min_index] + weights[max_index] <= limit:
            min_index += 1
        max_index -= 1
        platforms_count += 1
    return platforms_count


if __name__ == '__main__':
    robots_weights = map(int, input().split(' '))
    limit = int(input())
    print(get_min_platforms_count(robots_weights, limit))
