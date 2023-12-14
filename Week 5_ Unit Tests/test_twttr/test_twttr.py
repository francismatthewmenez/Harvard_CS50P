from twttr import shorten

def test_1():
    assert shorten("twitter") == "twttr"

def test_2():
    assert shorten("apple") == "ppl"

def test_3():
    assert shorten("Skibidi toilet") == "Skbd tlt"

def test_4():
    assert shorten("THEY SEE ME ROLLING") == "THY S M RLLNG"

def test_5():
    assert shorten("Killarney Secondary School") == "Kllrny Scndry Schl"

def test_6():
    assert shorten("AEIOUaeiou") == ""

def test_7():
    assert shorten("When? Oh, don't worry. My number is 6969") == "Whn? h, dn't wrry. My nmbr s 6969"







