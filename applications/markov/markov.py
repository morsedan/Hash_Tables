import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
word_list = words.split()
word_dict = {}
start_words = set()
end_words = set()

caps = ['A', 'B', 'C', 'D', 'E',
        'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O',
        'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z']
punctuation = ['.', '?', '!']

for i in range(len(word_list)-1):
    word = word_list[i]
    if word[0] == '"':
        if word[1] in caps:
            start_words.add(word)
    if word[0] in caps:
        start_words.add(word)
    if word[-1] == '"':
        if word[-2] in punctuation:
            end_words.add(word)
    if word[-1] in punctuation:
        end_words.add(word)
    if word in word_dict:
        a_list = word_dict[word]
        a_list.append(word_list[i+1])
        word_dict[word] = a_list
    else:
        word_dict[word] = [word_list[i+1]]

# TODO: construct 5 random sentences



# for item in word_dict:
#     print(item, "\n", word_dict[item])
def make_sentence():
    beg_word = random.choice(list(start_words))
    # print(beg_word)
    new_sentence_list = [beg_word]
    next_word = random.choice(word_dict[beg_word])
    while next_word not in end_words:
        # print(next_word)
        new_sentence_list.append(next_word)
        next_word = random.choice(word_dict[next_word])
        # print(next_word)
    new_sentence_list.append(next_word)
    print(" ".join(new_sentence_list))
for i in range(5):
    make_sentence()
