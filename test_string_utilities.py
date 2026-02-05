from string_utilities import reverse_String,check_palidrome,count_vowels

def test_reverse_string():
    assert reverse_String("dharshini") == "inihsrahd"

def test_check_palidrome():
    assert check_palidrome("aba") == True

def test_count_vowels():
    assert count_vowels("dharshini") == 3