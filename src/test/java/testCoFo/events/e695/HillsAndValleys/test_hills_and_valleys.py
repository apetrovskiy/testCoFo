from src.main.java.testCoFo.events.e695.HillsAndValleys.hills_and_valleys import hills_and_valleys
import pytest
from typing import List


test_data = [
    (4, [[3], [1, 5, 3], [5], [2, 2, 2, 2, 2], [6], [
     1, 6, 2, 5, 2, 10], [5], [1, 6, 2, 5, 1]], [[0], [0], [1], [0]])
]


@pytest.mark.parametrize("number,input_data,expected_result", test_data)
def test_hills_and_valleys(number: int, input_data: List[List[int]], expected_result: List[int]):
    assert expected_result == hills_and_valleys(number, input_data)
