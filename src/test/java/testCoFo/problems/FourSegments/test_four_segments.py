from src.main.java.testCoFo.problems.FourSegments.four_segments \
    import four_segments
from typing import List
import pytest


test_data = [
    (4, [[1, 2, 3, 4], [5, 5, 5, 5], [3, 1, 4, 1],
         [100, 20, 20, 100]], [3, 25, 3, 2000])
]


@pytest.mark.parametrize("number_of_cases,cases,expected_result", test_data)
def test_four_segments(number_of_cases: int,
                       cases: List[List[int]], expected_result: List[int]):
    assert expected_result == four_segments(number_of_cases, cases)
