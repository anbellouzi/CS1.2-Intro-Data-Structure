
class Histogram():

    def __init__(self, data):
        """Initialize this node with the given data."""
        pass

    # return a histogram data structure that stores each unique word along with the number of times the word appears in the source text.
    def histogram():
        filename = './text//adventure_holmes.txt'
        file = open(filename, 'r')
        lines = file.readlines()

        histogram = {}
        for line in lines:
            words = line.rstrip('\n').split()
            for word in words:
                if (word in histogram):
                    histogram[word] += 1
                else:
                    histogram[word] = 1

        return histogram

# returns the total count of unique words in the histogram
def unique_words(histogram):
    total = 0

    for item in histogram:
        total += 1


    return total


# returns the number of times that word appears in a text
def frequency(word, histogram):
    if word in histogram:
        return histogram[word]


if __name__ == '__main__':
    histogram_result = histogram()
    print("\nHistogram", '\n')
    print(histogram_result, '\n')

    unique_words_result = unique_words(histogram_result)
    print(unique_words_result, "Unique Words\n")

    word = "mystery" # check word frequency

    word_frequency = frequency(word, histogram_result)
    print("Word: '"+word+ "' appeared: "+str(word_frequency), " times\n")
