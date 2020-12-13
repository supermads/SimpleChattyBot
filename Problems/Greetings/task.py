def morning(other_func):
    def wrapper(name):
        other_func(name)
        print("Good morning,", name)
    return wrapper
