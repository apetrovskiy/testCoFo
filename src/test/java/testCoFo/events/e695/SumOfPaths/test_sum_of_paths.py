from src.main.java.testCoFo.events.e695.SumOfPaths.sum_of_paths \
    import sum_of_paths
import pytest
from typing import List


test_data = [
    ([5, 1, 5], [3, 5, 1, 4, 2], [[1, 9], [2, 4], [
     3, 6], [4, 6], [5, 2]], [62, 58, 78, 86, 86]),
    ([4, 40, 6], [92, 21, 82, 46], [[3, 56],
                                    [1, 72], [4, 28], [1, 97], [2, 49], [
     2, 88]], [239185261, 666314041, 50729936,
               516818968, 766409450, 756910476])
]


@pytest.mark.skip(reason="TODO: no way of currently testing this")
@pytest.mark.parametrize(
    "numbers,numbers2,input_data,expected_result", test_data)
def test_sum_of_pathsz(numbers: List[int],
                       numbers2: List[int],
                       input_data: List[List[int]],
                       expected_result: List[int]):
    assert expected_result == sum_of_paths(numbers, numbers2, input_data)
