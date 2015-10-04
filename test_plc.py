from lib.lang_featurizers import *


def test_presence_nil():
    assert presence_nil('') == 0
    assert presence_nil('Abinil') == 0
    assert presence_nil('nilitary?!') == 0
    assert presence_nil('ret == nil | ret == 0') == 1
    assert presence_nil('if ret == nil') == 1
