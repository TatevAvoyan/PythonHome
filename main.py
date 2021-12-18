import random


def get_random_word():
    languages = ["Python", "Go", "JavaScript", "PHP", "Perl", "Swift", "Flask"]
    latter = random.randrange(0, len(languages))

    return languages[latter].lower()


def guess_word(count, word):
    user = input("Input Your name: ")

    while True:
        if count < 1:
            print(f"{user}, You lost")
            break

        print(word)
        print(f"{user} You have {count} attempts")
        guess = input("Guess the word or letter: ").lower()

        if guess in word:
            if guess == word:
                print(f"Congratulations {user} You win!")
                break
            print("There is such a symbol in the word")
        else:
            count -= 1
            print(f"Wrong word/latter")


rand_count = 3
rand_word = get_random_word()

guess_word(rand_count, rand_word)
