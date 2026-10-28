"""Practice app - VERSION 1"""
from greetings import say_hello

VERSION = "1.0.0"


def main():
    print(f"Practice App v{VERSION}")
    name = input("What is your name? ")
    print(say_hello(name))


if __name__ == "__main__":
    main()
