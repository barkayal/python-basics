def sort_words(phrase):
    words = sorted(phrase.split(), key=lambda x: x.lower())
    return ' '.join(words)

tests = ['banana ORANGES apple']
[print(f"{test} => {sort_words(test)}") for test in tests]