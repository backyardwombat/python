def get_length(dna):
    ''' (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    '''
    return len(dna)


def is_longer(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    '''
    return get_length(dna1) > get_length(dna2)



def count_nucleotides(dna, nucleotide):
    ''' (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    '''
    num_nucleotides = 0
    for char in dna:
        if char in nucleotide:
            num_nucleotides = num_nucleotides + 1
    return num_nucleotides



def contains_sequence(dna1, dna2):
    ''' (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    
    '''
    return dna2 in dna1    

def is_valid_sequence(dna):
    ''' (str) -> bool

    Return True if and only if the DNA sequence is valid (this is, it contains
    no characters other than 'A', 'T', 'C' and 'G').Lower case characters are
    not valid.

    >>> is_valid_sequence('ACTGAGCT')
    True
    >>> is_valid_sequence('ABTC')
    False
    >>> is_valid_sequence('aGTc')
    False
    '''
    valid_sequence = True
    for char in dna:
        if char not in "ATCG": valid_sequence = False
    return valid_sequence

def insert_sequence(dna1, dna2, index):
    ''' (str, str, int) -> str

    Return the DNA sequence obtained by inserting dna2 into dna1 at index.
    Assumes that the index is valid.

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'ATACG', 0)
    'ATACGCCGG'
    >>> insert_sequence('CCGG', 'CAGT', -1)
    'CCGCAGTG'
    '''
    return dna1[:index] + dna2 + dna1[index:]

def get_complement(nucleotide):
    ''' (str) -> str

    Return the complement of nucleotide.

    >>> get_complement('C')
    G
    >>> get_complement('A')
    T
    >>> get_complement('G')
    C
    '''
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'G':
        return 'C'
    else:
        return ''
    
def get_complementary_sequence(dna):
    ''' (str) -> str

    Return the complement of DNA sequence dna.

    >>> get_complementary_sequence('AT')
    'TA'
    >>> get_complementary_sequence('GACT')
    'CTGA'
    >>> get_complementary_sequence('TTAGCG')
    'AATCGC'
    '''
    dna_complement = ''
    for char in dna:
        dna_complement = dna_complement + get_complement(char)
    return dna_complement
