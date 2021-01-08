def get_integer():
    return int(input())


def get_list_int():
    input_list = list(input().split(' '))
    return [int(x) for x in input_list]

print(get_integer())
print(get_integer())
print(get_list_int())
