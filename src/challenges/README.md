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
