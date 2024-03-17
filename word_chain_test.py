import word_chain

def test_word_chain_0_words():
    # setup
    a_string = ""
    expected = False

    # invoke
    actual = word_chain.is_word_chain(a_string)

    # analyze
    assert actual == expected

def test_word_chain_1_word():
    # setup
    a_string = "Parrot"
    expected = False

    # invoke
    actual = word_chain.is_word_chain(a_string)

    # analyze
    assert actual == expected

def test_word_chain_2_words_true():
    # setup
    a_string = "Parent Trap"
    expected = True

    # invoke
    actual = word_chain.is_word_chain(a_string)

    # analyze
    assert actual == expected

def test_word_chain_2_words_false():
    # setup
    a_string = "Party Animal"
    expected = False

    # invoke
    actual = word_chain.is_word_chain(a_string)

    # analyze
    assert actual == expected

def test_word_chain_long_true():
    # setup
    a_string = "Luke Endor Rey Y-Wing Geonosis sith Hutt Tatooine"
    expected = True

    # invoke
    actual = word_chain.is_word_chain(a_string)

    # analyze
    assert actual == expected

def test_word_chain_long_false():
    # setup
    a_string = "Fries Shake Eat Tomato Burger"
    expected = False

    # invoke
    actual = word_chain.is_word_chain(a_string)

    # analyze
    assert actual == expected