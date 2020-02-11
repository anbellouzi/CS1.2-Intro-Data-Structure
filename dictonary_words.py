from random import randint

filename = "/usr/share/dict/words"


def returnSentence(lines):
    index = 2  # how many words to use
    sentence = ""

    lines = lines.split('.')

    while index > 0:
        sentence += lines[randint(0, len(lines)-1)].rstrip('\n')
        sentence += " "
        index -= 1

    return sentence



if __name__ == '__main__':
    file = open(filename, 'r')
    lines = file.readlines()

    sentence = returnSentence(lines)

    print(sentence)
