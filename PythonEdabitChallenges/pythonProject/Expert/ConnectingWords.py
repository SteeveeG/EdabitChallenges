# link to Challenge : https://edabit.com/challenge/qNQkYzY8GpiFMmndh

def join(lst):
    no_join_count = 0
    minimum_shared_letters = lst[0].__len__()
    joined_word = ""
    for i in range(lst.__len__() - 1):
        word_count = lst[i].__len__()
        for ii in range(word_count):
            if lst[i][ii:word_count] in lst[i + 1]:
                joined_word += lst[i].replace(lst[i][ii: word_count], "")
                if minimum_shared_letters > lst[i].__len__() - ii: minimum_shared_letters = lst[i].__len__() - ii
                break
            elif ii + 1 == lst[i].__len__():
                no_join_count += 1
                joined_word += lst[i]
    if no_join_count == lst.__len__() - 1: minimum_shared_letters = 0
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
