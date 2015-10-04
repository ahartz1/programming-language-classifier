from lib.lang_featurizers import *


def test_presence_nil():
    assert presence_nil('') == 0
    assert presence_nil('Abinil') == 0
    assert presence_nil('nilitary?!') == 0
    assert presence_nil('ret == nil | ret == 0') == 1
    assert presence_nil('if ret == nil') == 1


def test_presence_nil_caps():
    assert presence_nil_caps('') == 0
    assert presence_nil_caps('AbiNIL') == 0
    assert presence_nil_caps('NILitary?!') == 0
    assert presence_nil_caps('ret == NIL | ret == 0') == 1
    assert presence_nil_caps('if ret == NIL') == 1


def test_presence_null():
    assert presence_null('') == 0
    assert presence_null('Abinull') == 0
    assert presence_null('nullitary?!') == 0
    assert presence_null('ret == null | ret == 0') == 1
    assert presence_null('if ret == null') == 1


def test_presence_none():
    assert presence_none('') == 0
    assert presence_none('AbiNone') == 0
    assert presence_none('Nonegon?!') == 0
    assert presence_none('ret == None | ret == 0') == 1
    assert presence_none('if ret == None') == 1


def test_presence_start_double_semicolons():
    assert presence_start_double_semicolons('') == 0
    assert presence_start_double_semicolons('Abinull;;') == 0
    assert presence_start_double_semicolons('nullit;;ary?!') == 0
    assert presence_start_double_semicolons(';; ret == null | ret == 0') == 1
    assert presence_start_double_semicolons('\n;;if ret == null') == 1


def test_presence_start_hashes():
    assert presence_start_hashes('') == 0
    assert presence_start_hashes('Abinull#') == 0
    assert presence_start_hashes('nullit#ary?!') == 0
    assert presence_start_hashes('# ret == null | ret == 0') == 1
    assert presence_start_hashes('\n#if ret == null') == 1


def test_presence_bar_hash():
    assert presence_bar_hash('') == 0
    assert presence_bar_hash('Abinull|#') == 0
    assert presence_bar_hash('nullit|#ary?!') == 0
    assert presence_bar_hash('|# ret == null |\n#| ret == 0') == 1
    assert presence_bar_hash('\n|#if ret == null\n#|') == 1


def test_percent_start_and_end_parenthesis():
    assert percent_start_and_end_parenthesis('') == 0
    assert percent_start_and_end_parenthesis('(Abinull') == 0
    assert percent_start_and_end_parenthesis('nullitary?!)') == 0
    assert percent_start_and_end_parenthesis('(nullit)ary?!') == 0
    assert percent_start_and_end_parenthesis('( ret == null | ret == 0)') == 1
    assert percent_start_and_end_parenthesis('\n(#if null)\nhi\nhi') == 0.25


def test_longest_run_of_parenthesis():
    assert longest_run_of_parenthesis('none') == 0
    assert longest_run_of_parenthesis('(one)') == 0
    assert longest_run_of_parenthesis('\n(one)\n') == 0
    assert longest_run_of_parenthesis('(one(two))') == 2
    assert longest_run_of_parenthesis('(one(two(three)))') == 3
    assert longest_run_of_parenthesis('(1(2))\n(1(2(3)))') == 3


def test_longest_run_of_curly_braces():
    assert longest_run_of_curly_braces('none') == 0
    assert longest_run_of_curly_braces('{one}') == 0
    assert longest_run_of_curly_braces('\n{one}\n') == 0
    assert longest_run_of_curly_braces('{one{two}}') == 2
    assert longest_run_of_curly_braces('{one{two{three}}}') == 3
    assert longest_run_of_curly_braces('{1{2}}\n{1{2{3}}}') == 3


def test_presence_void():
    assert presence_void('') == 0
    assert presence_void('Abivoid') == 0
    assert presence_void('voiditary?!') == 0
    assert presence_void('ret == void | ret == 0') == 1
    assert presence_void('if ret == void') == 1


def test_presence_public():
    assert presence_public('') == 0
    assert presence_public('Abipublic') == 0
    assert presence_public('publicitary?!') == 0
    assert presence_public('ret == public | ret == 0') == 1
    assert presence_public('if ret == public') == 1


def test_presence_bool():
    assert presence_bool('') == 0
    assert presence_bool('Abibool') == 0
    assert presence_bool('boolitary?!') == 0
    assert presence_bool('ret == bool | ret == 0') == 1
    assert presence_bool('if ret == bool') == 1










#
