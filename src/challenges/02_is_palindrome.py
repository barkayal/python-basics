def is_palindrome(phrase):
    lower_phrase = phrase.lower()
    forwards = ''.join(c for c in lower_phrase if c.isalpha())
    backwards = forwards[::-1]
    return forwards == backwards


tests = ['hello world', 'Go hang a salami, I’m a lasagna hog.', 'A man, a plan, a canal, Panama!', 'No lemon, no melon.']
[print(f"\"{test}\" is{' not ' if is_palindrome(test) != True else ' '}a palindrome {is_palindrome(test)}") for test in tests]