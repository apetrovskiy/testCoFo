from typing import List


def fair_division(number: int, cases: List[List[int]]) -> List[str]:
    return ['YES' if calculate_candies(cases[index][0][0], cases[index][1]) == True else 'NO' for index in range(0, number)]


def calculate_candies(number_of_candies: int, weights: List[int]) -> bool:
    sum_of_weights = sum(weights)
    if sum_of_weights % 2 == 1:
        return False
    
    return True
