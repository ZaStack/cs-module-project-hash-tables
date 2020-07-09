def no_dups(s):
    # Your code here
    words = s.split()
    dups = dict()
    unique = ''

    for word in words:
        if word not in dups:
            dups[word] = 1
            unique += f'{word} '

    return unique.rstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
