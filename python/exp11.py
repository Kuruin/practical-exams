def is_human(name):
    return True


def is_mortal(name):
    if is_human(name):
        return True


print(is_mortal("Socrates"))
