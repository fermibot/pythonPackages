def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for apple in apples:
        if s <= a + apple <= t:
            apples_count += 1
    for orange in oranges:
        if s <= b + orange <= t:
            oranges_count += 1
    print(apples_count)
    print(oranges_count)


if __name__ == '__main__':
    countApplesAndOranges()
