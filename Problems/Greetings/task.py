def greet():
    print("Hello! My name is Aid.")
    print("I was created in 2020.")
    name = input("Please, remind me your name.\n")
    print("What a great name you have, {}!".format(name))


def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    a = int(input())
    b = int(input())
    c = int(input())
    age = (a * 70 + b * 21 + c * 15) % 105
    print("Your age is {}; that's a good time to start programming!".format(age))


def count():
    print("Now I will prove to you that I can count to any number you want.")
    n = int(input())
    for i in range(n + 1):
        print("{} !".format(i))


def test():
    print("Let's test your programming knowledge.")
    print("Dictionaries store data in what type of pairs?")
    print("1. row:column")
    print("2. key:value")
    print("3. string:integer")
    print("4. word:byte")
    choice = int(input())
    while choice != 2:
        print("Please, try again.")
        choice = int(input())
    print("Completed, have a nice day!")
    print("Congratulations, have a nice day!")


def main():
    greet()
    guess_age()
    count()
    test()


main()
