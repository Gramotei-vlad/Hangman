#!/bin/python3
from hangman import Game


def test_1():
    game = Game()
    word_1 = 'look'
    char = 'o'
    game.visible_word = ['*', '*', '*', '*']
    game.remains = len(word_1)
    result = game._check_word(word_1, char)
    assert result == 'Hit!', 'Wrong method output'
    assert game.remains == 2 and game.curr_mistake == 0, 'Wrong counters'
    assert game.visible_word == ['*', 'o', 'o', '*'], 'Wrong word output'
    print('TEST 1 is OK')


def test_2():
    game = Game()
    word = 'qwerr'
    char = 'l'
    game.visible_word = ['*', '*', '*', '*', '*']
    game.remains = len(word)
    result = game._check_word(word, char)
    assert result == 'Missed, mistake 1 out of 5', 'Wrong method output'
    assert game.remains == len(word) and game.curr_mistake == 1, 'Wrong counters'
    assert game.visible_word == ['*', '*', '*', '*', '*'], 'Wrong word output'
    print('TEST 2 is OK')


def test_3():
    game = Game()
    word = 'apple'
    char = 'a'
    game.visible_word = ['*', '*', '*', '*', '*']
    game.remains = len(word)
    result = game._check_word(word, char)
    assert result == 'Hit!', 'Wrong method output'
    assert game.remains == 4 and game.curr_mistake == 0, 'Wrong counters'
    assert game.visible_word == ['a', '*', '*', '*', '*'], 'Wrong word output'
    print('TEST 3 is OK')


def test_4():
    game = Game()
    word = 'rrrrr'
    char = 'r'
    game.visible_word = ['*', '*', '*', '*', '*']
    game.remains = len(word)
    result = game._check_word(word, char)
    assert result == 'Hit!', 'Wrong method output'
    assert game.remains == 0 and game.curr_mistake == 0, 'Wrong counters'
    assert game.visible_word == ['r', 'r', 'r', 'r', 'r'], 'Wrong word output'
    print('TEST 4 is OK')


def test_5():
    game = Game()
    game.curr_mistake = 5
    result = game.play()
    assert result == 'You lost!', 'Wrong game result'
    print('TEST 5 is OK')


def start_tests():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()


start_tests()