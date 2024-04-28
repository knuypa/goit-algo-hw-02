from collections import deque
import string

def is_palindrome(s):
    # Підготовка рядка: видалення пробілів і переведення у нижній регістр
    formatted_string = ''.join(ch.lower() for ch in s if ch in string.ascii_letters or ch in string.digits)

    # Створення двосторонньої черги з символів рядка
    char_deque = deque(formatted_string)

    # Перевірка символів з обох кінців черги на співпадіння
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Приклади виклику функції
test_strings = ["A man a plan a canal Panama", "Racecar", "12321", "No palindrome", "Was it a car or a cat I saw?"]
results = {s: is_palindrome(s) for s in test_strings}
print(results)