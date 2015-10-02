import glob


def read_polyglot(extension_list):
    X = []
    y = []
    for extension in extension_list:
        files = glob.glob('data/*.{}'.format(extension))
        for file in files:
            y.append(extension)
            with open(file, encoding='windows-1252') as f:
                X.append(f.read())
    return X, y


def match_extensions(df):
    '''Match extensions with the name of their programming language
    '''
    df[0] = df[0].str.replace(r'^gcc$', 'C')
    df[0] = df[0].str.replace(r'^c$', 'C')
    df[0] = df[0].str.replace(r'^csharp$', 'C#')
    df[0] = df[0].str.replace(r'^tcl$', 'TCL')
    df[0] = df[0].str.replace(r'^sbcl$', 'Common Lisp')
    df[0] = df[0].str.replace(r'^clojure$', 'Clojure')
    df[0] = df[0].str.replace(r'^ghc$', 'Haskell')
    df[0] = df[0].str.replace(r'^haskell$', 'Haskell')
    df[0] = df[0].str.replace(r'^javascript$', 'JavaScript')
    df[0] = df[0].str.replace(r'^java$', 'Java')
    df[0] = df[0].str.replace(r'^js$', 'JavaScript')
    df[0] = df[0].str.replace(r'^ocaml$', 'OCaml')
    df[0] = df[0].str.replace(r'^perl$', 'Perl')
    df[0] = df[0].str.replace(r'^php$', 'PHP')
    df[0] = df[0].str.replace(r'^hack$', 'PHP')
    df[0] = df[0].str.replace(r'^python3$', 'Python')
    df[0] = df[0].str.replace(r'^python$', 'Python')
    df[0] = df[0].str.replace(r'^py$', 'Python')
    df[0] = df[0].str.replace(r'^yarv$', 'Ruby')
    df[0] = df[0].str.replace(r'^rb$', 'Ruby')
    df[0] = df[0].str.replace(r'^ruby$', 'Ruby')
    df[0] = df[0].str.replace(r'^jruby$', 'Ruby')
    df[0] = df[0].str.replace(r'^yarv$', 'Ruby')
    df[0] = df[0].str.replace(r'^scala$', 'Scala')
    df[0] = df[0].str.replace(r'^racket$', 'Scheme')
    df[0] = df[0].str.replace(r'^scheme$', 'Scheme')
    return df
