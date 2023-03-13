"""
Name: Keith Crawford
Date: 02/04/23
"""
from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    kcsingle_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        kcword = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the kcsingle_determiners list.
        assert kcword in kcsingle_determiners

    # 2. Test the plural determiners.

    kcplural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        kcword = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the kcplural_determiners list.
        assert kcword in kcplural_determiners

def test_get_noun():
    # 1. Test the single nouns.

    kcsingle_noun = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_noun function which
        # should return a single determiner.
        kcword = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the kcsingle_noun list.
        assert kcword in kcsingle_noun

    # 2. Test the plural nouns.

    kcplural_noun = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_noun function which
        # should return a plural noun.
        kcword = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the kcplural_noun list.
        assert kcword in kcplural_noun

def test_get_verb():
    # 1. Test the single and past tense verbs.
    
    kcsingle_verb_past = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(11):

        # Call the get_verb function which
        # should return a single verb.
        kcword = get_verb(1, "past")

        # Verify that the word returned from get_verb
        # is one of the words in the kcsingle_verb_past list.
        assert kcword in kcsingle_verb_past

    # 2. Test the single and present tense verbs

    kcsingle_verb_present = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_verb function which
        # should return a single verb.
        kcword = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the kcsingle_verb_present list.
        assert kcword in kcsingle_verb_present

    # 3. Test the plural and present tense verbs

    kcplural_verb_present = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 11 times.
    for _ in range(11):

        # Call the get_verb function which
        # should return a plural verb.
        kcword = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the kcplural_verb_present list.
        assert kcword in kcplural_verb_present

    # 4. Test the future verbs.

    kcfuture_verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(11):

        # Call the get_verb function which
        # should return a future verb.
        kcword = get_verb(1 or 2, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the kcfuture_verb list.
        assert kcword in kcfuture_verbs
def test_get_preposition():
    #Test the prepositions
    
    kcpreposition_words= ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    # This loop will repeat the statements inside it 31 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(31):

        # Call the get_preposition function which
        # should return a preposition.
        kcword = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the kcpreposition_words list.
        assert kcword in kcpreposition_words

    
def test_get_prepositional_phrase():
    # Call and verify the get_prepositional_phrase function which
    # should return 3 words (preposition, determiner, noun)
    kcword = get_prepositional_phrase(1 or 2)
    kcword.split(" ")==3

def test_get_adjective():
    #Testing to see if the sentence contains an adjective

    kcadjective_words= ["blue", "blind", "fast", "deaf", "smart", "dark", "light", "strong", "loose"]

     # This loop will repeat the statements inside it 11 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(10):

        # Call the get_preposition function which
        # should return an adjective.
        kcword = get_adjective()

        # Verify that the word returned from get_preposition
        # is one of the words in the kcpreposition_words list.
        assert kcword in kcadjective_words

     
       
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])