"""
Name: Keith Crawford
Date: 02/01/23
"""
from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Keith", "Crawford")== "Crawford; Keith"
    assert make_full_name("Mike", "Jordan")== "Jordan; Mike"
    assert make_full_name("LeRoy", "James")== "James; LeRoy"
    assert make_full_name("Tom", "Goat")== "Goat; Tom"
    assert make_full_name("In-fant", "Bouchelor")== "Bouchelor; In-fant"
    assert make_full_name("Returnoftheking", "Don'tsleeponmyboy")=="Don'tsleeponmyboy; Returnoftheking"

def test_extract_family_name():
    assert extract_family_name("Crawford; Keith")== "Crawford"
    assert extract_family_name("Jordan; Mike")== "Jordan"
    assert extract_family_name("James; LeRoy")== "James"
    assert extract_family_name("Goat; Tom")== "Goat"
    assert extract_family_name("Bouchelor; In-fant")== "Bouchelor"
    assert extract_family_name("Don'tsleeponmyboy; Returnoftheking")== "Don'tsleeponmyboy"

def test_extract_given_name():
    assert extract_given_name("Crawford; Keith")== "Keith"
    assert extract_given_name("Jordan; Mike")== "Mike"
    assert extract_given_name("James; LeRoy")== "LeRoy"
    assert extract_given_name("Goat; Tom")== "Tom"
    assert extract_given_name("Bouchelor; In-fant")== "In-fant"
    assert extract_given_name("Don'tsleeponmyboy; Returnoftheking")== "Returnoftheking"

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
