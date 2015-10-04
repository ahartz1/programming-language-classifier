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


def test_presence_paren_define():
    assert presence_paren_define('') == 0
    assert presence_paren_define('Abi(define') == 0
    assert presence_paren_define('(defineitary?!') == 0
    assert presence_paren_define('\n\t(define | ret == 0)') == 1  # TODO: 0
    assert presence_paren_define('\n\t(define | (ret) == 0)') == 1  # TODO: 0
    assert presence_paren_define('\n\t(define | ret == 0') == 1
    assert presence_paren_define('\n(define-lib') == 1
    assert presence_paren_define('\n(define-lib (part)') == 1


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


def test_presence_int():
    assert presence_int('') == 0
    assert presence_int('Abiint') == 0
    assert presence_int('intitary?!') == 0
    assert presence_int('ret == int | ret == 0') == 1
    assert presence_int('if ret == int') == 1


def test_presence_module_line():
    assert presence_module_line('') == 0
    assert presence_module_line('Abimodule') == 0
    assert presence_module_line('moduleitary?!') == 0
    assert presence_module_line('\n    module Pork\n') == 1
    assert presence_module_line('module Pork') == 1


def test_presence_extend_line():
    assert presence_extend_line('') == 0
    assert presence_extend_line('Abiextend') == 0
    assert presence_extend_line('extenditary?!') == 0
    assert presence_extend_line('\n    extend Pork::Pie\n') == 1
    assert presence_extend_line('extend Pork::Pie') == 1


def test_presence_require_line():
    assert presence_require_line('') == 0
    assert presence_require_line('Abirequire') == 0
    assert presence_require_line('requireitary?!') == 0
    assert presence_require_line('\n    require pork\n') == 1
    assert presence_require_line('require pork') == 1


def test_presence_end():
    assert presence_end('') == 0
    assert presence_end('Abiend') == 0
    assert presence_end('enditary?!') == 0
    assert presence_end('before the end') == 0
    assert presence_end('\n  end') == 1
    assert presence_end('\nend\n') == 1


def test_presence_multiple_end():
    assert presence_multiple_end('') == 0
    assert presence_multiple_end('Abiend') == 0
    assert presence_multiple_end('enditary?!') == 0
    assert presence_multiple_end('before the end') == 0
    assert presence_multiple_end('\nend') == 0
    assert presence_multiple_end('\n  end\nend\n') == 1
    assert presence_multiple_end('\nend\nend') == 1


def test_presence_def_no_colon():
    assert presence_def_no_colon('') == 0
    assert presence_def_no_colon('Abidef') == 0
    assert presence_def_no_colon('defitary?!') == 0
    assert presence_def_no_colon('before the def') == 0
    assert presence_def_no_colon('\ndef no_colon:') == 0
    assert presence_def_no_colon('\n  def i_work\n') == 1
    assert presence_def_no_colon('\ndef i_work') == 1


def test_presence_at():
    assert presence_at('') == 0
    assert presence_at('Abi@tus') == 0
    assert presence_at('@@') == 0
    assert presence_at('\n  @end') == 1
    assert presence_at('\n@end\n') == 1


def test_presence_double_at():
    assert presence_double_at('') == 0
    assert presence_double_at('Abi@@tus') == 0
    assert presence_double_at('@') == 0
    assert presence_double_at('\n  @@end') == 1
    assert presence_double_at('\n@@end\n') == 1


def test_presence_puts():
    assert presence_puts('') == 0
    assert presence_puts('Abiputs') == 0
    assert presence_puts('putsitary?!') == 0
    assert presence_puts('before the puts') == 1
    assert presence_puts('\n  puts "open"') == 1
    assert presence_puts('\nputs tippy\n') == 1


def test_presence_dot_times():
    assert presence_dot_times('') == 0
    assert presence_dot_times('Abitimes') == 0
    assert presence_dot_times('.times with nothing before') == 0
    assert presence_dot_times('\n  end.times') == 1
    assert presence_dot_times('\n1..100.times\n') == 1


def test_presence_paren_defn():
    assert presence_paren_defn('') == 0
    assert presence_paren_defn('Abidefn') == 0
    assert presence_paren_defn('defnitary?!') == 0
    assert presence_paren_defn('before the (defn') == 0
    assert presence_paren_defn('\ndefn no paren') == 0
    assert presence_paren_defn('\n  (defn no_colon\n') == 1
    assert presence_paren_defn('\n(defn i_work') == 1


def test_presence_taskloop():
    assert presence_taskloop('') == 0
    assert presence_taskloop('AbitaskLoop') == 0
    assert presence_taskloop('taskLoopnitary?!') == 0
    assert presence_taskloop('comment (taskLoop') == 0
    assert presence_taskloop('\ntaskLoop no paren') == 0
    assert presence_taskloop('\n  (taskLoop no_colon\n') == 1
    assert presence_taskloop('\n(taskLoop i_work') == 1


def test_presence_runtask():
    assert presence_runtask('') == 0
    assert presence_runtask('AbirunTask') == 0
    assert presence_runtask('runTasknitary?!') == 0
    assert presence_runtask('comment (runTask') == 0
    assert presence_runtask('\nrunTask no paren') == 0
    assert presence_runtask('\n  (runTask no_colon\n') == 1
    assert presence_runtask('\n(runTask i_work') == 1















#
