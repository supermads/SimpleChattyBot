def main():
    print("Hello! My name is Aid.")
    print("I was created in 2020.")
    name = input("Please, remind me your name.\n")
    print("What a great name you have, {}!".format(name))
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    a = int(input())
    b = int(input())
    c = int(input())
    age = (a * 70 + b * 21 + c * 15) % 105
    print("Your age is {}; that's a good time to start programming!".format(age))


main()
