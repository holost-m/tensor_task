from functools import reduce
import time
from typing import Iterable

file_in_name: str = 'e.in.txt'
file_out_name: str = 'e.out.txt'

def make_intersection_set(args: Iterable[int]) -> set:
    """
        Создает множество, полученное
        в результате пересечения множеств,
        полученных из элементов коллекции
    """
    x = reduce(lambda x, y: set(x).intersection(y), args)

    return x

def find_divisors(number: int, args: Iterable[int]) -> int:
    """
        Находит количество делимых на number из коллеции args
    """
    sum1: int = 0
    for i in args:
        if i % number == 0:
            sum1 += 1
    return sum1


def find_res(args: Iterable[int]) -> int:
    """
        Находит финальный результат
    """
    lst = sorted(args)
    length: int = lst[-1]
    res: int = length
    for i in range(len(lst)):
        if length % lst[i] == 0:
            count_of_division = (length / lst[i]) - 1
            if count_of_division == find_divisors(lst[i], lst[i+1:]):
                res = lst[i]
                break
    return res

def get_dct_indexes(lst_numbers) -> dict:
    """
    Формирует словарь , где ключами будут являтся
    встречающиеся в последовательности числа, а значениями индексы этого числа
    """
    dct_indexes: dict[int, list] = {}

    for i in range(len(lst_numbers) - 1):
        num: int = lst_numbers[i]
        dct_indexes[num] = dct_indexes.get(num, []) + [i]

    return dct_indexes


def get_dct_diff(dct_indexes: dict[int, list]) -> dict:
    """
    Формируем словарь dct_diff, где ключами будут являтся
    встречающиеся в последовательности числа,
    а значениями списки разностей индексов этого числа с первым индексом
    """
    dct_diff: dict[int, list] = {}
    for k, v in dct_indexes.items():
        first: int = v[0]
        dct_diff[k] = []
        for j in v[1:]:
            delta: int = j - first
            dct_diff[k].append(delta)

    return dct_diff


def main() -> None:
    # чтение из файла
    with open(file_in_name, 'r', encoding='utf-8') as file:
        total_count: int = int(file.readline()) # первое число
        lst_numbers: list[int] = list(map(int, file.readline().split()))
        length: int = len(lst_numbers) - 1  # Длинна последовательности чисел

    # основные операции
    dct_indexes: dict[int, list] = get_dct_indexes(lst_numbers)
    if len(dct_indexes) == 1:
        result: str = '1'
    else:

        dct_diff: dict[int, list] = get_dct_diff(dct_indexes)
        total_set: set = make_intersection_set(dct_diff.values())
        total_set.add(length)

        # находим количество чисел на барабане
        result: str = str(find_res(total_set))

    # запись результата в файл
    with open(file_out_name, "w", encoding='utf-8') as output:
        output.write(result)


if __name__ == '__main__':
    main()