def is_pangram(text):
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = list(text.lower())
    for i in abc:
        if i not in text:
            return False
    return True

text = input()

print(is_pangram(text))