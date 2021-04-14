from src.main.java.testCoFo.events.e695.ThreeBags.three_bags import three_bags
import pytest
from typing import List


test_data = [
    ([2, 4, 1], [[1, 2], [6, 3, 4, 5], [5]], 20),
    ([3, 2, 2], [[7, 5, 4], [2, 9], [7, 1]], 29)
]


@pytest.mark.parametrize("numbers,input_data,expected_result", test_data)
def test_three_bags(numbers: List[int],
                    input_data: List[List[int]], expected_result: int):
    assert expected_result == three_bags(numbers, input_data)
