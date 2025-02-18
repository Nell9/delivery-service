# id: 133632349


def get_min_platforms_count(robots_weight: tuple[int], limit: int) -> int:
    """
    Получает значение минимального количества платформ для перевозки роботов.
        Параметры:
        robots_weight: tuple[int] - содержит веса роботов.
        limit: int - предельный вес платформы.
    """
    weights: list = sorted(robots_weight)
    platforms_count = 0
    min_element = 0
    max_element = len(weights)-1

    while min_element <= max_element:
        if (weights[min_element] + weights[max_element] <= limit):
            min_element += 1
        max_element -= 1
        platforms_count += 1
    return platforms_count


if __name__ == '__main__':

    def get() -> tuple[tuple[int], int]:
        robots_weight = map(int, input().split(' '))
        limit = int(input())
        return tuple(robots_weight), limit

    print(get_min_platforms_count(*get()))