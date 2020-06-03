import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# convert all whitespace characters to a space
characters_whitespace = '\n \t \r'.split(" ")

for whitespace in characters_whitespace:
    words = words.replace(whitespace, " ")

# remove consecutive spaces
words = words.replace("  ", " ")

# analyze which words can follow other words
following_words = dict()

# create additional dictionaries to categorize words as start/end words
start_words = dict()
end_words = dict()

ending_punctuation = [".", "?", "!"]

words_array = words.split(" ")

for word_id in range(len(words_array)):

    word = words_array[word_id]

    # skip the last word
    if word_id == len(words_array) - 2:
        break

    # if there is a next word, add it
    if word_id + 1 < len(words_array):

        next_word = words_array[word_id + 1]

        # start a new set for words to follow if the set doesn't exist yet
        if word not in following_words:
            following_words[word] = []

        # add the next word to the set
        following_words[word].append(next_word)

        # if the word is a start word, add it to the start_words dictionary
        # start word criteria: starts with a capital letter OR starts with a quote and 
        is_start_word = (word[0].isalpha() and word[0] == word[0].upper()) or (len(word) > 1 and word[0] == '"' and word[1].isalpha() and word[1] == word[1].upper())

        if is_start_word and word not in start_words:
            start_words[word] = 1

        # if the word is an end word, add it to the end_words dictionary
        is_end_word = (word[-1] in ending_punctuation) or (len(word) > 1 and word[-1] == '"' and word[-2:-1] in ending_punctuation)

        if is_end_word and word not in end_words:
            end_words[word] = 1

# for data in following_words:
#     print(data, following_words[data])

# for data in start_words:
    # print(data, start_words[data])

# for data in end_words:
#     print(data, end_words[data])


# TODO: construct 5 random sentences
# Your code here

