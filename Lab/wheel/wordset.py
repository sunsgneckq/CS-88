from utils import lowercase, key_of_max
import string
from collections import OrderedDict    # Variant of dict that you might want to learn about

#
# WordSet class
#
class WordSet:
    """Set of unique words, all in lower case and of positive length.

    >>> WordSet("one two, Two. tHree").words()
    ['one', 'three', 'two']
    >>> WordSet(["one","two","Two", ""]).words()
    ['one', 'two']
    >>> 'two' in WordSet(["one","two","Two"])
    True
    """
    def __init__(self, text):
        """Form a WordSet from a string of words or collection of words.
        """
        # BEGIN Question 2
        self.text = text
        self.word_set = []
        # END Question 2

    def words(self):
        """Return sorted list of words in WordSet.

        >>> WordSet("Hi. Hey you. How, the heck, are you?").words()
        ['are', 'heck', 'hey', 'hi', 'how', 'the', 'you']
        """
       
        # BEGIN Question 2      
        exclude = set(string.punctuation)
        if type(self.text) == str: 
            a = ''.join(x for x in self.text if x not in exclude)
            b = lowercase(a).split()
            c = set(b)
            self.word_set = sorted(list(c))
            return  self.word_set
        elif type(self.text) == list:
            self.text = filter(None, self.text)
            for i in self.text:           
                e = lowercase(i)
                self.word_set.append(e)
            f = set(self.word_set)
            self.word_set = sorted(list(f))
            return self.word_set
        # END Question 2

    def __contains__(self, word):
        # BEGIN Question 2
        if word in self.text:
            return True
        # END Question 2


#
# Dictionary class
#
class Dictionary(WordSet):
    """Construct a dictionary from all the words in a text file.
    Subclass of WordSet with a file based initializer.

    >>> from wordset import Dictionary
    >>> Dictionary('assets/lincoln.txt').words()[55]
    'government'
    """
    def __init__(self, filename):
        with open(filename) as fp:
            text = fp.read()
            WordSet.__init__(self, text)

#
# WordMunch class
#
class WordMunch(WordSet):
    """Perform analytics on a set of unique words.

    Subclass of WordSet that provides analytics on the words.

    >>> w = WordMunch("one two, Two. tHree")
    >>> w.words()
    ['one', 'three', 'two']
    >>> w.frequency()['o']
    2
    >>> key_of_max(w.frequency())
    'e'
    """
    def filter(self, ffun):
        """Filter set to include only those that satisfy the filter function predicate."""
        # BEGIN
        filtered = []
        for word in self.words():
            if ffun(word):
                filtered += [word]
        # END

    def frequency(self):
        """Return an ordered dictionary of the frequency of each letter in the word set."""
        # BEGIN
        ordered_dict = {}
        for i in self.words():
            for letter in i:
                ordered_dict[letter] = 0
        for i in self.words():
            for letter in i:
                ordered_dict[letter] += 1
        return ordered_dict
        # END
