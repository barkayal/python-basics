import secrets


def generate_passphrase(num_words, filename='diceware.wordlist.asc'):
    wordlist_path = '../../f.input/'+filename
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)


print(generate_passphrase(7))
print(generate_passphrase(3))