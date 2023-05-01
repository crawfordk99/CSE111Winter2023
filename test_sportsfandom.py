"""
Name:Keith Crawford
Date 03/26/23
To test functions from sportsfandom.py
"""
from sportsfandom import calculate_score, make_quiz
import pytest

def test_calculate_score():
    """Verify that the calculate_score method works correctly"""
    kctest_list= ["j", "5", "c", "f"]
    kctest_list2= ["fat", "calories", "oil", "sugar", "salt", "infinite", "house", "five", "jack"]
    assert calculate_score(kctest_list)== 4
    assert calculate_score(kctest_list2)== 9

def test_make_quiz():
    """Verify that the make_quiz function works correctly.
    Parameters: none
    Return: nothing
    """
    # Call the make_quiz function and store the returned
    # dictionary in a variable named kcquestions_dict.
    kcquestions_dict = make_quiz()

    # Verify that the make_quiz function returns a dictionary.
    assert isinstance(kcquestions_dict, dict), \
        "make_quiz function must return a dictionary: " \
        f" expected a dictionary but found a {type(kcquestions_dict)}"
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])