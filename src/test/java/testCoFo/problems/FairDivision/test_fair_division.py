from src.main.java.testCoFo.problems.FairDivision.fair_division import fair_division
import pytest
from typing import List


test_data = [
    (5, [[[2], [1, 1]], [[2], [1, 2]], [[4], [1, 2, 1, 2]], [
     [3], [2, 2, 2]], [[3], [2, 1, 2]]], ['YES', 'NO', 'YES', 'NO', 'NO'])
]


@ pytest.mark.parametrize("number,cases,expected_result", test_data)
def test_fair_division(number: int, cases: List[List[int]], expected_result: List[str]):
    assert expected_result == fair_division(number, cases)
