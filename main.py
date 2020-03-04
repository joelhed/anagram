from collections import defaultdict
import json


words_filename = "words.txt"
numbers_to_words_filename = "number_to_words.json"


primes = [
      2,   3,   5,   7,  11,  13,  17,  19,  23,  29, 
     31,  37,  41,  43,  47,  53,  59,  61,  67,  71, 
     73,  79,  83,  89,  97, 101, 103, 107, 109, 113, 
    127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 
    179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 
]

alphabet = "abcdefghijklmnopqrstuvwxyzßàáãäåæçèéëíîïñòóôõöøüÿ'-."

letters_to_primes = {l: p for l, p in zip(alphabet, primes)}


def letter_to_prime(letter):
    return letters_to_primes[letter]


def word_to_number(word):
    n = 1

    for c in word:
        n *= letter_to_prime(c)

    return n


def choices(items):
    for n in range(1, 2 ** len(items)):
        binary_n = ("{:0" +  str(len(items)) + "b}").format(n)
        yield [items[i] for i, pick in enumerate(binary_n) if bool(int(pick))]


# Stateful functions (IO)


def write_number_to_words_file():
    number_to_words = defaultdict(list)

    with open(words_filename) as f:
        # prints the alphabet
        #print("".join(sorted(set(f.read().lower()))))

        for line in f:
            word = line.lower().strip()
            number_to_words[word_to_number(word)].append(word)

    with open(numbers_to_words_filename, "w") as f:
        json.dump(number_to_words, f)


def read_number_to_words_file():
    with open(numbers_to_words_filename) as f:
        return json.load(f)


def solve(regular_letters, required_letter):
    number_to_words = read_number_to_words_file()

    for letters in choices(regular_letters):
        #print(word_to_number(letters), "".join(letters))
        word_number = word_to_number([required_letter] + letters)
        words = number_to_words.get(str(word_number))
        if words is not None:
            yield from words


def main():
    puzzle_letters = "polsotal"
    words = set(solve(puzzle_letters, "k"))
    for word in words:
        print(word)


if __name__ == "__main__":
    main()
