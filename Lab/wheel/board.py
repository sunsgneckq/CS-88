"""Board class for Wheel of Fortune game."""

class Board:
    """Board for Wheel of Fortune with attributes board and guessed.
    Attributes:
       board - list of correct characters or "_" in the secret word
       guessed - list of characters guessed so far

    >>> from secret import SecretWord
    >>> b = Board(SecretWord("bookkeeper"))
    >>> len(b)
    10
    >>> b.guess('o')
    2
    >>> b
    < _ o o _ _ _ _ _ _ _ : o >
    >>> b.done()
    False
    >>> b.guess('k')
    2
    >>> b
    < _ o o k k _ _ _ _ _ : o,k >
    >>> b.guess('j')
    0
    >>> b
    < _ o o k k _ _ _ _ _ : o,k,j >
    >>> b.word()
    ['_', 'o', 'o', 'k', 'k', '_', '_', '_', '_', '_']
    >>> b.guesses()
    ['o', 'k', 'j']
    """
    def __init__(self, secret):
        """Create an initial board with no guesses and a secret."""
        # BEGIN
        self.secret= secret
        self.guessed= []
        self.
        # END

    def __repr__(self):
        return '< ' + " ".join(self.word()) + " : " + ",".join(self.guesses()) + ' >'

    def __len__(self):
        return self.word_len()

    def word_len(self):
        """Return the length of the secret word."""
        # BEGIN
        return len(self.secret)
        # END

    def word(self):
        """Return the current state of guessing the word as a lsit of characters.
        Unguessed positions are represented by '_'
        Guessed positions hold the character.
        """
        # BEGIN
        lst = ['_' for i in self.secret.word]
        for i in self.secret.word:
            if i in self.hits():
                for k in self.secret.match(i):
                    lst[k] = i
        return lst
        # END

    def guesses(self):
        """Return a list of the characters guessed so far."""
        # BEGIN
        return [a for a in self.guessed]
        # END

    def hits(self):
        """Return a list of characters correctly guessed."""
        # BEGIN
        return [c for c in self.guessed if c in self.secret.word]
        # END

    def misses(self):
        """Return a list of characters incorrectly guessed."""
        # BEGIN
        return [c for c in self.guessed if c not in self.secret.word]
        # END

    def guess(self, char):
        """Update the board to reflect the guess of char.
        Return the number of indices in the secret word where char occurs.
        If char does not appear in the word, this will be 0.
        """
        # BEGIN
        count = 0
        for i in self.secret.word:
            if i == char:
                count+=1
        self.guessed+=[char]        
             
        return count
            
      
        
        # END

    def done(self):
        """Determine if the game is done."""
        # BEGIN
        if '_' in self.word():
            return False
        return True
        # END

    max_miss = 11
    # def miss_man(missed):
    #     missed = min(missed, Board.max_miss)
    #     return "assets/man{0}.txt".format(missed)

    def display(self):
        missed = len(self.misses())
        # path = Board.miss_man(missed)
        # with open(path) as fp:
        #     symbol = fp.read()
        # print(symbol)
        print(self.word())
        print("Guessed chars: ", self.guesses())
