from secret import SecretWord
from board import Board

class Game:
    """Run an entire game. 

    Initialization defines the player who pickers secret word and one or more guessers.
    play
       - picker picks the secret word from the dictionary held by all players
       - guessers guess in turn looking at the state of the board until the game is done
       - each guesser continues as long as they guess currect letters
       - returns final board
    winner returns the player who picked the last letter.

    >>> from wordset import Dictionary
    >>> from player import Player, DummyPlayer
    >>> p = Player(Dictionary("assets/lincoln.txt"))
    >>> game = Game(DummyPlayer("pick"), [ DummyPlayer("guess") ] )
    >>> board = game.play(False)
    >>> board.word()
    ['s', 'c', 'o', 'r', 'e']
    >>> len(board.guesses())
    6
    """
    def __init__(self, picker, guessers):
        # BEGIN
        self.picker = picker
        self.guessers = guessers
        self. win= None
        # END

    def play(self, verbose=True):
        # BEGIN
        self.word = self.picker.pick_word()
        a= SecretWord(self.word)
        b=Board(a)
        while self.win is None:
            for i in range(len(self.guessers)):
                same = self.guessers[i].guess(b)
                c= b.guess(same)
                if verbose:
                    b.display()
                while c != 0:
                    if not b.done():
                        same = self.guessers[i].guess(b)
                        c= b.guess(same)
                        if verbose:
                            b.display()
                    else:
                        self.win = self.guessers[i]
                        break
                if self.win is not None:
                        break
        return b
                
        # END

    def winner(self):
        # BEGIN
        return self.win
        # END



