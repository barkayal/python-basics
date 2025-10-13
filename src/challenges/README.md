# Python challenges

## Python Code Challenge #01: Find Prime Factors

Your goal is to implement a function, `get_prime_factors()`, that takes an integer value as the input argument and returns a list containing all of its prime factors.

### Example Test Output

```console
>>> get_prime_factors(13)
[13]
>>> get_prime_factors(630)
[2, 3, 3, 5, 7]
```

## Python Code Challenge #02: Identify a Palindrome

Your goal is to implement a function, `is_palindrome()`, that takes a text string as the input argument and returns a boolean indicating whether or not it's a palindrome.

### Example Test Output

```console
>>> is_palindrome('hello world')
False
>>> is_palindrome('Go hang a salami, I’m a lasagna hog.')
True
```

## Python Code Challenge #03: Sort a String

Your goal is to implement a function, `sort_words()`, that takes a string containing one or more words separated by spaces as the input argument and returns a string containing those words sorted alphabetically.

### Example Test Output

```console
>>> sort_words('banana ORANGE apple')
'apple banana ORANGE'
```

## Python Code Challenge #04: Find All List Items

Your goal is to implement a function, `index_all()`, that takes a list of objects and the item to search for as input arguments and returns a list of indices for where that item exists within the list.

NOTE: Since the input argument could be a list of lists, your function should be able to traverse multidimensional lists to find all instances of the item, and the elements of the returned list should also be lists to indicate multidimensional indices.

### Example Test Output

```console
>>> example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
>>> index_all(example, 2)
[[0, 0, 1], [0, 1], [1, 1]]
>>> print(index_all(example, [1, 2, 3]))
[[0, 0], [1]]
```

## Python Code Challenge #05: Play the Waiting Game

Your goal is to implement a function, `waiting_game()`, that prints a message for the player to wait a random amount of time, somewhere between two to four seconds. When the player presses Enter, that starts a timer. The player's goal is to wait the specified number of seconds and then press Enter again. That displays the elapsed time, along with a message about whether the player was too fast, too slow, or right on target.

### Example Test Output

```console
>>> waiting_game()

Your target time is 2 seconds
 ---Press Enter to Begin---

...Press Enter again after 2 seconds...

Elapsed time: 1.680 seconds
(0.320 seconds too fast)
```

## Python Code Challenge #06: Save a Dictionary

Your goal is to implement two functions, `save_dict()` and `load_dict()`. The `save_dict()` function takes two inputs arguments for the dictionary to save and an output file path. The `load_dict()` function takes an input argument of the file path to the saved dictionary and returns its stored dictionary object.

### Example Test Output

```console
>>> save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
print(load_dict('test.pickle'))
{1: 'a', 2: 'b', 3: 'c'}
```

## Python Code Challenge #07: Schedule a Function

Your goal is to implement a function, `schedule_function()`, that takes three inputs arguments for the time at which to run a specified function, the function you want to execute, and a variable number (zero or more) of arguments which are passed to the schedule function to use.

When your `schedule_function()` is called, it should immediately print a message indicating which function was scheduled and when it will execute.

### Example Test Output

```console
>>> schedule_function(time.time() + 1, print, 'Howdy!')
print() scheduled for Sun Aug 14 20:39:28 2022
```

Then one second later...

```console
Howdy!
```

## Python Code Challenge #08: Send an Email

Your goal is to implement a function, `send_email()`, that takes three input arguments for the recipient’s email address, the email’s subject line, and the email message body.

### Example Test Output

```console
>>> send_email('recipient@email.com', ‘Notification', 'Everything is awesome!')
```

The recipient should receive an email with the subject "Notification" and the message body "Everything is aweseome!"

## Python Code Challenge #09: Simulate Dice

Your goal is to implement a function, `roll_dice()`, that takes a variable number of input arguments representing the number of sides on an arbitrary number of dice, its and its output should print a table of the probability for each possible outcome.

### Example Test Output

Rolling one four-sided die and two six-sided dices:

```console
>>> roll_dice(4,6,6)

OUTCOME PROBABILITY
3       0.69%
4       2.06%
5       4.14%
6       6.95%
7       9.70%
8       12.55%
9       13.93%
10      13.85%
11      12.52%
12      9.70%
13      6.95%
14      4.17%
15      2.09%
16      0.70%
```

## Python Code Challenge #10: Count Unique Words

Your goal is to implement a function, `count_words()`, that takes the path to a text file as the input argument and prints the total number of words in the file, as well as the top 20 most frequently used words and how many times each of them occurs.

### Example Test Output

Using [The Complete Works of William Shakespeare](https://www.gutenberg.org/cache/epub/100/pg100.txt) as input:

```console
>>> count_words('shakespeare.txt')


Total Words: 976836

Top 20 Words:
THE      30257
AND      28413
I        23070
TO       20997
OF       18824
A        16163
YOU      14570
MY       13179
IN       12333
THAT     12063
IS       9858
NOT      9066
WITH     8531
ME       8262
FOR      8244
IT       8212
HIS      7583
BE       7384
THIS     7165
HE       7100
```

## Python Code Challenge #11: Generate a Password

Your goal is to implement a function, `generate_passphrase()`, that takes the number of words to include in the password as the input argument and returns a string containing a sequence of randomly selected words from the [Diceware list](https://theworld.com/~reinhold/diceware.wordlist.asc) separated by spaces.

### Example Test Output

```console
>>> generate_passphrase(4)
'correct horse battery staple'
```

## Python Code Challenge #12: Merge CSV Files

Your goal is to implement a function, `merge_csv()`, that takes two input arguments: a list of file paths to CSV files to merge and an output file path to save the resulting CSV file.

### Example Test Output

Using the two included CSV files with student grades as input:

```console
>>> merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')
```

## Python Code Challenge #13: Solve a Sudoku

Your goal is to implement a function, `solve_sudoku()`, that takes a two-dimensional list of lists representing an unsolved [Sudoku](https://en.wikipedia.org/wiki/Sudoku) puzzle as the input argument and returns a 9x9 two-dimensional list-of-lists containing the puzzle solution.

NOTE: Zero is used to represent an empty cell.

### Example Test Output

```console
>>> puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
              [6, 0, 0, 1, 9, 5, 0, 0, 0],
              [0, 9, 8, 0, 0, 0, 0, 6, 0],
              [8, 0, 0, 0, 6, 0, 0, 0, 3],
              [4, 0, 0, 8, 0, 3, 0, 0, 1],
              [7, 0, 0, 0, 2, 0, 0, 0, 6],
              [0, 6, 0, 0, 0, 0, 2, 8, 0],
              [0, 0, 0, 4, 1, 9, 0, 0, 5],
              [0, 0, 0, 0, 8, 0, 0, 7, 9]]
>>> solve_sudoku(puzzle)
[[5, 3, 4, 6, 7, 8, 9, 1, 2],
 [6, 7, 2, 1, 9, 5, 3, 4, 8],
 [1, 9, 8, 3, 4, 2, 5, 6, 7],
 [8, 5, 9, 7, 6, 1, 4, 2, 3],
 [4, 2, 6, 8, 5, 3, 7, 9, 1],
 [7, 1, 3, 9, 2, 4, 8, 5, 6],
 [9, 6, 1, 5, 3, 7, 2, 8, 4],
 [2, 8, 7, 4, 1, 9, 6, 3, 5],
 [3, 4, 5, 2, 8, 6, 1, 7, 9]]
```

As a bonus challenge, implement a `print_sudoku()` function to display a 9x9 grid of numbers Sudoku-style:

```console
>>> print_sudoku(puzzle)
 5  3  *  |  *  7  *  |  *  *  * 
 6  *  *  |  1  9  5  |  *  *  * 
 *  9  8  |  *  *  *  |  *  6  * 
---------------------------------
 8  *  *  |  *  6  *  |  *  *  3 
 4  *  *  |  8  *  3  |  *  *  1 
 7  *  *  |  *  2  *  |  *  *  6 
---------------------------------
 *  6  *  |  *  *  *  |  2  8  * 
 *  *  *  |  4  1  9  |  *  *  5 
 *  *  *  |  *  8  *  |  *  7  9  
```

## Python Code Challenge #14: Build a ZIP Archive

Your goal is to implement a function, `zip_all()`, that takes three input arguments for a path to the top-level directory you want to include, a list of file extensions, and an output file path for the resulting archive.

### Example Test Output

Using the included directory of images and text files as input:

```console
>>> zip_all('my_stuff', ['.jpg', '.txt'], 'my_stuff.zip')
```

## Python Code Challenge #15: Download Sequential Files

Your goal is to implement a function, `download_files()`, that takes two input arguments: the URL for the first item in the sequence, and a path to the output directory where you want to save them.

### Example Test Output

Using the example URL hosting 50 images, with the first image at <http://699340.youcanlearnit.net/image001.jpg>:

```console
>>> download_files('http://699340.youcanlearnit.net/image001.jpg', './images')
```
