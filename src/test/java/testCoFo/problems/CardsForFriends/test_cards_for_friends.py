from src.main.java.testCoFo.problems.CardsForFriends.cards_for_friends \
    import cards_for_friends
import pytest
from typing import List


test_data = [
    (5, [[2, 2, 3], [3, 3, 2], [5, 10, 2], [11, 13, 1],
         [1, 4, 4]], ['YES', 'NO', 'YES', 'YES', 'YES'])
]


@ pytest.mark.parametrize("number,cases,expected_result", test_data)
def test_cards_for_friends(number: int,
                           cases: List[List[int]], expected_result: List[str]):
    assert expected_result == cards_for_friends(number, cases)
