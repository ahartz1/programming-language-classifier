# Classify code snippets into programming languages

## Description

Classifier that can take snippets of code and guesses the programming language of the code.

## Objectives

### Learning Objectives

After completing this assignment, you should understand:

* Feature extraction
* Classification
* The varied syntax of programming languages

### Performance Objectives

After completing this assignment, you should be able to:

* Build a robust classifier

## Details

### Deliverables

* A Git repo called programming-language-classifier containing at least:
  * `README.md` file explaining how to run your project
  * a `requirements.txt` file
  * a suite of tests for your project

### Requirements  

* Passing unit tests
* No PEP8 or Pyflakes warnings or errors

## Normal Mode

### Getting a corpus of programming languages

Option 1: Get code from the [Computer Language Benchmarks Game](http://benchmarksgame.alioth.debian.org/). You can [download their code](https://alioth.debian.org/snapshots.php?group_id=100815) directly. In the downloaded archive under `benchmarksgame/bench`, you'll find many directories with short programs in them. Using the file extensions of these files, you should be able to find out what programming language they are.

Option 2: Scrape code from [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code). You will need to figure out how to scrape HTML and parse it. [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/) is your best bet for doing that.

Option 3: Get code from GitHub somehow. The specifics of this are left up to you.

You are allowed to use other code samples as well.

**For your sanity, you only have to worry about the following languages:**

* C (.gcc, .c)
* C#
* Common Lisp (.sbcl)
* Clojure
* Haskell
* Java
* JavaScript
* OCaml
* Perl
* PHP (.hack, .php)
* Python
* Ruby (.jruby, .yarv)
* Scala
* Scheme (.racket)

Feel more than free to add others!

### Classifying new snippets

Using your corpus, you should extract features for your classifier. Use whatever classifier engine that works best for you _and that you can explain how it works._

Your initial classifier should be able to take a string containing code and return a guessed language for it. It is recommended you also have a method that returns the snippet's percentage chance for each language in a dict.

### Testing your classifier

The `test/` directory contains code snippets. The file `test.csv` contains a list of the file names in the `test` directory and the language of each snippet. Use this set of snippets to test your classifier. _Do not use the test snippets for training your classifier._

<!-- ## Hard Mode

In addition to the requirements from **Normal Mode**:

Create a runnable Python file that can classify a snippet in a text file, run like this:

`guess_lang.py code-snippet.txt`

where `guess_lang.py` is whatever you name your program and `code-snippet.txt` is any snippet. Your program should print out the language it thinks the snippet is.

To do this, you will likely want to either pre-parse your corpus and output it as features to load or save out your classifier for later use. Otherwise, you'll have to read your entire corpus every time you run the program. That's acceptable, but slow.

You may want to add some command-line flags to your program. You could allow people to choose the corpus, for example, or to get percentage chances instead of one language. To understand how to write a command-line program with arguments and flags, see the [argparse](https://docs.python.org/3/library/argparse.html) module in the standard library. -->

#### System Requirements

* You will need to have **Python&nbsp;3** installed on your machine or have access to a Python&nbsp;3 interpreter. See [python's site](https://www.python.org/) for details.

* Clone this repo onto your machine.

* You will need to make sure that you have a Python&nbsp;3 virtual environment running in the folder that you intend to work from. [See this site for details if you're not familiar.](http://docs.python-guide.org/en/latest/dev/virtualenvs/) **Complete this step before attempting the below.**

* In your command-line program (such as Terminal on Mac&nbsp;OS&nbsp;X), navigate into the newly created repo. By default, this will be called `programming-language-classifier`. Install the requirements file by runnning **`pip install -r requirements.txt`**. Note that **`lxml`** compiles to the version of Python in your environment after downloading (Python 3)—this process can take awhile, so please be patient.

* For textblob to work properly, you will need to download its associated data files. To do this you will need to run the following command at the command line: **`python -m textblob.download_corpora`** This process can take awhile, so please be patient.

* For nltk to work properly, you will need to download its associated data files. To do this you will need to run the following command at the command line:

```
$ python3
>>> import nltk
>>> nltk.download()
```

This will open up a new window on which you will need to select to download all. This process can take awhile, so please be patient. When it is done and you have closed the download window the command line will show `True`. Enter `exit()` on the Python command line to return to the command prompt.

* To run this program, save `guess_lang.py` to your computer. Using a command-line program (such as Terminal on Mac&nbsp;OS&nbsp;X), navigate to the folder containing the downloaded file and run the following line to play: `python3 guess_lang.py`


## Additional Resources

* [TextBlob](http://textblob.readthedocs.org/en/dev/)
* [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/)
* [Rosetta Code](http://rosettacode.org/wiki/Rosetta_Code)
* [Working with Text Files](https://opentechschool.github.io/python-data-intro/core/text-files.html)
