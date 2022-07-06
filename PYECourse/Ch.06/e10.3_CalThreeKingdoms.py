# Ch.06.6.2 Calculate ThreeKingdoms
# Find the most 15 used words and counts

import jieba

txt = open(".\PYECourse\Ch.06\\threekingdoms.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))