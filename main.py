"""Practice app - VERSION 2"""
from greetings import say_hello, say_goodbye

VERSION = "2.0.0"


def main():
    print(f"Practice App v{VERSION}")
    name = input("What is your name? ")
    print(say_hello(name))
    print(say_goodbye(name))


if __name__ == "__main__":
    main()
