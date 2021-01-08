from src.main.java.testCoFo.events.e695.WizardOfOrz.wizard_of_orz import wizard_of_orz
import pytest
from typing import List


test_data = [
    (2, [1, 2], ["9", "98"])
]


@pytest.mark.parametrize("number,input_data,expected_result", test_data)
def test_wizard_of_orz(number: int, input_data: List[int], expected_result: List[str]):
    assert expected_result == wizard_of_orz(number, input_data)
