---
created: 2022-11-02T09:44:48 (UTC -04:00)
tags: []
source: https://medium.com/towards-data-science/how-to-find-the-best-wordle-first-combination-words-with-python-ded4b0679a5
author: Fahmi Nurfikri
---

# How to Find the Best Wordle First Combination Words with Python | by Fahmi Nurfikri | Oct, 2022 | Towards Data Science

> ## Excerpt
> When playing Wordle, finding the right letters is usually determined by the first words. The more effective the first word, the more clues we can get to get the letter right. Usually, everyone has…

---
## Search for the optimum first and second words combination

![](https://miro.medium.com/max/700/0*Rc0WtBAnE5W48JXA)

Photo by [Nils Huenerfuerst](https://unsplash.com/@nhuenerfuerst?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

When playing Wordle, finding the right letters is usually determined by the first words. The more effective the first word, the more clues we can get to get the letter right. Usually, everyone has their own preference.

For those of you who don’t know, wordle is a daily word game created by Josh Wardle, where every day there will be a new word puzzle to solve. For more, you can visit [https://www.nytimes.com/games/wordle/index.html](https://www.nytimes.com/games/wordle/index.html).

I will look for a solution to get the best first-word using python in this post. Here I will only use basic statistical methods so that it is easy for everyone to understand.

I will divide this article into 4 parts, namely:

1.  Search for the first word
2.  Looking for the second word
3.  Look for the combination of the first and second words
4.  Looking for the most optimum combination

## Search for the first word

I used a [**dataset**](https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt) from [_The Art of Computer Programming (TAOCP)_](https://www-cs-faculty.stanford.edu/~knuth/taocp.html) by Donald E. Knuth. The dataset contains words in English consisting of 5 letters (according to the letter limit on the wordle) with a total of 5757 words.

> **CITATION**: The dataset above is from prof. Donald E. Knuth. Professor Emeritus of The Art of Computer Programming at Stanford University.

The first thing I did was import dependencies and loaded the dataset file.

```
import pandas as pdimport numpy as npimport mathwords = []with open('sgb-words.txt') as f:    words = [line.rstrip() for line in f]
```

The dataset contains the following data.

```
whichtheretheiraboutwould...pupal
```

The first processing is done by removing the same letters in each word. This is necessary so that we can get a word with 5 different letters. The method is as follows.

```
distinct_words = []for word in words:    distinct_words.append(list(set(word)))
```

The result will be like this.

```
[['w', 'h', 'i', 'c'],['t', 'h', 'e', 'r'],['t', 'h', 'e', 'i', 'r'],['a', 'b', 'o', 'u', 't'],['w', 'o', 'u', 'l', 'd'],...['p', 'u', 'a', 'l']]
```

After that, we can get the weight of each letter. The method is quite simple, namely by adding up each letter, and the results are presented in the form of a dictionary. The weight will determine how often the letter appears, the more often the letter appears, the greater the weight letter.

```
letter_counter = {}for word in distinct_words:    for letter in word:        if letter in letter_counter:            letter_counter[letter] += 1        else:            letter_counter[letter] = 0
```

The result will be like this.

```
{'h': 790, 'w': 500, 'i': 1538, 'c': 919, 'e': 2657, 't': 1461, 'r': 1798, 'u': 1067, 'a': 2180, 'o': 1682, 'b': 668, 'l': 1433, 'd': 1099, 's': 2673, 'f': 501, 'g': 650, 'k': 573, 'n': 1218, 'y': 867, 'p': 894, 'v': 308, 'm': 793, 'q': 52, 'j': 87, 'x': 137, 'z': 120}
```

If we sort, the result will be like this.

```
>>> {key: val for key, val in sorted(letter_counter.items(), key = lambda x: x[1], reverse = True)}{'s': 2673, 'e': 2657, 'a': 2180, 'r': 1798, 'o': 1682, 'i': 1538, 't': 1461, 'l': 1433, 'n': 1218, 'd': 1099, 'u': 1067, 'c': 919, 'p': 894, 'y': 867, 'm': 793, 'h': 790, 'b': 668, 'g': 650, 'k': 573, 'f': 501, 'w': 500, 'v': 308, 'x': 137, 'z': 120, 'j': 87, 'q': 52}
```

From these results, it can be seen that the 5 letters that appear most often are the letters `s`, `e`, `a`, `r`, and `o`.

In addition, this is the result when expressed as a percentage.

```
>>> values = letter_counter.values()>>> total = sum(values)>>> percent = [value * 100. / total for value in values]>>> for i, letter in enumerate(letter_counter.keys()):...    print("{}: {}".format(letter, percent[i]))h: 2.962685167822989w: 1.8751171948246765i: 5.767860491280705c: 3.4464654040877556e: 9.964372773298331t: 5.479092443277705r: 6.742921432589537u: 4.00150009375586a: 8.17551096943559o: 6.307894243390212b: 2.505156572285768l: 5.374085880367523d: 4.121507594224639s: 10.024376523532721f: 1.878867429214326g: 2.4376523532720795k: 2.148884305269079n: 4.567785486592912y: 3.2514532158259892p: 3.3527095443465216v: 1.1550721920120008m: 2.973935870991937q: 0.19501218826176636j: 0.3262703918994937x: 0.5137821113819614
```

Next, we only need to find the word that has the letter with the highest weight. The method is as follows.

```
word_values = []for word in distinct_words:    temp_value = 0    for letter in word:        temp_value += letter_counter[letter]    word_values.append(temp_value)words[np.argmax(word_values)]
```

And the result is `arose`. If viewed from the data above, it can be seen that the word `arose` has letters that have a high weight. So it can be concluded that the word `arose` is the best word to use in the first word of the Wordle based on statistical results.

> But is the first word only enough?

Sometimes we need one more word to get enough clues. So we will search for another word.

## Looking for the second word

After we get the first word, the next step is to get a list of words that do not contain letters in the first word. For example, the first word we get is `arose`. So the word list in the dataset cannot contain the letters `a`, `r`, `o`, `s`, and `e`. If there is a word that contains these letters, then the word will be removed from the list. The method is as follows.

```
result_word = []first_word_list = list(set(best_word))for word in words:    in_word = False    i = 0    while i < len(first_word_list) and not in_word:        if first_word_list[i] in word:            in_word = True        i += 1    if not in_word:        result_word.append(word)
```

And the result is as follows.

```
['which','think','might','until',...'biffy']
```

The number of words was reduced to 310 words from the previous 5757 words. There are only about 5% of words left.

The next step is that we will repeat the process as we did the first-word search. The complete code is as follows.

```
import pandas as pdimport numpy as npimport mathdef best_words(words):    distinct_words = []    for word in words:        distinct_words.append(list(set(word)))    letter_counter = {}    for word in distinct_words:        for letter in word:            if letter in letter_counter:                letter_counter[letter] += 1            else:                letter_counter[letter] = 0    word_values = []    for word in distinct_words:        temp_value = 0        for letter in word:            temp_value += letter_counter[letter]        word_values.append(temp_value)    return word_valuesdef get_best_word(words, word_values):    return words[np.argmax(word_values)]def remove_word_contain_letters(words, first_word):    result_word = []    first_word_list = list(set(first_word))        for word in words:        in_word = False        i = 0        while i < len(first_word_list) and not in_word:            if first_word_list[i] in word:                in_word = True            i += 1        if not in_word:            result_word.append(word)    return result_wordwords = []with open('sgb-words.txt') as f:    words = [line.rstrip() for line in f]word_values = best_words(words)first_word = get_best_word(words, word_values)second_words = remove_word_contain_letters(words, first_word)second_values = best_words(second_words)second_word = get_best_word(second_words, second_values)print(first_word)  # first wordprint(second_word)  # second word
```

And the results for the first and second words are `arose` and `unity`.

From the method above, it can be concluded that `arose` and `unity` are the best words to start the Wordle game. However, if we look at the statistics on the number of letters in the previous post, it can be seen that the letters `u` and `y` are not in the top 10 most used letters. That indicates that the words `arose` and `unity` may not be the most optimal words.

## Look for the combination of the first and second words

In this section, we will discuss so that we can get two words whose letters are all letters that occur most often.

We only need to repeat the process that we have done before. If in the previous process we only used the first word that had the best value, now we also use the second best word as the first word so that we get more variations in results.

The steps are as follows.

The first is to calculate the value for all words, then sort the words by value.

```
values = best_words(words)values_index = np.argsort(values)[::-1]
```

After that, we will search for the first and second words as before. The difference is, here we will continue to loop to find the first and second-word combinations in order to produce words that have the best value.

```
best_val = 0best_word_list = []top_words = sorted(values, reverse=True)for i, idx in enumerate(values_index):    best_word = words[idx]    second_words = remove_word_contain_letters(words, best_word)    second_values = best_words(second_words)    second_best_word = get_best_word(second_words, second_values)    temp_value = 0    for letter in second_best_word:        temp_value += letter_counter[letter]    if temp_value + top_words[i] >= best_val:        best_val = temp_value + top_words[i]        print(best_word, second_best_word, top_words[i] + temp_value)
```

And the result is like this.

```
arose unity 17141tears doily 17388stare doily 17388tares doily 17388rates doily 17388aster doily 17388tales irony 17507taels irony 17507stale irony 17507least irony 17507tesla irony 17507steal irony 17507slate irony 17507teals irony 17507stela irony 17507store inlay 17507lores antic 17559...laird stone 17739adorn tiles 17739radon tiles 17739tonal rides 17739talon rides 17739lined roast 17739intro leads 17739nitro leads 17739nodal tries 17739
```

From these results, the first column is the first word, the second column is the second word, and the third column is the sum of the values of the first word and the second word.

If you look at the results above, the words `arose` and `unity` are not a combination of words with the greatest value. In addition, there are many word combinations that get a value of 17739, if you pay attention to all the letters in the word combination that get that value, it is the ten letters that appear the most in the dataset. So it can be concluded that the combination of words that get a value of 17739 is the highest word combination that we can get.

> But which is the most optimal combination of words?

To get the answer to this question, we need to know the weight of the letters based on their placement.

## Looking for the most optimum combination

Now we will look for the most optimal word combination to be the first and second word in the Wordle game. What we need to do next is calculate the letter weights for each position. The method is as follows.

```
letter_list =['r', 'o', 'a', 's', 't', 'l', 'i', 'n', 'e', 's']letter_value = {}for letter in letter_list:    letter_counter = {}    for i in range(len(letter_list)//2):        loc_counter = 0        for j in range(len(words)):            if words[j][i] == letter:                loc_counter += 1        letter_counter[str(i)] = loc_counter    letter_value[letter] = letter_counter
```

The variable `letter_list` consists of the letters that appear the most. After that, we will count how many occurrences of these letters are at the beginning of the word and so on from all the words in the dataset.

The contents of the `letter_value` are as follows.

```
{'r': {'0': 268, '1': 456, '2': 475, '3': 310, '4': 401}, 'o': {'0': 108, '1': 911, '2': 484, '3': 262, '4': 150}, 'a': {'0': 296, '1': 930, '2': 605, '3': 339, '4': 178}, 's': {'0': 724, '1': 40, '2': 248, '3': 257, '4': 1764}, 't': {'0': 376, '1': 122, '2': 280, '3': 447, '4': 360}, 'l': {'0': 271, '1': 360, '2': 388, '3': 365, '4': 202}, 'i': {'0': 74, '1': 673, '2': 516, '3': 284, '4': 45}, 'n': {'0': 118, '1': 168, '2': 410, '3': 386, '4': 203}, 'e': {'0': 129, '1': 660, '2': 397, '3': 1228, '4': 595}}
```

These results explain that for example, the letter `r` appears as the first letter 268 times, the second letter 456 times, and so on. So we can get the value of each position.

Next, we will calculate the weight of the word combination that we got earlier by using `letter_value`. The method is as follows.

```
result_list = []for i in range(len(best_word_list)):    word_value = 0    for word in best_word_list[i]:        for j, letter in enumerate(word):            if letter in letter_value:                word_value += letter_value[letter][str(j)]    result_list.append(word_value)
```

And here is the result.

```
for i in range(len(result_list)):    print(best_word_list[i], result_list[i])=== result ===['arose', 'unity'] 3219['tears', 'doily'] 5507['stare', 'doily'] 4148['tares', 'doily'] 6565...['lined', 'roast'] 4983['intro', 'leads'] 4282['nitro', 'leads'] 4831['nodal', 'tries'] 5910
```

To get the most optimum combination of values, we can enter the following syntax.

```
result_index = np.argsort(result_list)[::-1]best_word_list[result_index[0]]
```

And the best word combination is `toned` and `rails`.

Lastly, this is the full code of Wordle’s first word search using Python series.

```
import pandas as pdimport numpy as npimport mathdef best_words(words):    distinct_words = []    for word in words:        distinct_words.append(list(set(word)))    letter_counter = {}    for word in distinct_words:        for letter in word:            if letter in letter_counter:                letter_counter[letter] += 1            else:                letter_counter[letter] = 0    word_values = []    for word in distinct_words:        temp_value = 0        for letter in word:            temp_value += letter_counter[letter]        word_values.append(temp_value)    return word_valuesdef get_best_word(words, word_values):    return words[np.argmax(word_values)]def remove_word_contain_letters(words, first_word):    result_word = []    first_word_list = list(set(first_word))        for word in words:        in_word = False        i = 0        while i < len(first_word_list) and not in_word:            if first_word_list[i] in word:                in_word = True            i += 1        if not in_word:            result_word.append(word)    return result_wordwords = []with open('sgb-words.txt') as f:    words = [line.rstrip() for line in f]    distinct_words = []for word in words:    distinct_words.append(list(set(word)))letter_counter = {}for word in distinct_words:    for letter in word:        if letter in letter_counter:            letter_counter[letter] += 1        else:            letter_counter[letter] = 0word_values = best_words(words)first_word = get_best_word(words, word_values)second_words = remove_word_contain_letters(words, first_word)second_values = best_words(second_words)second_word = get_best_word(second_words, second_values)values = best_words(words)values_index = np.argsort(values)[::-1]best_val = 0best_word_list = []top_words = sorted(values, reverse=True)for i, idx in enumerate(values_index):    best_word = words[idx]    second_words = remove_word_contain_letters(words, best_word)    second_values = best_words(second_words)    second_best_word = get_best_word(second_words, second_values)    temp_value = 0    for letter in second_best_word:        temp_value += letter_counter[letter]    if temp_value + top_words[i] >= best_val:        best_val = temp_value + top_words[i]        best_word_list.append([best_word, second_best_word])        letter_list =['r', 'o', 'a', 's', 't', 'l', 'i', 'n', 'e', 's']letter_value = {}for letter in letter_list:    letter_counter = {}    for i in range(len(letter_list)//2):        loc_counter = 0        for j in range(len(words)):            if words[j][i] == letter:                loc_counter += 1        letter_counter[str(i)] = loc_counter    letter_value[letter] = letter_counter    result_list = []for i in range(len(best_word_list)):    word_value = 0    for word in best_word_list[i]:        for j, letter in enumerate(word):            if letter in letter_value:                word_value += letter_value[letter][str(j)]    result_list.append(word_value)result_index = np.argsort(result_list)[::-1]print(best_word_list[result_index[0]])
```

It can be concluded that the words `toned` and `rails` are the best combinations of words to start a Wordle game. In addition to the fact that the letters in the word combination are the letters that appear the most in the dataset, the letters are also placed in the position that has the highest value.

The answer may not be fully optimal because it only relies on statistical data without looking at other considerations. If you have other ways to get the most optimal words in the Wordle game, please write them in the comments.
