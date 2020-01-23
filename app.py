from random import randint
import sys as sys


filename = '/Users/Anas/Desktop/MakeSchool/Term_3/CS1.2/Assignments/CS1.2-Intro-Data-Structure/words.txt'


def pritLines():
    my_file = open(filename, "r")
    lines = my_file.readlines()
    print(lines)


if __name__ == "__main__":
    args = sys.argv
    print(args)
    # pritLines()
