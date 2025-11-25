"""
Project 00: Статистический калькулятор
Реализуй функции для вычисления базовой статистики
"""
from typing import List
from math import sqrt

def mean(numbers: List[float]) -> float:
    """Вычисляет среднее значение списка чисел"""
    try:
        if not numbers:
            raise ValueError("Список не может быть пустым")
        return sum(numbers) / len(numbers)
    except TypeError as e:
        raise TypeError(f"Все элементы должны быть числами: {e}")

def median(numbers: List[float]) -> float:
    """Вычисляет медиану списка чисел"""
    sorted_list = sorted(numbers, key=None, reverse=False)
    try:
        if not numbers:
            raise ValueError("Список не может быть пустым")
        length = len(sorted_list)
        if length % 2 != 0:
            return sorted_list[length // 2]
        else:
            sub_sorted_list = sorted_list[length // 2 - 1 : length // 2 + 1]
            return mean(sub_sorted_list)
    except TypeError as e:
        raise TypeError(f"Все элементы должны быть числами: {e}")

def standard_deviation(numbers: List[float]) -> float:
    """Вычисляет стандартное отклонение"""
    mean_value = mean(numbers)
    new_list = [(i - mean_value) ** 2 for i in numbers]
    mean_square = mean(new_list)
    return sqrt(mean_square)

def doit(numbers: list[float]) -> None:
    #print("Тестовые данные:", numbers)
    print("Среднее:", mean(numbers))
    print("Медиана:", median(numbers))
    print("Стандартное отклонение:", standard_deviation(numbers))

# Тестовые данные для проверки
if __name__ == "__main__":
    test_data = [100, 150, 200, 180, 220, 190, 210, 170, 160, 140]
    print("Тестовые данные:", test_data)
    print("Среднее:", mean(test_data))
    print("Медиана:", median(test_data))
    print("Стандартное отклонение:", standard_deviation(test_data))
