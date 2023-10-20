import pytest
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'wolfgang amadeus mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    assert formatted_name == 'Wolfgang Amadeus Mozart'