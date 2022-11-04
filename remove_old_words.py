'''
Quick Script to remove old words from the dataset
'''

with open('data\words.txt') as f:
    words = [line.rstrip() for line in f]
f.close()
print(f"Starting Word List Length --> {len(words)}")

with open('data\previous_words.txt') as p:
    previous_words = p.read().lower().split(' ')

for previous_word in previous_words:
    # print(f"{previous_word} in words --> {previous_word in words}")
    if previous_word in words:
        words.remove(previous_word)
    # print(f"{previous_word} is not in words")

print(f"Ending Word List Length --> {len(words)}")

with open('data\words.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')