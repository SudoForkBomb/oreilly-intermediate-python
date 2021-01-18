import scrabble

longest_word = ""

for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest_word):
        longest_word = word
print(longest_word)


