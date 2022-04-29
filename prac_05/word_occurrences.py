word_to_occurrences = {}
string_of_words = input("Text: ")
words = string_of_words.split(" ")
words.sort()

longest_count = 0
for word in words:
    if len(word) > longest_count:
        longest_count = len(word)

for word in words:
    if word in word_to_occurrences:
        word_to_occurrences[word] += 1
    else:
        word_to_occurrences[word] = 1

for word, occurrences in word_to_occurrences.items():
    print(f"{word:<{longest_count}} : {occurrences}")
