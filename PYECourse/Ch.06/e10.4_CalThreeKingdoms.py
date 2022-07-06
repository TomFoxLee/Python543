# Ch.06.6.2 Calculate ThreeKingdoms
# Find the most 5 used words and counts
#
# excludes "将军","却说","荆州","二人","不可","不能","如此"
#
# remove duplicate "诸葛亮" or "孔明曰" as "孔明"; "关公" or "云长" as "关羽";
# "玄德" or "玄德曰" as "刘备"; "孟德" or "丞相" as "曹操"

import jieba

excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此"}

txt = open(".\PYECourse\Ch.06\\threekingdoms.txt", "r", encoding="utf-8").read()
words = jieba.lcut(txt)
counts = {}

for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word

    counts[rword] = counts.get(rword, 0) + 1

for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(5):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
