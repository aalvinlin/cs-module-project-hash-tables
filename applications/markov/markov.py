import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# convert all whitespace characters to a space
characters_whitespace = '\n \t \r'.split(" ")

for whitespace in characters_whitespace:
    words = words.replace(whitespace, " ")

# TODO: analyze which words can follow other words
following_words = dict()

words_array = words.split(" ")

for word_id in range(len(words_array)):

    word = words_array[word_id]
    

    # if there is a next word, add it
    if word_id + 1 < len(words_array):

        next_word = words_array[word_id + 1]

        # start a new set for words to follow if the set doesn't exist yet
        if word not in following_words:
            following_words[word] = set()

        # add the next word to the set
        following_words[word].add(next_word)

for data in following_words:
    print(data, following_words[data])

# TODO: construct 5 random sentences
# Your code here

