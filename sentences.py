"""
Name: Keith Crawford
Date: 02/01/23
"""
import random



def get_determiner(kcquantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity is 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity is 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if (kcquantity) == 1:
        kcwords = ["a", "one", "the"]
    else:
        kcwords = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    kcword = random.choice(kcwords)
    return kcword

def get_noun(kcquantity):
    """Return a randomly chosen noun.
    If quantity is 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if (kcquantity) == 1:
        kcwords = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        kcwords = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a determiner.
    kcword = random.choice(kcwords)
    return kcword

def get_verb(kcquantity, kctense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        kcquantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    
    if (kctense== "past"):
        kcwords = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif (kcquantity) == 1 and (kctense== "present"):
        kcwords = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif (kcquantity) == 2 and (kctense== "present"):
        kcwords= ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        kcwords= ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]    
    
    # Randomly choose and return a verb.
    kcword = random.choice(kcwords)
    return kcword

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    kcwords= ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    kcword = random.choice(kcwords)
    return kcword



def get_prepositional_phrase(kcquantity):
    """Build and return a prepositional phrase composed
    of three words: a preposition, a determiner, and a
    noun by calling the get_preposition, get_determiner,
    and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and noun in the prepositional
            phrase returned from this function should
            be single or pluaral.
    Return: a prepositional phrase.
    """
    kcdeterminer= get_determiner(kcquantity)
    kcnoun= get_noun(kcquantity)
    kcprepositional= get_preposition()
    kcphrase=(f"{kcprepositional} {kcdeterminer} {kcnoun}")
    return kcphrase

def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
        "blue", "blind", "fast", "deaf", "smart", "dark", "light", "strong", "loose"


    Return: a randomly chosen preposition.
    """
    kcwords= ["blue", "blind", "fast", "deaf", "smart", "dark", "light", "strong", "loose"]
    kcword = random.choice(kcwords)
    return kcword

def main(kcquantity, kctense):
    """
    The main function where all the other functions will be called
    Parameters: kcquantity= Single or Plural
    kctense= the verb tense, past, present or future
    """

    #Calling the other functions here
    kcdeterm= get_determiner(kcquantity)
    kcnoun= get_noun(kcquantity)
    kcverb= get_verb(kcquantity, kctense)
    kcprepositional_phrase= get_prepositional_phrase(kcquantity)
    kcadjective= get_adjective()
    print(f"{kcdeterm.capitalize()} {kcadjective} {kcnoun} {kcverb} {kcprepositional_phrase}.")
# If this file is executed like this:
# > python program.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main(1, "past")
    main(1, "present")
    main(1, "future")
    main(2, "past")
    main(2, "present")
    main(2, "future")