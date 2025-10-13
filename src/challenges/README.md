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

## Python Code Challenge #5: Play the Waiting Game

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
