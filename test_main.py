import pytest

from main import get_min_platforms_count


def test_get_min_platforms_count():
    data, limit = [1, 2, 3, 4], 4
    assert get_min_platforms_count(data, limit) == 3
    data, limit = [1, 1, 1, 1], 4
    assert get_min_platforms_count(data, limit) == 2
    data, limit = [1, 1, 1], 2
    assert get_min_platforms_count(data, limit) == 2
    data, limit = [1, 1, 1, 1, 100], 102
    assert get_min_platforms_count(data, limit) == 3
    data, limit = [5, 3, 4, 1, 2], 6
    assert get_min_platforms_count(data, limit) == 3
