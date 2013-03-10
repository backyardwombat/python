#!/usr/bin/env python3
from tkinter.filedialog import askopenfile

import a3

words_file = askopenfile(mode='r', title='Select word list file')
words = a3.read_words(words_file)
