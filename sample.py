import random
import histogram 

#TO DO: make importing the histogram it's own function
# imports histogram for use in random_word function
# def import_text(histo, file):
#     with open(file) as f:
#         histo = histogram.histogram(f)
#         return histo

''' this function generates a random word from a histogram by creating an empty array,
accessing the histogram via the histogram function, iterating through the histogram,
appending the words to the empty array, generating a random index, and returning that index
'''
def random_word(file):
        words_list = []
        histo = histogram.histogram(file)
        for word in histo:
            words_list.append(word)
            rand_word = random.randint(1, len(histo)-1)
        return words_list[rand_word]


if __name__ == '__main__':
    random_word('siddhartha.txt')
    