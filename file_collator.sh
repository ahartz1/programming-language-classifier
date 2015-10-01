#!/bin/bash

# HOW TO USE THIS SCRIP: Run from the parent directory that has your data


# Start by finding all files with the desired extensions, then copy to data/
find . \
      \(   -name '*.c' -or -name '*.gcc'                        `# C` \
       -or -name '*.csharp'                                    `# C#` \
       -or -name '*.sbcl'                                      `# Common Lisp` \
       -or -name '*.clojure'                                   `# Clojure` \
       -or -name '*.ghc'                                       `# Haskell GHC` \
       -or -name '*.java'                                      `# Java` \
       -or -name '*.js'                                        `# JavaScript` \
       -or -name '*.ocaml'                                     `# OCaml` \
       -or -name '*.perl'                                      `# Perl` \
       -or -name '*.hack' -or -name '*.php'                    `# PHP` \
       -or -name '*.py' -or -name '*.python3'                  `# Python` \
       -or -name '*.rb' -or -name '*.jruby' -or -name '*.yarv' `# Ruby` \
       -or -name '*.scala'                                     `# Scala` \
       -or -name '*.racket'  \)                                `#scheme` \
       -exec cp "{}" ~/TIY/programming-language-classifier/data/ \;
