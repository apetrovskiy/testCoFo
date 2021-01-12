from src.main.java.testCoFo.problems.WasteSorting.waste_sorting import waste_sorting
import pytest
from typing import List


test_data = [
    (7, [[[1, 2, 3], [1, 2, 3, 0, 0]], [[2, 2, 3], [1, 2, 3, 1, 0]], [[2, 2, 3], [1, 2, 3, 0, 1]], [[1, 2, 5], [1, 2, 3, 1, 1]], [[0, 0, 0], [
     0, 0, 0, 0, 0]], [[0, 0, 4], [1, 0, 0, 0, 0]], [[13, 37, 42], [0, 0, 0, 40, 47]]], ['YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES'])
]


@ pytest.mark.parametrize("number,cases,expected_result", test_data)
def test_waste_sorting(number: int, cases: List[List[int]], expected_result: List[str]):
    assert expected_result == waste_sorting(number, cases)
