from src.main.java.testCoFo.events.e695.DistinctiveRootsInATree.distinctive_roots_in_a_tree import distinctive_roots_in_a_tree
import pytest
from typing import List


test_data = [
    (5, [2, 5, 1, 1, 4], [[1, 2], [1, 3], [2, 4], [2, 5]], 3),
    (5, [2, 1, 1, 1, 4], [[1, 2], [1, 3], [2, 4], [2, 5]], 0)
]


@ pytest.mark.parametrize("number,numbers,input_data,expected_result", test_data)
def test_wizard_of_orz(number: int, numbers: List[int], input_data: List[List[int]], expected_result: int):
    assert expected_result == distinctive_roots_in_a_tree(
        number, numbers, input_data)
