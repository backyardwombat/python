'''A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
'''


def is_valid_word(wordlist, word):
    ''' (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'FROM')
    False
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO', 'BOX'], 'BOX')
    True
    '''
    word_exists = False
    for list_word in wordlist:
        if list_word == word:
            word_exists = True
    return word_exists


def make_str_from_row(board, row_index):
    ''' (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    >>>  make_str_from_row([['A', 'N'], ['T', 'T'], ['X', 'S'], ['O', 'B']], 3)
    OB
    '''
    word = ''
    for char in board[row_index]:
        word = word + char
    return word

def make_str_from_column(board, column_index):
    ''' (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2)
    'TO'
    >>> make_str_from_column([['A', 'N'], ['T', 'T'], ['X', 'S'], ['O', 'B']], 1)
    'NTSB'
    '''
    word = ''
    for row in board:
        word = word + row[column_index]
    return word


def board_contains_word_in_row(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    '''
    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    ''' (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    '''
    bcwic = False
    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            bcwic = True
    return bcwic
                              

def board_contains_word(board, word):
    '''(list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TAN')
    False
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    '''
    return board_contains_word_in_column(board, word) or board_contains_word_in_row(board, word)


def word_score(word):
    '''(str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character in word
                 7-9: 2 points per character in word
                 10+: 3 points per character in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('ASSOCIATES')
    30
    >>> word_score('TO')
    0
    >>> word_score('FOR')
    3
    '''
    word_len = len(word)
    if word_len >= 10:
        return word_len * 3
    elif word_len >= 7:
        return word_len * 2
    elif word_len >= 3:
        return word_len
    else:
        return 0

def update_score(player_info, word):
    '''([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    '''
    player_info[1] = player_info[1] + word_score(word)

def num_words_on_board(board, words):
    '''(list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    '''
    words_on_board = 0
    for word in words:
        if board_contains_word(board, word):
            words_on_board = words_on_board + 1
    return words_on_board

def read_words(words_file):
    ''' (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.

    >>> read_words('wordlist1.txt')
    ['CRUNCHY', 'COWS', 'EAT', 'GRASS']
    '''
    return words_file.read().splitlines()
    '''return open(words_file, 'r').readlines()'''


def read_board(board_file):
    ''' (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    
    >>>read_board('board2.txt')
    [['E','F','J'], ['S','D','G'], ['A','S','R']]
    >>>read_board('board1.txt')
    [['E','F','J','A','J','C','O','W','S','S'], ['S','D','G','K','S','R','F','D','F','F'], ...
    '''
    word_list = read_words(board_file)
    board_list = [] 
    for i in range(len(word_list)):
        inner_list = []
        for char in word_list[i]:
            inner_list.append(char)
        board_list.append(inner_list)
    return board_list

