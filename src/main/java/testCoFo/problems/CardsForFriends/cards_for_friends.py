from typing import List


def cards_for_friends(number: int, cases: List[List[int]]) -> List[str]:
    result: List[str] = []
    for index in range(0, number):
        width: int = cases[index][0]
        height: int = cases[index][1]
        number_of_recipients: int = cases[index][2]
        if number_of_recipients < 2:
            result.append('YES')
            continue
        width_number = 1
        while width > 2:
            if width % 2 == 0:
                width_number += 1
            else:
                break
        height_number = 1
        while height > 2:
            if height % 2 == 0:
                height_number += 1
            else:
                break
        result.append('YES' if width_number * height_number >=
                      number_of_recipients else 'NO')
    return result
