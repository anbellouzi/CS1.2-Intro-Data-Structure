from random import randint
import sys as sys

def reaarange():
    wordDic = {}
    while True:
        word = args[randint(0, len(args)-1)]
        if word in wordDic.keys():
            if len(wordDic) == len(args):
                break
        else:
            wordDic[word] = word
    return wordDic




if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    print("Original List:")
    for arg in args:
        print(arg)

    print()
    rearrangedWords = reaarange()
    print("Rearranged List:")
    for keys,values in rearrangedWords.items():
        print(values)
    print()
