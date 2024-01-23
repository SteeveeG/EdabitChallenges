# Link to Challenge : https://edabit.com/challenge/76ibd8jZxvhAwDskb

def tallest_skyscraper(skyscrapers):
    sumedheight = [sum(x) for x in zip(*skyscrapers)]
    highest = max(sumedheight)
    print(highest)


tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
])
tallest_skyscraper([
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
])
tallest_skyscraper([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 1]
])
tallest_skyscraper([
    [0, 0, 0, 1],
    [0, 0, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1]
])
tallest_skyscraper([
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1]
])
tallest_skyscraper([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1]
])