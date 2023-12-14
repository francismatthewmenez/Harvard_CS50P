from bank import value


def test_value_0():
    assert value("hello world") == 0
    assert value("HELLOOOOOO") == 0

def test_value_20():
    assert value("hi world") == 20
    assert value("How's it going?") == 20


def test_value_100():
    assert value("this is CS50!") == 100
    assert value("GOOD MORNING to YOUUU!") == 100


# Until I found the correct test cases, I only realized that I was using the wrong ones the whole time.
# Make sure that you use the test cases I have here (or in the same format as that, doesn't have to be mine)
# Don't just use any test case you want; you might get that yellow text error. And you don't want that.


