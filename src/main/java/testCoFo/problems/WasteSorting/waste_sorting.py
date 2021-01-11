from typing import List


def waste_sorting(number: int, cases: List[List[int]]) -> List[str]:
    return ['YES' if calculate_waste(cases[index][0], cases[index][1]) == True else 'NO' for index in range(0, number)]


def calculate_waste(containers: List[int], waste: List[int]) -> bool:
    c1, c2, c3 = containers
    a1, a2, a3, a4, a5 = waste
    result3 = a3 <= c3
    result1 = a1 + a4 + a3 <= c1 + c3 and a1 <= c1 and a3 <= c3
    result2 = a2 + a5 + a3 <= c2 + c3 and a2 <= c2 and a3 <= c3
    print(result1, result2, result3)
    return result1 and result2 and result3
