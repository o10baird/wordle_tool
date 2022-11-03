'''
Original Work by --> Fahmi Nurfikri
https://medium.com/towards-data-science/how-to-find-the-best-wordle-first-combination-words-with-python-ded4b0679a5
'''

import pandas as pd
import numpy as np
import math

def best_words(words: list) -> list:
    distinct_words = []
    for word in words: # create a list of lists containing the distinct letters in each word
        distinct_words.append(list(set(word))) 
    letter_counter = {} #dictionary with letter as key and number of times it appears as value
    for distinct_word in distinct_words:
        for letter in distinct_word:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 0
    word_values = []
    for word in distinct_words:
        # print(word)
        temp_value = 0
        for letter in word:
            temp_value += letter_counter[letter]
        word_values.append(temp_value)
    return word_values

def get_word_values(words: list, greens_dict: dict) -> list:
    distinct_words = []
    letter_counter = greens_dict
    for word in words:
        distinct_words.append(list(set(word)))
    for distinct_word in distinct_words:
        for letter in distinct_word:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 0
    word_values = []
    for word in distinct_words:
        temp_value = 0
        for letter in word:
            temp_value += letter_counter[letter]
        word_values.append(temp_value)
    return word_values

    pass

def get_best_word(words, word_values):
    return words[np.argmax(word_values)]


def find_next_word_list(words: list, previous_word: str, results: str) -> list:
    previous_word_chars = [char for char in previous_word]
    previous_results_list = [num for num in results]
    previous_word_results = zip(previous_word_chars, previous_results_list)
    
    for word in words:
        position = 0
        for char, num in previous_word_results:
            if char in word and num == 0: # remove words that do not match green letters
                words.remove(word)
            if num == 2 and char != word[position]: # remove words with grey letters
                words.remove(word)
            if num == 1 and char not in word: # remove words without yellow letters
                words.remove(word)
            if num ==1 and char == word[position]: # remove words with yellow letters in the wrong position
                words.remove(word)
            position += 1
    return words



def update_greens(greens_dict: dict, guessed_word: str, results: str) -> dict:
    guessed_word_chars = [char for char in guessed_word]
    results_list = [num for num in results]
    word_results = zip(guessed_word_chars, results_list)
    for char, num in word_results:
        if num == 2:
            greens_dict.get(char, 0) - 1
    return greens_dict


if __name__ == '__main__':
    words = []
    with open('data\words.txt') as f: # create a list of words from the input file
        words = [line.rstrip() for line in f]
    f.close()

    word_values = best_words(words)
    guess = get_best_word(words, word_values)
    print(f"First Word: {guess}")

    while True:
        try:
            results = str(input("Enter the results of the first word as a sequence of numbers. \n0 --> not in word (grey) \n1 --> in word (yellow) \n2--> in correct position (green)\n")).lower()
            assert len(results) == 5
            for num in results:
                assert num in ['0', '1', '2']
            break
        except AssertionError:
            print("Results must be 5 numbers long and either 0, 1, or 2.")
    # Create and update a list of green letters
    greens_dict = {}
    greens_dict = update_greens(greens_dict, guess, results)

    # Update the list of words and values given the results of the first guess
    next_words_list = find_next_word_list(words, guess, results)
    next_word_values = get_word_values(next_words_list, greens_dict)
    print(f"Greens Dictionary\n{greens_dict}")

    guess_num = 2
    while guess_num < 7:
        guess = get_best_word(next_words_list, next_word_values)

        # User Input
        results = str(input(f"Enter the results of guess {guess_num}, {guess}, as a sequence of numbers. \n0 --> not in word (grey) \n1 --> in word (yellow) \n2--> in correct position (green)\n")).lower()
        
        # Update based on user results
        greens_dict = update_greens(greens_dict, guess, results)
        next_words_list = find_next_word_list(next_words_list, guess, results)
        next_word_values = get_word_values(next_words_list, greens_dict)
        guess_num += 1
