import random


def repeat_lyrics():
    for number in range(random.randint(1, 10)):
        print_lyrics(number+1)


def print_lyrics(number):
    print(number)
    print("I'm a lumberjack and I'm okay.")
    print("I sleep all night and I work all day.")


repeat_lyrics()
