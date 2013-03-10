def has_vowel(s):
    """(str) -> bool
    
    Return True if and only if s has at least one vowel, not including y.
    
    >>> has_vowel("Anniversary")
    True
    >>> has_vowel("xyz")
    False
    """
    vowel_found = False
    for char in s:
        if char in 'aeiouAEIOU': vowel_found = True
    return vowel_found
