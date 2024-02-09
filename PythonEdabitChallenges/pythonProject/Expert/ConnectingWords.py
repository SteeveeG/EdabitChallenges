# link to Challenge : https://edabit.com/challenge/qNQkYzY8GpiFMmndh


def join(lst):
    count = 0
    joined_word = ""
    minimum_shared_letters = sum(len(words) for words in lst)
    for words in range(lst.__len__() - 1):
        word_joined = False
        word_count = lst[words].__len__()
        next_word_count = lst[words + 1].__len__()
        for pre_word in range(lst[words].__len__()):
            preword = lst[words][pre_word:word_count]
            for next_word in range(lst[words + 1].__len__()):
                nexword1 = lst[words + 1][0:next_word_count - next_word]
                if not word_joined:
                    if preword == nexword1:
                        joined_word += lst[words].replace(nexword1, "")
                        if minimum_shared_letters > next_word_count - next_word:
                            minimum_shared_letters = next_word_count - next_word
                        word_joined = True
                        break
                    else:
                        word_joined = False
        if not word_joined:
            joined_word += lst[words]
            count += 1
    if count == lst.__len__()-1:
        minimum_shared_letters=0
    joined_word += lst[lst.__len__() - 1]
    joined = [joined_word, minimum_shared_letters]
    print(joined)


join(["happy", "python", "honey", "yelp", "plank", "lanky"])  # , ["happythoneyelplanky", 1])
join(["move", "over", "very"])  # , ["movery", 3])
join(["oven", "envier", "erase", "serious"])  # , ["ovenvieraserious", 2])
join(["to", "ops", "psy", "syllable"])  # , ["topsyllable", 1])
join(["aaa", "bbb", "ccc", "ddd"])  # , ["aaabbbcccddd", 0])
join(["abcde", "bcdefghi", "efghi", "fghij", "ghijklmnop"])  # , ["abcdefghijklmnop", 4])
join(["aab", "abcccd", "cdeeef", "effff"])  # , ["aabcccdeeeffff", 2])
