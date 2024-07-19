from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    s = ''.join(char.lower() for char in s if char.isalnum())

    # Додамо символи до двосторонньої черги
    char_deque = deque(s)

    # Порівняємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Приклади використання
print(is_palindrome("Я несу гусеня"))  # True
print(is_palindrome("Лев і олово, воло і вел"))  # True
print(is_palindrome("Слава, Україні!"))  # False

