# Hangman
[![Build Status](https://travis-ci.org/Gramotei-vlad/Hangman.svg?branch=master)](https://travis-ci.org/Gramotei-vlad/Hangman)
[![codecov](https://codecov.io/gh/Gramotei-vlad/Hangman/branch/master/graph/badge.svg)](https://codecov.io/gh/Gramotei-vlad/Hangman)

## Описание
Реализация популярной игры Hangman или в простонародье "Виселица" на языке Python. По правилам игры компьютер в начале выбирает случайное слово из заранее заданного словаря, а игрок должен его отгадать. На каждом шаге пользователь вводит одну букву, а программа отвечает "Hit!" в случае, если эта буква присутствует в слове, и "Missed", если такой буквы нет. Максимальное количество ошибок от игрока - пять. В этом случае он считается проигравшим.

## Реализация
Все игровые данные (словарь, кол-во попыток и т.д.) хранятся в классе *Game* под соответствующими аттрибутами.
```python
class Game:
    def __init__(self):
        self.words = ['Milk', 'Car', 'Cheese', 'book', 'S', 'lll']
        self.mistakes = 5
        self.curr_mistake = 0
        self.visible_word = []
        self.remains = 0
```
Основной процесс игры происходит в методе *play*, который запрашивает букву у пользователя, делает вывод текущих угаданных букв в слове и возвращает результат игры (победа/поражение)
```python
def play(self):
    word = choice(self.words).lower()
    self.visible_word  = ['*' for _ in range(len(word))]
    self.remains = len(word)
    while self.curr_mistake < self.mistakes and self.remains > 0:
        print('Guess a letter: ')
        char = str(input()).lower()
        print(self._check_word(word, char))
        print()
        print('The word: ' + self._get_pred_word())
    return 'You win!' if self.remains == 0 else 'You lost!'
```
Метод *check_word* проверяет вхождение введенной игроком буквы в слове и возвращает результат в виде строки.
```python
def _check_word(self, word, pred_char):
    guess = False
    result = ''
    for idx, char in enumerate(word):
        if char == pred_char:
            self.visible_word[idx] = char
            guess = True
            result = 'Hit!'
            self.remains -= 1
    self.curr_mistake = self.curr_mistake + 1 if not guess else self.curr_mistake
    if not guess:
        result = 'Missed, mistake ' + str(self.curr_mistake) + ' out of ' + str(self.mistakes)
    return result
```

## Copyright
Copyright © 2020 Vladislav Kosukhin. See [license](https://github.com/Gramotei-vlad/Hangman/blob/master/LICENSE) for details.