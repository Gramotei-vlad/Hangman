"""
    Module for implementation Hangman game
"""

from random import choice



class Game:
    """
       Class for implementation Hangman game
       Attrs:
           self.words (list) - list of possible words;
           self.mistakes (int) - amount of attempts;
           self.curr_mistake (int) - current amount of mistakes
           self.visible_words (list) - word for showing to a player
           self.remains (int) - amount of chars that need to guess
    """
    def __init__(self):
        self.words = ['Milk', 'Car', 'Cheese', 'book', 'S', 'lll']
        self.mistakes = 5
        self.curr_mistake = 0
        self.visible_word = []
        self.remains = 0

    def _check_word(self, word, pred_char):
        """
           Check occurrence 'pred_char' in word
           Args:
              word (str) - word that need to guess
              pred_char (str) - input char
           Returns:
              result (str) - output message to player
        """
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

    def _get_pred_word(self):
        """
           List to str method
           Returns:
               (str) - word that need to guess
        """
        return "".join(self.visible_word)

    def play(self):
        """
           Main loop of game
           Player inputs a char and game checks whether a char in a word
           Returns:
               (str) - output message with result
        """
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
        