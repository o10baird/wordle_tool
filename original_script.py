'''
Original Work by --> Fahmi Nurfikri
https://medium.com/towards-data-science/how-to-find-the-best-wordle-first-combination-words-with-python-ded4b0679a5
'''

import pandas as pd
import numpy as np
import math

def best_words(words):
    distinct_words = []
    for word in words:
        distinct_words.append(list(set(word)))
    letter_counter = {}
    for word in distinct_words:
        for letter in word:
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

def get_best_word(words, word_values):
    return words[np.argmax(word_values)]

def remove_word_contain_letters(words, first_word):
    result_word = []
    first_word_list = list(set(first_word))
    
    for word in words:
        in_word = False
        i = 0
        while i < len(first_word_list) and not in_word:
            if first_word_list[i] in word:
                in_word = True
            i += 1
        if not in_word:
            result_word.append(word)
    return result_word

if __name__ == '__main__':
    words = []
    with open('data\words.txt') as f:
        words = [line.rstrip() for line in f]
        
    distinct_words = []
    for word in words:
        distinct_words.append(list(set(word)))
    letter_counter = {}
    for word in distinct_words:
        for letter in word:
            if letter in letter_counter:
                letter_counter[letter] += 1
            else:
                letter_counter[letter] = 0
    word_values = best_words(words)
    first_word = get_best_word(words, word_values)
    second_words = remove_word_contain_letters(words, first_word)
    second_values = best_words(second_words)
    second_word = get_best_word(second_words, second_values)
    values = best_words(words)
    values_index = np.argsort(values)[::-1]
    best_val = 0
    best_word_list = []
    top_words = sorted(values, reverse=True)
    for i, idx in enumerate(values_index):
        best_word = words[idx]
        second_words = remove_word_contain_letters(words, best_word)
        second_values = best_words(second_words)
        second_best_word = get_best_word(second_words, second_values)
        temp_value = 0
        for letter in second_best_word:
            temp_value += letter_counter[letter]
        if temp_value + top_words[i] >= best_val:
            best_val = temp_value + top_words[i]
            best_word_list.append([best_word, second_best_word])
            
    letter_list =['r', 'o', 'a', 's', 't', 'l', 'i', 'n', 'e', 's']
    letter_value = {}
    for letter in letter_list:
        letter_counter = {}
        for i in range(len(letter_list)//2):
            loc_counter = 0
            for j in range(len(words)):
                if words[j][i] == letter:
                    loc_counter += 1
            letter_counter[str(i)] = loc_counter
        letter_value[letter] = letter_counter
        
    result_list = []
    for i in range(len(best_word_list)):
        word_value = 0
        for word in best_word_list[i]:
            for j, letter in enumerate(word):
                if letter in letter_value:
                    word_value += letter_value[letter][str(j)]
        result_list.append(word_value)
    result_index = np.argsort(result_list)[::-1]
    print(best_word_list[result_index[0]])